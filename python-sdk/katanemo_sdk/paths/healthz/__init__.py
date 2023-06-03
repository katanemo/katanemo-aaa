# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from katanemo_sdk.paths.healthz import Api

from katanemo_sdk.paths import PathValues

path = PathValues.HEALTHZ