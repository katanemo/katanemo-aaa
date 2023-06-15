from os import environ as env
import logging as log
from functools import wraps

from utils import AuthError, get_token_auth_header
from katanemo.integrations import KatanemoFlaskAuth
from flask import Flask, request, session, redirect
from dotenv import load_dotenv, find_dotenv

log.basicConfig(level=log.INFO, format="%(message)s")


# load environment variables from .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get('APP_SECRET_KEY')
kauth = KatanemoFlaskAuth(app)

kauth.register(client_name="flask-auth",
    service_id=env.get("KATANEMO_SERVICE_ID"),
    client_id=env.get("KATANEMO_CLIENT_ID"),
    client_secret=env.get("KATANEMO_CLIENT_SECRET"),
)

def requires_authz(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # extract authorization token from http header
        try:
          access_token = None
          if session and session["token"]:
            access_token = session["token"]
          else:
            access_token = get_token_auth_header()
        except AuthError as e:
            log.warning(e)
            log.warning("No access token provided")
            return redirect("/login?redirect_url=" + request.path)
        
        # throw exception if authorization fails
        kauth.authorize_request(
            access_token = access_token,
            request_path = request.path,
            http_method = request.method,
            request_body = None,
        )
        return f(*args, **kwargs)
    
    return decorated


@app.route('/login')
def login():
    redirect_url = "/"
    if 'redirect_url' in request.args:
      redirect_url = request.args['redirect_url']
    login_redirect_url = kauth.authorize(redirect_uri=redirect_url, service_id=env.get("KATANEMO_SERVICE_ID"))
    return redirect(login_redirect_url)


@app.route("/callback")
def callback():
    token, redirect_url = kauth.exchange_oauth_code()
    session["token"] = token
    return redirect(redirect_url)


@app.route("/patient", methods=["POST"])
@requires_authz
def create_patient():
    return 'creating patient'


@app.route('/patient/<patient_id>', methods=['GET'])
@requires_authz
def get_patient(patient_id):
    return 'patient id: ' + patient_id


@app.route('/patient/<patient_id>', methods=['PUT'])
@requires_authz
def update_patient(patient_id):
    return 'patient id: ' + patient_id


@app.route('/patient/<patient_id>', methods=['DELETE'])
@requires_authz
def delete_patient(patient_id):
    return 'patient id: ' + patient_id


app.run(host='0.0.0.0', port=3030, debug=True)
