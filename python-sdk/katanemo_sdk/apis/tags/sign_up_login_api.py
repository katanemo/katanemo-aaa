# coding: utf-8

"""
    Katanemo - identity, and fine-grained authorization for modern { API-first } software companies.

    With Katanemo developers can add support for users, enterprise SSO, machine keys and fine-grained authorization in minutes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@katanemo.com
    Generated by: https://openapi-generator.tech
"""

from katanemo_sdk.paths.confirm_user_confirmation_code.get import ConfirmUser
from katanemo_sdk.paths.set_password_service_id.get import GetPasswordPolicy
from katanemo_sdk.paths.login_service_id.post import Login
from katanemo_sdk.paths.login_init_service_id.post import LoginInit
from katanemo_sdk.paths.sign_up_service_id.post import ServiceSignup
from katanemo_sdk.paths.set_password_service_id.post import SetPassword


class SignUpLoginApi(
    ConfirmUser,
    GetPasswordPolicy,
    Login,
    LoginInit,
    ServiceSignup,
    SetPassword,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
