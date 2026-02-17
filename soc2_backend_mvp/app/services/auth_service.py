from datetime import datetime, timezone

from ..db import get_db
from ..utils.password import hash_password, verify_password
from ..utils.jwt import create_access_token
from ..utils.errors import bad_request, unauthorized


async def register_user(email: str, password: str):
    db = get_db()

    existing = await db.users.find_one({"email": email.lower()})
    if existing:
        bad_request("Email already registered")

    now = datetime.now(timezone.utc)
    doc = {
        "email": email.lower(),
        "passwordHash": hash_password(password),
        "createdAt": now,
    }

    res = await db.users.insert_one(doc)
    user_id = str(res.inserted_id)

    token = create_access_token(subject=user_id)
    return {
        "accessToken": token,
        "user": {
            "id": user_id,
            "email": doc["email"],
            "createdAt": doc["createdAt"],
        },
    }


async def login_user(email: str, password: str):
    db = get_db()

    user = await db.users.find_one({"email": email.lower()})
    if not user:
        unauthorized("Invalid credentials")

    if not verify_password(password, user["passwordHash"]):
        unauthorized("Invalid credentials")

    user_id = str(user["_id"])
    token = create_access_token(subject=user_id)

    return {
        "accessToken": token,
        "user": {
            "id": user_id,
            "email": user["email"],
            "createdAt": user["createdAt"],
        },
    }
