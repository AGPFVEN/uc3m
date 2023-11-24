import hashlib

print(hashlib.pbkdf2_hmac('sha512', "op", "o", 1))