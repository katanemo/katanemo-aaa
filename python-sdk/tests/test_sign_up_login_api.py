# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.initial_login_request import InitialLoginRequest  # noqa: F401
from katanemo_sdk.models.initial_login_response import InitialLoginResponse  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.login_token import LoginToken  # noqa: F401
from katanemo_sdk.models.login_with_password_request import LoginWithPasswordRequest  # noqa: F401
from katanemo_sdk.models.password_policy import PasswordPolicy  # noqa: F401
from katanemo_sdk.models.set_password_request import SetPasswordRequest  # noqa: F401
from katanemo_sdk.models.signup_request import SignupRequest  # noqa: F401
from katanemo_sdk.models.signup_response import SignupResponse  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401
from katanemo_sdk.models.user_confirmation_response import UserConfirmationResponse  # noqa: F401


def test_confirm_user(client: TestClient):
    """Test case for confirm_user

    Confirm User
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/confirmUser/{confirmationCode}".format(confirmationCode='confirmation_code_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_password_policy(client: TestClient):
    """Test case for get_password_policy

    Get password policy
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/set-password/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_login(client: TestClient):
    """Test case for login

    Login (Password)
    """
    login_with_password_request = {"skip_redirect":1,"email_address":"emailAddress","password":"password","state":"state"}

    headers = {
    }
    response = client.request(
        "POST",
        "/login/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
        json=login_with_password_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_login_init(client: TestClient):
    """Test case for login_init

    Login-init (SSO vs. Password)
    """
    initial_login_request = {"email_address":"emailAddress","state":"state"}

    headers = {
    }
    response = client.request(
        "POST",
        "/login-init/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
        json=initial_login_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_service_signup(client: TestClient):
    """Test case for service_signup

    Sign-up for Service
    """
    signup_request = {"email_address":"emailAddress"}

    headers = {
    }
    response = client.request(
        "POST",
        "/sign-up/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
        json=signup_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_set_password(client: TestClient):
    """Test case for set_password

    Set Password
    """
    set_password_request = {"email_address":"emailAddress","password":"password","session":"session"}

    headers = {
    }
    response = client.request(
        "POST",
        "/set-password/{serviceId}".format(serviceId='service_id_example'),
        headers=headers,
        json=set_password_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

