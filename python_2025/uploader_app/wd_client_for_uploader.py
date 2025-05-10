# pip install requests


from pydantic import BaseModel
import requests
from typing import List
from hashlib import md5


class Token(BaseModel):
    studentid: int
    wdauth: str
    expiry_epoch_s: int


class AuthResponse(BaseModel):
    token: Token
    roles: List[str]


def authenticate(album: str, password: str) -> AuthResponse:
    url = "https://wdauth.wsi.edu.pl/authenticate"
    params = {
        "album": album,
        "pass": md5(password.encode()).hexdigest()
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return AuthResponse(**response.json())

if __name__ == '__main__':
    x = authenticate('nr_indeksu', 'hasło_plain_text')
    print(x)