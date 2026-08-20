from datetime import timedelta

import pytest
from fastapi import HTTPException
from jose import jwt
from utils import *

from todoapp.routers.auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_db,
)

app.dependency_overrides[get_db] = override_get_db


def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    authenticated_user = authenticate_user(test_user.username, "testpassword", db)
    assert authenticated_user is not None
    assert authenticated_user.username == test_user.username

    non_existent_user = authenticate_user("WrongUserName", "testpassword", db)
    assert non_existent_user is False

    wrong_password_user = authenticate_user(test_user.username, "wrongpassword", db)
    assert wrong_password_user is False


def test_create_access_token():
    username = "testuser"
    user_id = 1
    role = "user"
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)

    decoded_token = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
        options={"verify_signature": False},
    )

    assert decoded_token["sub"] == username
    assert decoded_token["id"] == user_id
    assert decoded_token["role"] == role


@pytest.mark.asyncio
async def test_get_current_user_valid_token(monkeypatch):
    monkeypatch.setattr("todoapp.routers.auth.SECRET_KEY", settings.SECRET_KEY)
    monkeypatch.setattr("todoapp.routers.auth.ALGORITHM", settings.ALGORITHM)
    encode = {"sub": "testuser", "id": 1, "role": "admin"}
    token = jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    user = await get_current_user(token=token)
    assert user == {"username": "testuser", "id": 1, "user_role": "admin"}


@pytest.mark.asyncio
async def test_get_current_user_missing_payload(monkeypatch):
    monkeypatch.setattr("todoapp.routers.auth.SECRET_KEY", settings.SECRET_KEY)
    monkeypatch.setattr("todoapp.routers.auth.ALGORITHM", settings.ALGORITHM)
    encode = {"role": "user"}
    token = jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Could not validate user."
