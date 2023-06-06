# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from katanemo_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SERVICE = "service"
    SIGNUP_LOGIN = "sign-up/login"
    ACCESSCONTROL = "access-control"
    ORGANIZATION = "organization"
    IDENTITY = "identity"
    ACCESSLOGS = "access-logs"
    SSO = "sso"
    ARC = "arc"
    HEALTH = "health"
    DEFAULT = "default"
