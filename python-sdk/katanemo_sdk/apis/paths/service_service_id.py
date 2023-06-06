from katanemo_sdk.paths.service_service_id.get import ApiForget
from katanemo_sdk.paths.service_service_id.put import ApiForput
from katanemo_sdk.paths.service_service_id.delete import ApiFordelete


class ServiceServiceId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
