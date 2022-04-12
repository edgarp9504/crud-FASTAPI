from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

def hashed_password(password : str) -> str:
    return pwd_context.hash(password)

def verify_password(password : str, hased_password : str) -> str:
    return pwd_context.verify(password, hased_password)