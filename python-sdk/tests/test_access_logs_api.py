# coding: utf-8

from fastapi.testclient import TestClient


from katanemo_sdk.models.audit_log_entry import AuditLogEntry  # noqa: F401
from katanemo_sdk.models.bad_request_exception import BadRequestException  # noqa: F401
from katanemo_sdk.models.conflict_exception import ConflictException  # noqa: F401
from katanemo_sdk.models.error import Error  # noqa: F401
from katanemo_sdk.models.internal_server_error_exception import InternalServerErrorException  # noqa: F401
from katanemo_sdk.models.too_many_requests_exception import TooManyRequestsException  # noqa: F401
from katanemo_sdk.models.unauthorized_exception import UnauthorizedException  # noqa: F401


def test_get_audit_logs(client: TestClient):
    """Test case for get_audit_logs

    List Access logs
    """
    params = [("start_time", 'start_time_example'),     ("end_time", 'end_time_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/audit-logs/service/{serviceId}/account/{accountId}".format(serviceId='service_id_example', accountId='account_id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

