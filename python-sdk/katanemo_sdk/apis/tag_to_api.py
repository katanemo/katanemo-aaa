import typing_extensions

from katanemo_sdk.apis.tags import TagValues
from katanemo_sdk.apis.tags.service_api import ServiceApi
from katanemo_sdk.apis.tags.sign_up_login_api import SignUpLoginApi
from katanemo_sdk.apis.tags.access_control_api import AccessControlApi
from katanemo_sdk.apis.tags.organization_api import OrganizationApi
from katanemo_sdk.apis.tags.identity_api import IdentityApi
from katanemo_sdk.apis.tags.access_logs_api import AccessLogsApi
from katanemo_sdk.apis.tags.sso_api import SsoApi
from katanemo_sdk.apis.tags.arc_api import ArcApi
from katanemo_sdk.apis.tags.health_api import HealthApi
from katanemo_sdk.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SERVICE: ServiceApi,
        TagValues.SIGNUP_LOGIN: SignUpLoginApi,
        TagValues.ACCESSCONTROL: AccessControlApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.IDENTITY: IdentityApi,
        TagValues.ACCESSLOGS: AccessLogsApi,
        TagValues.SSO: SsoApi,
        TagValues.ARC: ArcApi,
        TagValues.HEALTH: HealthApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SERVICE: ServiceApi,
        TagValues.SIGNUP_LOGIN: SignUpLoginApi,
        TagValues.ACCESSCONTROL: AccessControlApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.IDENTITY: IdentityApi,
        TagValues.ACCESSLOGS: AccessLogsApi,
        TagValues.SSO: SsoApi,
        TagValues.ARC: ArcApi,
        TagValues.HEALTH: HealthApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
