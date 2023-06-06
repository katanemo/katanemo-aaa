import typing_extensions

from katanemo_sdk.paths import PathValues
from katanemo_sdk.apis.paths.service import Service
from katanemo_sdk.apis.paths.service_3x_a import Service3xA
from katanemo_sdk.apis.paths.service_service_id import ServiceServiceId
from katanemo_sdk.apis.paths.service_service_id_tags import ServiceServiceIdTags
from katanemo_sdk.apis.paths.service_service_id__well_known_jwks_json import ServiceServiceIdWellKnownJwksJson
from katanemo_sdk.apis.paths.sign_up_service_id import SignUpServiceId
from katanemo_sdk.apis.paths.confirm_user_confirmation_code import ConfirmUserConfirmationCode
from katanemo_sdk.apis.paths.set_password_service_id import SetPasswordServiceId
from katanemo_sdk.apis.paths.login_init_service_id import LoginInitServiceId
from katanemo_sdk.apis.paths.login_service_id import LoginServiceId
from katanemo_sdk.apis.paths.assignrole import Assignrole
from katanemo_sdk.apis.paths.assume_role import AssumeRole
from katanemo_sdk.apis.paths.org import Org
from katanemo_sdk.apis.paths.org_account_id import OrgAccountId
from katanemo_sdk.apis.paths.org_account_id_verify import OrgAccountIdVerify
from katanemo_sdk.apis.paths.org_account_id_user import OrgAccountIdUser
from katanemo_sdk.apis.paths.org_account_id_user_user_id import OrgAccountIdUserUserId
from katanemo_sdk.apis.paths.org_account_id_role import OrgAccountIdRole
from katanemo_sdk.apis.paths.org_account_id_role_role_id import OrgAccountIdRoleRoleId
from katanemo_sdk.apis.paths.org_account_id_keys import OrgAccountIdKeys
from katanemo_sdk.apis.paths.org_account_id_key_key_id import OrgAccountIdKeyKeyId
from katanemo_sdk.apis.paths.token import Token
from katanemo_sdk.apis.paths.oauth_token import OauthToken
from katanemo_sdk.apis.paths.authorize import Authorize
from katanemo_sdk.apis.paths.org_account_id_sso_connections_oidc import OrgAccountIdSsoConnectionsOidc
from katanemo_sdk.apis.paths.org_account_id_sso_connections_oidc_connection_id import OrgAccountIdSsoConnectionsOidcConnectionId
from katanemo_sdk.apis.paths.org_account_id_sso_connections_oidc_connection_id_login_trigger import OrgAccountIdSsoConnectionsOidcConnectionIdLoginTrigger
from katanemo_sdk.apis.paths.org_account_id_sso_connections_oidc_connection_id_sso_callback import OrgAccountIdSsoConnectionsOidcConnectionIdSsoCallback
from katanemo_sdk.apis.paths.org_account_id_sso_connections_saml import OrgAccountIdSsoConnectionsSaml
from katanemo_sdk.apis.paths.org_account_id_sso_connections_saml_connection_id import OrgAccountIdSsoConnectionsSamlConnectionId
from katanemo_sdk.apis.paths.org_account_id_sso_connections_saml_connection_id_map_attribute_to_roles import OrgAccountIdSsoConnectionsSamlConnectionIdMapAttributeToRoles
from katanemo_sdk.apis.paths.org_account_id_sso_connections_saml_connection_id_login_trigger import OrgAccountIdSsoConnectionsSamlConnectionIdLoginTrigger
from katanemo_sdk.apis.paths.org_account_id_sso_connections_saml_connection_id_sso_callback_saml_acs import OrgAccountIdSsoConnectionsSamlConnectionIdSsoCallbackSamlAcs
from katanemo_sdk.apis.paths.arc_service_id_role import ArcServiceIdRole
from katanemo_sdk.apis.paths.arc_service_id_tags import ArcServiceIdTags
from katanemo_sdk.apis.paths.arc_service_id_init import ArcServiceIdInit
from katanemo_sdk.apis.paths.arc_authorize import ArcAuthorize
from katanemo_sdk.apis.paths.healthz import Healthz
from katanemo_sdk.apis.paths.audit_logs_service_service_id_account_account_id import AuditLogsServiceServiceIdAccountAccountId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SERVICE: Service,
        PathValues.SERVICE_3X_A: Service3xA,
        PathValues.SERVICE_SERVICE_ID: ServiceServiceId,
        PathValues.SERVICE_SERVICE_ID_TAGS: ServiceServiceIdTags,
        PathValues.SERVICE_SERVICE_ID__WELLKNOWN_JWKS_JSON: ServiceServiceIdWellKnownJwksJson,
        PathValues.SIGNUP_SERVICE_ID: SignUpServiceId,
        PathValues.CONFIRM_USER_CONFIRMATION_CODE: ConfirmUserConfirmationCode,
        PathValues.SETPASSWORD_SERVICE_ID: SetPasswordServiceId,
        PathValues.LOGININIT_SERVICE_ID: LoginInitServiceId,
        PathValues.LOGIN_SERVICE_ID: LoginServiceId,
        PathValues.ASSIGNROLE: Assignrole,
        PathValues.ASSUME_ROLE: AssumeRole,
        PathValues.ORG: Org,
        PathValues.ORG_ACCOUNT_ID: OrgAccountId,
        PathValues.ORG_ACCOUNT_ID_VERIFY: OrgAccountIdVerify,
        PathValues.ORG_ACCOUNT_ID_USER: OrgAccountIdUser,
        PathValues.ORG_ACCOUNT_ID_USER_USER_ID: OrgAccountIdUserUserId,
        PathValues.ORG_ACCOUNT_ID_ROLE: OrgAccountIdRole,
        PathValues.ORG_ACCOUNT_ID_ROLE_ROLE_ID: OrgAccountIdRoleRoleId,
        PathValues.ORG_ACCOUNT_ID_KEYS: OrgAccountIdKeys,
        PathValues.ORG_ACCOUNT_ID_KEY_KEY_ID: OrgAccountIdKeyKeyId,
        PathValues.TOKEN: Token,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.AUTHORIZE: Authorize,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC: OrgAccountIdSsoConnectionsOidc,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC_CONNECTION_ID: OrgAccountIdSsoConnectionsOidcConnectionId,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC_CONNECTION_ID_LOGINTRIGGER: OrgAccountIdSsoConnectionsOidcConnectionIdLoginTrigger,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC_CONNECTION_ID_SSOCALLBACK: OrgAccountIdSsoConnectionsOidcConnectionIdSsoCallback,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML: OrgAccountIdSsoConnectionsSaml,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID: OrgAccountIdSsoConnectionsSamlConnectionId,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID_MAP_ATTRIBUTE_TO_ROLES: OrgAccountIdSsoConnectionsSamlConnectionIdMapAttributeToRoles,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID_LOGINTRIGGER: OrgAccountIdSsoConnectionsSamlConnectionIdLoginTrigger,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID_SSOCALLBACK_SAML_ACS: OrgAccountIdSsoConnectionsSamlConnectionIdSsoCallbackSamlAcs,
        PathValues.ARC_SERVICE_ID_ROLE: ArcServiceIdRole,
        PathValues.ARC_SERVICE_ID_TAGS: ArcServiceIdTags,
        PathValues.ARC_SERVICE_ID_INIT: ArcServiceIdInit,
        PathValues.ARC_AUTHORIZE: ArcAuthorize,
        PathValues.HEALTHZ: Healthz,
        PathValues.AUDITLOGS_SERVICE_SERVICE_ID_ACCOUNT_ACCOUNT_ID: AuditLogsServiceServiceIdAccountAccountId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SERVICE: Service,
        PathValues.SERVICE_3X_A: Service3xA,
        PathValues.SERVICE_SERVICE_ID: ServiceServiceId,
        PathValues.SERVICE_SERVICE_ID_TAGS: ServiceServiceIdTags,
        PathValues.SERVICE_SERVICE_ID__WELLKNOWN_JWKS_JSON: ServiceServiceIdWellKnownJwksJson,
        PathValues.SIGNUP_SERVICE_ID: SignUpServiceId,
        PathValues.CONFIRM_USER_CONFIRMATION_CODE: ConfirmUserConfirmationCode,
        PathValues.SETPASSWORD_SERVICE_ID: SetPasswordServiceId,
        PathValues.LOGININIT_SERVICE_ID: LoginInitServiceId,
        PathValues.LOGIN_SERVICE_ID: LoginServiceId,
        PathValues.ASSIGNROLE: Assignrole,
        PathValues.ASSUME_ROLE: AssumeRole,
        PathValues.ORG: Org,
        PathValues.ORG_ACCOUNT_ID: OrgAccountId,
        PathValues.ORG_ACCOUNT_ID_VERIFY: OrgAccountIdVerify,
        PathValues.ORG_ACCOUNT_ID_USER: OrgAccountIdUser,
        PathValues.ORG_ACCOUNT_ID_USER_USER_ID: OrgAccountIdUserUserId,
        PathValues.ORG_ACCOUNT_ID_ROLE: OrgAccountIdRole,
        PathValues.ORG_ACCOUNT_ID_ROLE_ROLE_ID: OrgAccountIdRoleRoleId,
        PathValues.ORG_ACCOUNT_ID_KEYS: OrgAccountIdKeys,
        PathValues.ORG_ACCOUNT_ID_KEY_KEY_ID: OrgAccountIdKeyKeyId,
        PathValues.TOKEN: Token,
        PathValues.OAUTH_TOKEN: OauthToken,
        PathValues.AUTHORIZE: Authorize,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC: OrgAccountIdSsoConnectionsOidc,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC_CONNECTION_ID: OrgAccountIdSsoConnectionsOidcConnectionId,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC_CONNECTION_ID_LOGINTRIGGER: OrgAccountIdSsoConnectionsOidcConnectionIdLoginTrigger,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_OIDC_CONNECTION_ID_SSOCALLBACK: OrgAccountIdSsoConnectionsOidcConnectionIdSsoCallback,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML: OrgAccountIdSsoConnectionsSaml,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID: OrgAccountIdSsoConnectionsSamlConnectionId,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID_MAP_ATTRIBUTE_TO_ROLES: OrgAccountIdSsoConnectionsSamlConnectionIdMapAttributeToRoles,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID_LOGINTRIGGER: OrgAccountIdSsoConnectionsSamlConnectionIdLoginTrigger,
        PathValues.ORG_ACCOUNT_ID_SSOCONNECTIONS_SAML_CONNECTION_ID_SSOCALLBACK_SAML_ACS: OrgAccountIdSsoConnectionsSamlConnectionIdSsoCallbackSamlAcs,
        PathValues.ARC_SERVICE_ID_ROLE: ArcServiceIdRole,
        PathValues.ARC_SERVICE_ID_TAGS: ArcServiceIdTags,
        PathValues.ARC_SERVICE_ID_INIT: ArcServiceIdInit,
        PathValues.ARC_AUTHORIZE: ArcAuthorize,
        PathValues.HEALTHZ: Healthz,
        PathValues.AUDITLOGS_SERVICE_SERVICE_ID_ACCOUNT_ACCOUNT_ID: AuditLogsServiceServiceIdAccountAccountId,
    }
)
