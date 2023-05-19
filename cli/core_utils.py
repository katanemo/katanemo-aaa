from base64 import urlsafe_b64encode
import hashlib
import jwt

# same as utils.GenerateDevConfirmationCode
def generate_dev_confirmation_code(email, accountId):
    h = hashlib.sha1()
    h.update(email.encode("utf-8"))
    h.update(accountId.encode("utf-8"))
    digest = h.digest()
    return urlsafe_b64encode(digest).decode("utf-8")

def get_accound_id_from_token(token):
    decoded_token = jwt.decode(
        token,
        "xxx",
        algorithms=["RS256"],
        options={"verify_signature": False},
    )

    return decoded_token["accountId"]
