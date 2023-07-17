import json
import katanemo_identity
import katanemo_auth
import requests
from flask import request as flask_request

class KatanemoFlaskAuth:
    
    def __init__(self, app):
        self.app = app
        self.api_client = None
        self.auth_client = None
        self.api_access_token = None
        self.client_id = None
        self.api_config = katanemo_identity.Configuration()

    def register(self, client_name, service_id, client_id, client_secret):
        """ registers the client with katanemo """
        """ client_name: the name of the client """
        """ service_id: the id of the service to register """
        """ client_id: the id of the client """
        """ client_secret: the secret of the client """
        self.client_id = client_id
        self.client_secret = client_secret
        if not client_id or not client_secret:
          raise Exception("Client id and secret must be provided")
        access_api_client = katanemo_identity.AccessControlApi(self._get_access_api_client())
        req = katanemo_identity.OAuthTokenRequest(clientId=client_id, clientSecret=client_secret)
        resp = access_api_client.get_short_term_token(req)
        self.api_access_token = resp.access_token

    def authorize_request(self, access_token, request_path, http_method, request_body):
        """ authorizes the request with katanemo """
        """ access_token: the access token to use for authorization """
        """ request_path: the path of the request """
        """ http_method: the http method of the request """
        """ request_body (optional): the body of the request"""
        if not self.api_access_token:
            raise Exception("No access token provided, initlize the sdk with a client id and secret")
        auth_api_client = self._get_auth_client()

        req = katanemo_auth.AuthorizationRequest(
            token=access_token,
            path=request_path,
            http_method=http_method,
            request_body=request_body,
        )
        auth_api_client.authorize_request(req)
    
    def authorize(self, redirect_uri, service_id):
        """ redirects to katanemo login page """
        """ redirect_uri: the url to redirect to after successful login """
        """ service_id: the id of the service to authorize """
        api_endpoint = self.api_config.get_host_settings()[0]['url']
        authorizeUrl = "{}/authorize?state={}&service={}".format(api_endpoint, redirect_uri, service_id)
        resp = requests.get(authorizeUrl, allow_redirects=False)
        if resp.status_code != 302:
            raise Exception("Failed to get login redirect url")
        login_redirect_url = resp.headers["Location"]
        return login_redirect_url

    def exchange_oauth_code(self):
        """ exchanges the oauth code for an access token """
        """ expects code and state to be in the request args """
        if not self.api_access_token:
            raise Exception("No access token provided, initlize the sdk with a client id and secret")
        code = flask_request.args.get("code")
        state = flask_request.args.get("state")
        if not code:
            raise Exception("No oauth code provided")
        
        req = katanemo_identity.OAuthTokenRequest(code=code, clientId=self.client_id, clientSecret=self.client_secret)
        resp = katanemo_identity.AccessControlApi(self._get_access_api_client()).get_o_auth_token(req)
        return resp.access_token, state

    def _get_access_api_client(self):
        """ Get the access api client, creating it if necessary """
        self.api_client = katanemo_identity.ApiClient(katanemo_identity.Configuration())
        if self.api_access_token:
          self.api_client.default_headers["Authorization"] = "Bearer " + self.api_access_token
        
        return self.api_client

    def _get_auth_client(self):
        """ Get the auth client, creating it if necessary """
        if not self.auth_client:
            self.auth_client = katanemo_auth.ApiClient(katanemo_auth.Configuration())
            self.auth_client.default_headers["Authorization"] = "Bearer " + self.api_access_token
        return katanemo_auth.DefaultApi(self.auth_client)
