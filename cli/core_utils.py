import base64
from base64 import urlsafe_b64encode
import hashlib
import os
import requests
import json
import logging as log
import jwt
import urllib.parse

log.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s - %(message)s",
)

API_ENDPOINT = os.getenv("API_ENDPOINT") or "https://api.us-west-2.katanemo.dev"
AUTH_ENDPOINT = os.getenv("AUTH_ENDPOINT") or "https://auth.us-west-2.katanemo.dev"

# API_ENDPOINT = 'http://localhost:8090'
# AUTH_ENDPOINT = 'http://localhost:8081'


def get_default_service():
    url = API_ENDPOINT + "/service/3xA"

    res = requests.get(url)
    if res.status_code != 200:
        log.error("Default service get Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        return False

    service = json.loads(res.text)
    service_id = service["serviceId"]
    log.debug("Fetched default service ID: {}".format(service_id))
    return service


def signup_service(developer_email, service_id):
    url = API_ENDPOINT + "/sign-up/" + service_id
    payload = {"emailAddress": developer_email}

    res = requests.post(url, json=payload)
    if res.status_code != 200:
        log.error("Developer Creation Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)

    developer = json.loads(res.text)
    log.debug("created developer with id: {}".format(developer["accountId"]))
    return developer


def confirm_user(confirmation_code):
    url = API_ENDPOINT + "/confirmUser/" + confirmation_code
    res = requests.get(url)
    if res.status_code != 200:
        log.error("User Confirmation Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    user = json.loads(res.text)
    return user


# same as utils.GenerateDevConfirmationCode
def generate_dev_confirmation_code(email, accountId):
    h = hashlib.sha1()
    h.update(email.encode("utf-8"))
    h.update(accountId.encode("utf-8"))
    digest = h.digest()
    return urlsafe_b64encode(digest).decode("utf-8")


# For admin user signning up service, email and service ID are enough
# For users being added to the account later we need to pass the account ID as well.
def set_password(service_id, user_email, session, new_password, account_id=None):
    url = API_ENDPOINT + "/set-password/" + service_id
    payload = {
        "emailAddress": user_email,
        "session": session,
        "password": new_password,
    }
    if account_id:
        payload["accountId"] = account_id
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        log.error("Setting Password Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)


# get password policy of the service
def get_password_policy(service_id):
    url = API_ENDPOINT + "/set-password/" + service_id
    res = requests.get(url)
    if res.status_code != 200:
        log.error("GetPasswordPolicy failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)

    return json.loads(res.text)


def create_service(
    token,
    service_name,
    service_description,
    openapi_spec_file,
    redirect_url,
    display_name=None,
    logo_url=None,
    terms_url=None,
    privacy_url=None,
    docs_url=None,
):
    url = API_ENDPOINT + "/service"
    headers = {"Authorization": "Bearer " + token}

    multipart_form_data = {
        "apiSpecFile": ("apiSpecFile", open(openapi_spec_file, "rb")),
        "description": (None, service_description),
        "redirectUrl": (None, redirect_url),
        "name": (None, service_name),
    }
    if display_name:
        multipart_form_data["displayName"] = (None, display_name)
    if logo_url:
        multipart_form_data["logoUrl"] = (None, logo_url)
    if terms_url:
        multipart_form_data["termsUrl"] = (None, terms_url)
    if privacy_url:
        multipart_form_data["privacyUrl"] = (None, privacy_url)
    if docs_url:
        multipart_form_data["docsUrl"] = (None, docs_url)

    res = requests.post(url, files=multipart_form_data, headers=headers)
    if res.status_code != 200:
        log.error("Service Creation Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    service = json.loads(res.text)
    log.debug("service created with id: {}".format(service["serviceId"]))
    return service


def update_service(service_id, service_name, service_description, openapi_spec_file, redirect_url, token):
    url = f"{API_ENDPOINT}/service/{service_id}"
    headers = {"Authorization": "Bearer {}".format(token)}
    multipart_form_data = {
        "apiSpecFile": ("apiSpecFile", open(openapi_spec_file, "rb")),
        "description": (None, service_description),
        "redirectUrl": (None, redirect_url),
        "name": (None, service_name),
    }

    res = requests.put(url, files=multipart_form_data, headers=headers)
    if res.status_code != 200:
        log.error("Service Update Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    service = json.loads(res.text)
    log.debug("service updated with id: {}".format(service["serviceId"]))
    return service


def get_service(service_id, token):
    url = API_ENDPOINT + "/service/" + service_id
    headers = {"Authorization": "Bearer " + token}

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        log.error("Service Get Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    service = json.loads(res.text)
    return service


def get_services(token):
    url = API_ENDPOINT + "/service"
    headers = {"Authorization": "Bearer " + token}

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        log.error("Services Get Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    services = json.loads(res.text)
    return services


def login(service_id, email, password):
    url = API_ENDPOINT + "/login/" + service_id
    payload = {
        "emailAddress": email,
        "password": password,
        "skipRedirect": True,
    }
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        log.error("Login with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    loginInfo = json.loads(res.text)
    return loginInfo


def get_token_client_key(account_id, client_key_id, client_key_secret):
    url = "{}/oauth/{}/token".format(API_ENDPOINT, account_id)
    payload = {
        "clientId": client_key_id,
        "clientSecret": client_key_secret,
    }
    res = requests.post(url, json=payload)
    if res.status_code != 200:
        log.error("Login with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return json.loads(res.text)


def create_tags(serviceId, accountId, name, resourceId, token, tags):
    url = API_ENDPOINT + "/org/{}/tags".format(accountId)
    payload = {
        "serviceId": serviceId,
        "accountId": accountId,
        "name": name,
        "resourceId": resourceId,
        "tags": tags,
    }

    res = requests.post(url, json=payload, headers={"Authorization": "Bearer " + token})
    if res.status_code != 200:
        log.error("Tag assignment failed: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)


def assume_role(role_id, token):
    url = API_ENDPOINT + "/role/assume/" + role_id
    res = requests.get(url, headers={"Authorization": "Bearer " + token})
    if res.status_code != 200:
        log.error("Tag assignment failed: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    token_info = json.loads(res.text)
    return token_info


def authorizeRequest(token, path, operation, body=None):
    log.info("authorizing request for path: {} and operation: {}".format(path, operation))
    url = AUTH_ENDPOINT + "/authorize"
    payload = {"Token": token, "Path": path, "HttpMethod": operation, "RequestBody": json.dumps(body)}
    res = requests.post(url, json=payload)
    log.info("authorizeRequest response: {}".format(res.status_code))
    if res.status_code == 200:
        return True
    return False


def get_role_by_name(account_id, role_name, oauth_token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", oauth_token))}
    res = requests.get(API_ENDPOINT + "/role/byname/{}/{}".format(account_id, role_name), headers=headers)
    if res.status_code != 200:
        log.error("Failed to get role by name: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_role_by_id(account_id, role_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(API_ENDPOINT + f"/org/{account_id}/role/{role_id}", headers=headers)
    if res.status_code != 200:
        log.error("Failed to get role by id: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def update_role(account_id, role_id, role, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}

    res = requests.put(API_ENDPOINT + f"/org/{account_id}/role/{role_id}", json=role, headers=headers)
    if res.status_code != 200:
        log.error("Failed to update role: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_roles(account_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(API_ENDPOINT + f"/org/{account_id}/role", headers=headers)
    if res.status_code != 200:
        log.error("Failed to get roles: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_roles_for_service(service_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    path = API_ENDPOINT + f"/arc/{service_id}/role"
    res = requests.get(path, headers=headers)
    if res.status_code != 200:
        log.error("Failed to get roles: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def init_arc(service_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    path = API_ENDPOINT + f"/arc/{service_id}/init"
    res = requests.get(path, headers=headers)
    if res.status_code != 200:
        log.error("Failed to get roles: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_tags_for_service(service_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    path = API_ENDPOINT + f"/arc/{service_id}/tags"
    res = requests.get(path, headers=headers)
    if res.status_code != 200:
        log.error("Failed to get tags: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def make_policy_content_from_policy_list(policy_list):
    policy_content = {"version": 1, "type": "default", "policy": policy_list}
    return json.dumps(policy_content)


def create_role(account_id: str, service_id: str, role_name: str, policy_content: str, token: str):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    url = API_ENDPOINT + f"/org/{account_id}/role"

    policy = {
        "policyContent": policy_content,
    }

    payload = {"accountId": account_id, "serviceId": service_id, "rolename": role_name, "policy": policy}

    res = requests.post(url, json=payload, headers=headers)
    if res.status_code != 200:
        log.error("Role Creation with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    role = json.loads(res.text)
    log.debug("role created with id: {}".format(role["roleId"]))
    return role


def decode_token(token):
    decoded_token = jwt.decode(
        token,
        "xxx",
        algorithms=["RS256"],
        options={"verify_signature": False},
    )
    return decoded_token


def get_roleid_from_token(token):
    decoded_token = decode_token(token)
    return decoded_token["scp"][0]


def get_account_id_from_token(token):
    decoded_token = decode_token(token)
    return decoded_token["accountId"]


def create_client_key(account_id, role_id, client_name, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    url = f"{API_ENDPOINT}/org/{account_id}/keys"
    payload = {
        "defaultRoleId": role_id,
        "clientName": client_name,
    }
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code != 200:
        log.error("client key generation failed: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return json.loads(res.text)


def get_client_key(account_id, client_key_id, token):
    url = f"{API_ENDPOINT}/org/{account_id}/keys/{client_key_id}"
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        log.error("Get client key failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return json.loads(res.text)


def get_client_keys(account_id, token):
    headers = {"Authorization": "Bearer {}".format(token)}
    url = f"{API_ENDPOINT}/org/{account_id}/keys"
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        log.error("Get client keys failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return json.loads(res.text)


def delete_client_keys(account_id, client_key_id):
    url = "{}/clientkey/{}/{}".format(API_ENDPOINT, account_id, client_key_id)
    res = requests.delete(url)
    if res.status_code != 200:
        log.error("Login with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return json.loads(res.text)


def create_oidc_connection(token, account_id, org_name, client_id, client_secret, service_id):
    url = f"{API_ENDPOINT}/org/{account_id}/sso-connections/oidc"

    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {
        "orgName": org_name,
        "clientId": client_id,
        "clientSecret": client_secret,
        "accountId": account_id,
        "serviceId": service_id,
    }
    res = requests.post(url, headers=headers, json=payload)
    if res.status_code != 200:
        log.error("Connection Creation Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    connection = json.loads(res.text)
    log.debug("Connection created with id: {}".format(connection["connectionId"]))
    return connection


def create_saml_connection(token, account_id, service_id):
    url = f"{API_ENDPOINT}/org/{account_id}/sso-connections/saml"
    headers = {"Authorization": "Bearer {}".format(token)}
    data = {
        "accountId": account_id,
        "serviceId": service_id,
    }
    res = requests.post(url, headers=headers, json=data)
    if res.status_code != 200:
        log.error("Connection Creation Failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    connection = json.loads(res.text)
    print("Connection:", connection)
    print("Connection created with id: {}".format(connection["connectionId"]))
    return connection


def get_users(account_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(API_ENDPOINT + f"/org/{account_id}/user", headers=headers)
    if res.status_code != 200:
        log.error("Failed to get users: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_user(account_id, user_id, token):
    encoded_user_id = urllib.parse.quote(user_id)
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(f"{API_ENDPOINT}/org/{account_id}/user/{encoded_user_id}", headers=headers)
    if res.status_code != 200:
        log.error("Failed to get user: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


# roles should be list of strings if present (array of role IDs)
# tags is map of strings to map of strings e.g. {"k1":["v11", "v12"], "k2":["v21"]}
def create_user(account_id, user_email, token, roles=None, tags=None):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    url = API_ENDPOINT + f"/org/{account_id}/user"
    payload = {"accountId": account_id, "userId": user_email}
    if roles:
        payload["roles"] = roles
    if tags:
        payload["tags"] = json.loads(tags)

    res = requests.post(url, json=payload, headers=headers)
    if res.status_code != 200:
        log.error("Adding user with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    user = json.loads(res.text)
    log.debug("user created: {}".format(user))
    return user


def assign_role(principal_id, role_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    url = f"{API_ENDPOINT}/assignrole"
    payload = {"principalId": principal_id, "roleId": role_id}

    res = requests.post(url, json=payload, headers=headers)
    if res.status_code != 200:
        log.error("Assigning role to principal failed with status code: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    principal = json.loads(res.text)
    log.debug("role assignment successful: {}".format(principal))
    return principal


def get_own_organization(token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(f"{API_ENDPOINT}/org/", headers=headers)
    if res.status_code != 200:
        log.error("Failed to get own organization: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_organization(account_id, token):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(f"{API_ENDPOINT}/org/{account_id}", headers=headers)
    if res.status_code != 200:
        log.error("Failed to get organization: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_audit_log_events(token, service_id, account_id, start_time, end_time):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    res = requests.get(
        f"{API_ENDPOINT}/audit-logs/service/{service_id}/account/{account_id}?startTime={start_time}&endTime={end_time}",
        headers=headers,
    )
    if res.status_code != 200:
        log.error("Failed to get audit logs: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def get_public_key(service_id):
    url = f"{API_ENDPOINT}/service/{service_id}/.well-known/jwks.json"
    res = requests.get(url)
    if res.status_code != 200:
        log.error("Failed to get public key: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
    return res.json()


def add_access_logs(token, logs):
    headers = {"Authorization": "Bearer {}".format(os.getenv("BEARER_TOKEN", token))}
    url = f"{AUTH_ENDPOINT}/access-logs"
    entry = {
        "accountId": "a",
        "serviceId": "b",
        "path": "",
        "operation": "",
        "authenticationCode": 200,
        "authorizationCode": 300,
    }
    payload = [entry]

    res = requests.post(url, json=payload, headers=headers)
    if res.status_code != 200:
        log.error("posting logs failed: {}".format(res.status_code))
        log.error("Reason: {}".format(res.reason))
        exit(1)
