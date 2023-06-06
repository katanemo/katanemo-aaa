import time
import os
import katanemo_sdk
from pprint import pprint

# Defining the host is optional and defaults to https://api.katanemo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = katanemo_sdk.Configuration(
    host = "https://api.katanemo.com"
)


# Enter a context with an instance of the API client
with katanemo_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = katanemo_sdk.ServiceApi(api_client)

    try:
        # Get Details for Katanemo AAA
        api_response = api_instance.get_default_service()
        print("The response of ServiceApi->get_default_service:\n")
        pprint(api_response.json(by_alias=True))
    except Exception as e:
        print("Exception when calling ServiceApi->get_default_service: %s\n" % e)
