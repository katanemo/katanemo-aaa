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

    def register(self, client_name, service_id, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        access_api_client = katanemo_identity.AccessControlApi(self._get_access_api_client())
        req = katanemo_identity.OAuthTokenRequest(clientId=client_id, clientSecret=client_secret)
        resp = access_api_client.get_short_term_token(req)
        self.api_access_token = resp.access_token

    def authorize_request(self, access_token, request_path, http_method, request_body):
        auth_api_client = self._get_auth_client()

        req = katanemo_auth.AuthorizationRequest(
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
        
        req = katanemo_identity.OAuthTokenRequest(code=code, clientId=self.client_id, clientSecret=self.client_secret)
        resp = katanemo_identity.AccessControlApi(self._get_access_api_client()).get_o_auth_token(req)
        return resp.access_token, state

    def _get_access_api_client(self):
        # if not self.api_client:
        self.api_client = katanemo_identity.ApiClient(katanemo_identity.Configuration(
            host="https://api.katanemo.com"
        ))
        if self.api_access_token:
          self.api_client.default_headers["Authorization"] = "Bearer " + self.api_access_token
        
        return self.api_client

    def _get_auth_client(self):
        if not self.auth_client:
            self.auth_client = katanemo_auth.ApiClient(katanemo_auth.Configuration(
                host="https://auth.katanemo.com"
            ))
            self.auth_client.default_headers["Authorization"] = "Bearer " + self.api_access_token
        return katanemo_auth.DefaultApi(self.auth_client)
