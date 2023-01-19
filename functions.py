import hashlib
from email_validate import email_validate


def hash_password(password):
    hash_object = hashlib.md5(b"{password}")
    return hash_object.hexdigest()


def is_email(email):

    return email_validate.validate(email)


