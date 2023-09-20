
import { Plugin } from '@envelop/core/typings';
import jwtPkg, { DecodeOptions } from 'jsonwebtoken';
import fetch, { Response } from 'node-fetch';
import { GraphQLError } from 'graphql';

const { decode } = jwtPkg;

const contextField = '_kauth'
const API_ENDPOINT = 'https://api.katanemo.com'
const AUTH_ENDPOINT = 'https://auth.katanemo.com'

export const authorizeRequest = async function (context: Record<string, any> = {}, principalToken: string, katanemoApiAccessToken: string, authEndpointInput?: string): Promise<Response> {
  if (!context['params'] || !context['params']['query']) {
    console.log('query not found in request parameters')
    return null
  }
  const query = context['params']['query']
  const authEndpoint = authEndpointInput ?? AUTH_ENDPOINT;
  return await fetch(`${authEndpoint}/arc/authorize`, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${katanemoApiAccessToken}`
    },
    body: JSON.stringify({
      "Token": principalToken,
      "Query": query,
    })
  })
}

export const createTags = async function (context: Record<string, any>, resourceName: string, resourceId: string, tags = {}, apiEndpoint?: string): Promise<Response> {
  const localApiEndpoint = apiEndpoint ?? API_ENDPOINT

  const serviceId = context[contextField]['payload']['aud']
  const accountId = context[contextField]['payload']['accountId']
  const token = context[contextField]['token']
  const payload = JSON.stringify({
    "serviceId": serviceId,
    "accountId": accountId,
    "name": resourceName,
    "resourceId": resourceId,
    "tags": tags,
  })
  return await fetch(`${localApiEndpoint}/service/${serviceId}/tags`, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: payload
  })
}

export const getShortTermToken = async (clientId: string, clientSecret: string, apiEndpoint?: string): Promise<string> => {
  const localApiEndpoint = apiEndpoint ?? API_ENDPOINT
  // get token for api calls to katanemo
  const shortTermTokenResp = await fetch(`${localApiEndpoint}/token`, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      "clientId": clientId,
      "clientSecret": clientSecret,
    })
  })
  if (shortTermTokenResp.status != 200) {
    throw new Error('Failed to get short term token')
  }
  const shortTermTokenJson = await shortTermTokenResp.json()
  return shortTermTokenJson["accessToken"]
}

export type KAuthPluginOptions = {
  serviceId: string;
  accessToken: string;

  clientId?: string;
  clientSecret?: string;

  authEndpoint?: string;
  apiEndpoint?: string;

  jwtDecodeOptions?: DecodeOptions;
};

export type UserPayload = {
  sub: string;
  [key: string]: any;
};

type BuildContext<TOptions extends KAuthPluginOptions> = { [contextField]: UserPayload };

export class UnauthenticatedError extends GraphQLError { }

export const useKauth = <TOptions extends KAuthPluginOptions>(options: TOptions):
  Plugin<BuildContext<TOptions>> => {

  const headerName = 'authorization';
  const tokenType = 'Bearer';

  const extractToken = (ctx: Record<string, any> = {}): string | null => {
    const req = ctx['req'] || ctx['request'] || {};
    const headers = req.headers || ctx['headers'] || null;

    if (!headers) {
      console.warn(`unable to find headers in context, make sure to provide "headers" in context or "req" or "request"!`);
      return null
    }
    let authHeader: string | null = null;
    if (headers[headerName] && typeof headers[headerName] === 'string') {
      authHeader = headers[headerName] || null;
    } else if (headers.get && headers.has && headers.has(headerName)) {
      authHeader = headers.get(headerName) || null;
    }
    if (authHeader === null) {
      return null;
    }

    const split = authHeader.split(' ');

    if (split.length !== 2) {
      throw new Error(`Invalid value provided for header "${headerName}"!`);
    }
    const [type, value] = split;

    if (type !== tokenType) {
      throw new Error(`Unsupported token type provided: "${type}"!`);
    }
    return value;
  }

  return {

    async onContextBuilding({ context, extendContext }) {
      if (context['request'].method === 'OPTIONS') {
        return
      }

      const token = extractToken(context);
      if (!token) {
        throw new UnauthenticatedError('You are not authenticated');
      }
      const decodedPayload = decode(token, { complete: true, ...options.jwtDecodeOptions });
      decodedPayload['token'] = token
      extendContext({
        [contextField]: decodedPayload,
      } as BuildContext<TOptions>);
      const tokenServiceId = decodedPayload['payload']['aud']
      if (tokenServiceId != options.serviceId) {
        throw new UnauthenticatedError('You are not authorized to access this service. Invalid serviceId received in token: ' + tokenServiceId);
      }

      const resp = await authorizeRequest(context, token, options.accessToken, options.authEndpoint)
      if (resp.status != 200) {
        throw new UnauthenticatedError('You are not authorized. Response Status: ' + resp.status);
      }
    },
  }
}
