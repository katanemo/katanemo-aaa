from os import environ as env
import logging as log
from functools import wraps

from katanemo_flask import KatanemoFlaskAuth, requires_authz
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


@app.route('/login')
def login():
    redirect_url = "/"
    if 'redirect_url' in request.args:
        redirect_url = request.args['redirect_url']
    login_redirect_url = kauth.authorize(
        redirect_uri=redirect_url, service_id=env.get("KATANEMO_SERVICE_ID"))
    return redirect(login_redirect_url)


@app.route("/callback")
def callback():
    token, redirect_url = kauth.exchange_oauth_code()
    session["token"] = token
    return redirect(redirect_url)


@app.route("/patient", methods=["POST"])
@requires_authz(kauth)
def create_patient():
    return 'creating patient'


@app.route('/patient/<patient_id>', methods=['GET'])
@requires_authz(kauth)
def get_patient(patient_id):
    return 'patient id: ' + patient_id


@app.route('/patient/<patient_id>', methods=['PUT'])
@requires_authz(kauth)
def update_patient(patient_id):
    return 'patient id: ' + patient_id


@app.route('/patient/<patient_id>', methods=['DELETE'])
@requires_authz(kauth)
def delete_patient(patient_id):
    return 'patient id: ' + patient_id


app.run(host='0.0.0.0', port=3030, debug=True)
