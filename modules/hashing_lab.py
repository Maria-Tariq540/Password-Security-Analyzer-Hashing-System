import hashlib
import bcrypt
from argon2 import PasswordHasher

argon = PasswordHasher()


class HashingLab:

    @staticmethod
    def md5_hash(password):
        return hashlib.md5(
            password.encode()
        ).hexdigest()

    @staticmethod
    def sha256_hash(password):
        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    @staticmethod
    def sha512_hash(password):
        return hashlib.sha512(
            password.encode()
        ).hexdigest()

    @staticmethod
    def bcrypt_hash(password):
        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )
        return hashed.decode()

    @staticmethod
    def argon2_hash(password):
        return argon.hash(password)