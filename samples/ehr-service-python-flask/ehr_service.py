# noqa
from functools import wraps
import os
from os import environ as env

from utils import get_token_auth_header
# from katanemo.authentication import get_sts_token, authorize_request, create_katanemo_context
from katanemo.integrations import KatanemoFlaskAuth
from flask import Flask, request, session, redirect
from dotenv import load_dotenv, find_dotenv

# load environment variables from .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
# app.secret_key = os.getenv('APP_SECRET_KEY')
kauth = KatanemoFlaskAuth(app)

kauth.register("flask-auth",
    client_id=env.get("KATANEMO_CLIENT_ID"),
    client_secret=env.get("KATANEMO_CLIENT_SECRET"),
    client_secret=env.get("KATANEMO_SERVICE_ID"),
)


def requires_authz(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # extract authorization token from http header
        access_token = get_token_auth_header()
        
        if not access_token:
            # redirect to login page
            pass
        
        # throw exception if authorization fails
        kauth.authorize_request(
            access_token = access_token,
            request_path = request.path,
            http_method = request.method,
            request_body = None,
        )
        return f(*args, **kwargs)


@app.route('/login')
def login():
    redirect_url = kauth.authorize_redirect("flask-auth", redirect_uri="/callback")
    redirect(redirect_url)


@app.route("/callback")
def callback():
    token = kauth.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route('/patient', methods=['POST'])
@requires_authz()
def create_patient():
    return 'creating patient'


@requires_authz()
@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    return 'patient id: ' + patient_id


@requires_authz()
@app.route('/patient/<patient_id>', methods=['PUT'])
def update_patient(patient_id):
    return 'patient id: ' + patient_id


@requires_authz()
@app.route('/patient/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    return 'patient id: ' + patient_id


app.run(host='0.0.0.0', port=3030, debug=True)
