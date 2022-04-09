from passlib.context import CryptContext

hashed = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

def hashed_password(password : str) -> str:
    return hashed.hash(password)