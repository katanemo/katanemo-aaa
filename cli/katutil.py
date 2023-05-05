import os
import logging as log
import core_utils
import argparse
import json

log.basicConfig(level=log.INFO, format="%(message)s")


parser = argparse.ArgumentParser(prog="PROG")

# create sub-parser
sub_parsers = parser.add_subparsers(help="sub-command help", dest="sub_parser")

init_service_cmd = sub_parsers.add_parser("init-service", help="registers service with katanemo")
init_service_cmd.add_argument("--service_name", type=str, help="service name", required=True)
init_service_cmd.add_argument("--service_description", type=str, help="service name", required=False)
init_service_cmd.add_argument("--api_spec", type=str, help="open api spec for service", required=True)
init_service_cmd.add_argument("--redirect_uri", type=str, help="redirect url service", required=True)
init_service_cmd.add_argument("--token", type=str, help="access token", required=True)

create_service_cmd = sub_parsers.add_parser("create-service", help="registers service with katanemo")
create_service_cmd.add_argument("--name", type=str, help="", required=True)
create_service_cmd.add_argument("--description", type=str, help="service description", default="")
create_service_cmd.add_argument("--openapi_spec", type=str, help="open api spec for service", required=True)
create_service_cmd.add_argument("--redirect_url", type=str, help="redirect url service", required=True)
create_service_cmd.add_argument("--service_id", type=str, help="service id", default=os.getenv("SERVICE_ID"))
create_service_cmd.add_argument("--email", type=str, help="", required=True)
create_service_cmd.add_argument("--password", type=str, help="", default="test123")

get_service_cmd = sub_parsers.add_parser("get-service", help="get service details")
get_service_cmd.add_argument("--subscribed_service_id", type=str, help="service id", required=True)
get_service_cmd.add_argument("--service_id", type=str, help="service id", required=True)
get_service_cmd.add_argument("--email", type=str, help="", required=True)
get_service_cmd.add_argument("--password", type=str, help="", default="test123")


get_token_cmd = sub_parsers.add_parser("login-with-password", help="")
get_token_cmd.add_argument("--service_id", type=str, help="service id", default=os.getenv("SERVICE_ID"))
get_token_cmd.add_argument("--email", type=str, help="", required=True)
get_token_cmd.add_argument("--password", type=str, help="", default="MyTestPassword")
get_token_cmd.add_argument("--account_id", type=str, help="")

get_token_cmd = sub_parsers.add_parser("get-token-client-key", help="")
get_token_cmd.add_argument("--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
get_token_cmd.add_argument("--client_key_id", type=str, help="", required=True)
get_token_cmd.add_argument("--client_key_secret", type=str, help="", required=True)

signup_service_cmd = sub_parsers.add_parser("signup-service", help="")
signup_service_cmd.add_argument("--service_id", type=str, help="", required=True)
signup_service_cmd.add_argument("--email", type=str, help="", required=True)

add_user_cmd = sub_parsers.add_parser("add-user", help="")
add_user_cmd.add_argument("--account_id", type=str, help="", required=True)
add_user_cmd.add_argument("--email", type=str, help="", required=True)
add_user_cmd.add_argument("--tags", type=str, help="", default=None)
add_user_cmd.add_argument("--token", type=str, help="", required=True)

get_auth_service_cmd = sub_parsers.add_parser("get-default-service", help="")

confirm_set_password_cmd = sub_parsers.add_parser("confirm-and-set-password", help="")
confirm_set_password_cmd.add_argument("--code", type=str, help="", default="")
confirm_set_password_cmd.add_argument("--service_id", type=str, help="", required=True)
confirm_set_password_cmd.add_argument("--account_id", type=str, help="", default="")
confirm_set_password_cmd.add_argument("--email", type=str, help="", required=True)
confirm_set_password_cmd.add_argument("--password", type=str, help="", required=True)

get_password_policy = sub_parsers.add_parser("get-password-policy", help="")
get_password_policy.add_argument("--service_id", type=str, help="", required=True)

create_client_key_cmd = sub_parsers.add_parser("create-client-key", help="")
create_client_key_cmd.add_argument("--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
create_client_key_cmd.add_argument("--role_id", type=str, help="", required=True)
create_client_key_cmd.add_argument("--client_name", type=str, help="", required=True)
create_client_key_cmd.add_argument("--token", type=str, help="", default=os.getenv("TOKEN"))

get_client_key_cmd = sub_parsers.add_parser("get-client-key", help="")
get_client_key_cmd.add_argument("--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
get_client_key_cmd.add_argument("--client_key_id", type=str, help="", required=True)

get_client_keys_cmd = sub_parsers.add_parser("get-client-keys", help="")
get_client_keys_cmd.add_argument("--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))

delete_client_key_cmd = sub_parsers.add_parser("delete-client-key", help="")
delete_client_key_cmd.add_argument("--account_id", type=str, help="", default=os.getenv("ACCOUNT_ID"))
delete_client_key_cmd.add_argument("--client_key_id", type=str, help="", required=True)

create_and_assign_role_cmd = sub_parsers.add_parser("create-role", help="")
create_and_assign_role_cmd.add_argument("--account_id", type=str, required=True)
create_and_assign_role_cmd.add_argument("--service_id", type=str, required=True)
create_and_assign_role_cmd.add_argument("--role_name", type=str, required=True)
create_and_assign_role_cmd.add_argument("--policies", type=str, required=True)
create_and_assign_role_cmd.add_argument("--token", type=str, required=True)

assign_role_cmd = sub_parsers.add_parser("assign-role", help="")
assign_role_cmd.add_argument("--principal_id", type=str, required=True)
assign_role_cmd.add_argument("--role_id", type=str, required=True)
assign_role_cmd.add_argument("--token", type=str, required=True)

get_roles_cmd = sub_parsers.add_parser("get-roles", help="")
get_roles_cmd.add_argument("--account_id", type=str, required=True)
get_roles_cmd.add_argument("--token", type=str, required=True)

args = parser.parse_args()

if args.sub_parser == "create-service":
    login_details = core_utils.login(args.service_id, args.email, args.password)

    resp = core_utils.create_service(
        login_details["token"],
        args.name,
        args.description,
        args.openapi_spec,
        args.redirect_url,
    )
    service_id = resp["serviceId"]

    print(json.dumps({"message": "service registered", "serviceId": service_id}))

if args.sub_parser == "init-service":
    resp = core_utils.create_service(
        args.token,
        args.service_name,
        args.service_description,
        args.api_spec,
        args.redirect_uri,
    )
    service_id = resp["serviceId"]
    onboardURL = resp["onboardURL"]


    print("")
    print("Successfully Created Service ✅")
    print("Your Service ID is: %s " % service_id)
    print("Katanemo's hosted Sign-up/Login URL for your service: %s " % onboardURL)
    print("Katanemo's Console to manage your customers % s" % "https://console.us-west-2.katanemo.dev/sign-up/3xA")
    print("")


if args.sub_parser == "get-service":
    log.info("getting login credentials")
    login_details = core_utils.login(args.subscribed_service_id, args.email, args.password)
    log.info("login successful")

    resp = core_utils.get_service(args.service_id, login_details["token"])
    print(json.dumps(resp))


if args.sub_parser == "login-with-password":
    res = core_utils.login(args.service_id, args.email, args.password, args.account_id)
    print(json.dumps(res))


if args.sub_parser == "get-default-service":
    resp = core_utils.get_default_service()
    print(json.dumps(resp))


if args.sub_parser == "signup-service":
    resp = core_utils.signup_service(args.email, args.service_id)
    print(json.dumps(resp))


if args.sub_parser == "confirm-and-set-password":
    code = args.code
    if code == "":
        code = core_utils.generate_dev_confirmation_code(args.email, args.account_id)
    user_session = core_utils.confirm_user(code)["session"]
    core_utils.set_password(args.service_id, args.email, user_session, args.password, args.account_id)


if args.sub_parser == "get-password-policy":
    password_policy = core_utils.get_password_policy(args.service_id)


if args.sub_parser == "create-client-key":
    resp = core_utils.create_client_key(args.account_id, args.role_id, args.client_name, args.token)
    print(json.dumps(resp))


if args.sub_parser == "get-token-client-key":
    resp = core_utils.get_token_client_key(args.account_id, args.client_key_id, args.client_key_secret)
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
        policiesJson,
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
    roles = core_utils.get_roles(
        args.account_id,
        args.token,
    )

    print(json.dumps(roles))

if args.sub_parser == "add-user":
    resp = core_utils.create_user(
        args.account_id,
        args.email,
        args.token,
        tags=args.tags,
    )

    print(json.dumps(resp))
