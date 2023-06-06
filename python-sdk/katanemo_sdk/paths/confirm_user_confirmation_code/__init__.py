# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from katanemo_sdk.paths.confirm_user_confirmation_code import Api

from katanemo_sdk.paths import PathValues

path = PathValues.CONFIRM_USER_CONFIRMATION_CODE