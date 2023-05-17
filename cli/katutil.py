import os
import logging as log
import core_utils
import argparse
import json
import katanemo_sdk

log.basicConfig(level=log.INFO, format="%(message)s")

DEFAULT_API_ENDPOINT = "https://api.us-west-2.katanemo.dev"


parser = argparse.ArgumentParser(prog="PROG")

# create sub-parser
sub_parsers = parser.add_subparsers(help="sub-command help", dest="sub_parser")

init_service_cmd = sub_parsers.add_parser(
    "init-service", help="registers service with katanemo")
init_service_cmd.add_argument(
    "--service_name", type=str, help="service name", required=True)
init_service_cmd.add_argument(
    "--service_description", type=str, help="service description", required=True)
init_service_cmd.add_argument(
    "--api_spec", type=str, help="open api spec for service", required=True)
init_service_cmd.add_argument(
    "--redirect_uri", type=str, help="redirect url service", required=True)
init_service_cmd.add_argument(
    "--token", type=str, help="access token", required=True)
init_service_cmd.add_argument(
    "--print_output", type=bool, help="print response from server", default=False)

get_service_cmd = sub_parsers.add_parser(
    "get-service", help="get service details")
get_service_cmd.add_argument(
    "--subscribed_service_id", type=str, help="service id", required=True)
get_service_cmd.add_argument(
    "--service_id", type=str, help="service id", required=True)
get_service_cmd.add_argument("--email", type=str, help="", required=True)
get_service_cmd.add_argument(
    "--password", type=str, help="", default="test123")

get_token_cmd = sub_parsers.add_parser(
    "login-with-password", help="get token for service")
get_token_cmd.add_argument("--service_id", type=str,
                           help="service id", required=True)
get_token_cmd.add_argument("--email", type=str, help="", required=True)
get_token_cmd.add_argument("--password", type=str, help="", required=True)

get_token_cmd = sub_parsers.add_parser(
    "get-token-client-key", help="exchange client key for token")
get_token_cmd.add_argument("--account_id", type=str, help="", required=True)
get_token_cmd.add_argument("--client_key_id", type=str, help="", required=True)
get_token_cmd.add_argument("--client_key_secret",
                           type=str, help="", required=True)

signup_service_cmd = sub_parsers.add_parser(
    "signup-service", help="sign up for service")
signup_service_cmd.add_argument(
    "--service_id", type=str, help="", required=True)
signup_service_cmd.add_argument("--email", type=str, help="", required=True)

add_user_cmd = sub_parsers.add_parser(
    "add-user", help="add user to an organization")
add_user_cmd.add_argument("--account_id", type=str, help="", required=True)
add_user_cmd.add_argument("--email", type=str, help="", required=True)
add_user_cmd.add_argument("--tags", type=str, help="", default=None)
add_user_cmd.add_argument("--token", type=str, help="", required=True)

get_auth_service_cmd = sub_parsers.add_parser(
    "get-default-service", help="get katanemo auth service")

confirm_set_password_cmd = sub_parsers.add_parser(
    "confirm-and-set-password", help="confirm and set password")
confirm_set_password_cmd.add_argument("--code", type=str, help="", default="")
confirm_set_password_cmd.add_argument(
    "--service_id", type=str, help="", required=True)
confirm_set_password_cmd.add_argument(
    "--account_id", type=str, help="", default="")
confirm_set_password_cmd.add_argument(
    "--email", type=str, help="", required=True)
confirm_set_password_cmd.add_argument(
    "--password", type=str, help="", required=True)

get_password_policy = sub_parsers.add_parser(
    "get-password-policy", help="gets passport policy for service")
get_password_policy.add_argument(
    "--service_id", type=str, help="", required=True)

create_client_key_cmd = sub_parsers.add_parser(
    "create-client-key", help="creates client key and secret with specified role"
)
create_client_key_cmd.add_argument(
    "--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
create_client_key_cmd.add_argument(
    "--role_id", type=str, help="", required=True)
create_client_key_cmd.add_argument(
    "--client_name", type=str, help="", required=True)
create_client_key_cmd.add_argument(
    "--token", type=str, help="", default=os.getenv("TOKEN"))

get_client_key_cmd = sub_parsers.add_parser(
    "get-client-key", help="get details of client key")
get_client_key_cmd.add_argument(
    "--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
get_client_key_cmd.add_argument(
    "--client_key_id", type=str, help="", required=True)

get_client_keys_cmd = sub_parsers.add_parser(
    "get-client-keys", help="gets list of client keys for account")
get_client_keys_cmd.add_argument(
    "--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))

delete_client_key_cmd = sub_parsers.add_parser(
    "delete-client-key", help="deletes a client key")
delete_client_key_cmd.add_argument(
    "--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
delete_client_key_cmd.add_argument(
    "--client_key_id", type=str, help="", required=True)

create_and_assign_role_cmd = sub_parsers.add_parser(
    "create-role", help="create a role")
create_and_assign_role_cmd.add_argument(
    "--account_id", type=str, required=True)
create_and_assign_role_cmd.add_argument(
    "--service_id", type=str, required=True)
create_and_assign_role_cmd.add_argument("--role_name", type=str, required=True)
create_and_assign_role_cmd.add_argument("--policies", type=str, required=True)
create_and_assign_role_cmd.add_argument("--token", type=str, required=True)

assign_role_cmd = sub_parsers.add_parser(
    "assign-role", help="assign role to a principal")
assign_role_cmd.add_argument("--principal_id", type=str, required=True)
assign_role_cmd.add_argument("--role_id", type=str, required=True)
assign_role_cmd.add_argument("--token", type=str, required=True)

get_roles_cmd = sub_parsers.add_parser(
    "get-roles", help="get roles for an account")
get_roles_cmd.add_argument("--account_id", type=str, required=True)
get_roles_cmd.add_argument("--token", type=str, required=True)

args = parser.parse_args()


def get_api_client(token=None):
    configuration = katanemo_sdk.Configuration(
        host=os.getenv("API_ENDPOINT", DEFAULT_API_ENDPOINT),
    )
    api_client = katanemo_sdk.ApiClient(configuration)
    if token:
        api_client.default_headers["Authorization"] = "Bearer " + token
    return katanemo_sdk.DefaultApi(api_client)


if args.sub_parser == "init-service":
    resp = get_api_client(args.token).create_service(
        args.service_name, args.service_description, args.redirect_uri, args.api_spec)
    print(resp.json(by_alias=True))

    service_id = resp.service_id
    onboardURL = resp.onboard_url

    log.info("")
    log.info("Successfully Created Service ✅")
    log.info("Your Service ID is: %s " % service_id)
    log.info(
        "Katanemo's hosted Sign-up/Login URL for your service: %s " % onboardURL)
    log.info("Katanemo's Console to manage your customers % s" %
              "https://console.us-west-2.katanemo.dev/sign-up/3xA")
    log.info("")


if args.sub_parser == "get-service":
    log.info("getting login credentials")
    login_details = core_utils.login(
        args.subscribed_service_id, args.email, args.password)
    log.info("login successful")

    resp = core_utils.get_service(args.service_id, login_details["token"])
    print(json.dumps(resp))


if args.sub_parser == "login-with-password":
    login_with_password_request = katanemo_sdk.LoginWithPasswordRequest(
        emailAddress=args.email, password=args.password, skipRedirect=True)
    api_response = get_api_client().login(
        args.service_id, login_with_password_request)
    print(api_response.json(by_alias=True))


if args.sub_parser == "get-default-service":
    api_response = get_api_client().get_default_service()
    print(api_response.json(by_alias=True))


if args.sub_parser == "signup-service":
    api_response = get_api_client().service_signup(
        args.service_id, katanemo_sdk.SignupRequest(email_address=args.email))
    print(api_response.json(by_alias=True))


if args.sub_parser == "confirm-and-set-password":
    code = args.code
    if code == "-" or code == "":
        code = core_utils.generate_dev_confirmation_code(
            args.email, args.account_id)
    api_client = get_api_client()
    confirmed_user = api_client.confirm_user(code)
    api_client.set_password(args.service_id,
                            katanemo_sdk.SetPasswordRequest(
                                emailAddress=args.email,
                                session=confirmed_user.session,
                                password=args.password,
                            ))


if args.sub_parser == "get-password-policy":
    password_policy = core_utils.get_password_policy(args.service_id)


if args.sub_parser == "create-client-key":
    resp = core_utils.create_client_key(
        args.account_id, args.role_id, args.client_name, args.token)
    print(json.dumps(resp))


if args.sub_parser == "get-token-client-key":
    resp = core_utils.get_token_client_key(
        args.account_id, args.client_key_id, args.client_key_secret)
    print(json.dumps(resp))


if args.sub_parser == "get-client-key":
    resp = core_utils.get_client_key(args.account_id, args.client_key_id)
    print(json.dumps(resp))


if args.sub_parser == "get-client-keys":
    resp = core_utils.get_client_keys(args.account_id)
    print(json.dumps(resp))


if args.sub_parser == "delete-client-key":
    resp = core_utils.delete_client_keys(args.account_id, args.client_key_id)
    print(json.dumps(resp))


if args.sub_parser == "create-role":
    policiesJson = json.loads(args.policies)
    roles = core_utils.create_role(
        args.account_id,
        args.service_id,
        args.role_name,
        json.dumps(policiesJson),
        args.token,
    )

    print(json.dumps(roles))

if args.sub_parser == "assign-role":
    resp = core_utils.assign_role(
        args.principal_id,
        args.role_id,
        args.token,
    )

    print(json.dumps(resp))


if args.sub_parser == "get-roles":
    api_response = get_api_client(
        args.token).get_roles_for_account(args.account_id)
    print('[' + ','.join([role.json(by_alias=True)
          for role in api_response]) + ']')


if args.sub_parser == "add-user":
    api_response = get_api_client(
        args.token).create_user_for_account(args.account_id, katanemo_sdk.User(account_id=args.account_id, user_id=args.email, tags=json.loads(args.tags)))

    print(api_response.json(by_alias=True))
    