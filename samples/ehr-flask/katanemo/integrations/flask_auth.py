import json
import katanemo_sdk
import katanemo_auth_sdk
import requests
from flask import request as flask_request

class KatanemoFlaskAuth:
    
    def __init__(self, app):
        self.app = app
        self.api_client = None
        self.auth_client = None
        self.api_access_token = None
        self.client_id = None

    def register(self, client_name, service_id, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        access_api_client = katanemo_sdk.AccessControlApi(self._get_access_api_client())
        req = katanemo_sdk.OAuthTokenRequest(clientId=client_id, clientSecret=client_secret)
        resp = access_api_client.get_short_term_token(req)
        self.api_access_token = resp.access_token

    def authorize_request(self, access_token, request_path, http_method, request_body):
        auth_api_client = self._get_auth_client()

        req = katanemo_auth_sdk.AuthorizationRequest(
            token=access_token,
            path=request_path,
            http_method=http_method,
            request_body=request_body,
        )
        auth_api_client.authorize_request(req)
    
    def authorize(self, redirect_uri, service_id):
        authorizeUrl = "https://api.katanemo.com/authorize?state={}&service={}".format(redirect_uri, service_id)
        resp = requests.get(authorizeUrl, allow_redirects=False)
        if resp.status_code != 302:
            raise Exception("Failed to get login redirect url")
        login_redirect_url = resp.headers["Location"]
        return login_redirect_url

    def exchange_oauth_code(self):
        code = flask_request.args.get("code")
        state = flask_request.args.get("state")
        if not code:
            raise Exception("No oauth code provided")
        
        req = katanemo_sdk.OAuthTokenRequest(code=code, clientId=self.client_id, clientSecret=self.client_secret)
        resp = katanemo_sdk.AccessControlApi(self._get_access_api_client()).get_o_auth_token(req)
        return resp.access_token, state

    def _get_access_api_client(self):
        # if not self.api_client:
        self.api_client = katanemo_sdk.ApiClient(katanemo_sdk.Configuration(
            host="https://api.katanemo.com"
        ))
        if self.api_access_token:
          self.api_client.default_headers["Authorization"] = "Bearer " + self.api_access_token
        
        return self.api_client

    def _get_auth_client(self):
        if not self.auth_client:
            self.auth_client = katanemo_auth_sdk.ApiClient(katanemo_auth_sdk.Configuration(
                host="https://auth.katanemo.com"
            ))
            self.auth_client.default_headers["Authorization"] = "Bearer " + self.api_access_token
        return katanemo_auth_sdk.DefaultApi(self.auth_client)
