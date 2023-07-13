from flask import Flask, request, session, redirect
from functools import wraps
import logging as log

from katanemo_flask.auth_error import AuthError, get_token_auth_header


def requires_authz(kauth):
    def requires_authz_inner(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # extract authorization token from http header
            try:
                print('checking to see if token is in session')
                access_token = None
                if session and session["token"]:
                    print('token is in session')
                    access_token = session["token"]
                else:
                    print('checking to see if auth header has token')
                    access_token = get_token_auth_header()
                    print('access token: ' + access_token)
            except AuthError as e:
                log.warning(e)
                log.warning("No access token provided")
                return redirect("/login?redirect_url=" + request.path)

            # throw exception if authorization fails
            kauth.authorize_request(
                access_token=access_token,
                request_path=request.path,
                http_method=request.method,
                request_body=None,
            )
            return f(*args, **kwargs)

        return decorated
    return requires_authz_inner
