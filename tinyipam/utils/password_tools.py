#!/usr/bin/env python3
import hashlib
import random
import string

from typing import Tuple


def hash_password_with_salt(password_clear: str, password_salt: str) -> str:
    password_hashed = hashlib.sha512(password_clear.encode() + password_salt.encode()).hexdigest()

    return password_hashed


def hash_password(password_clear: str) -> Tuple[str, str]:
    password_salt = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(16))

    return hash_password_with_salt(password_clear, password_salt), password_salt
