from datetime import datetime
from app.db import get_db


def serialize_framework(f):
    return {
        "id": str(f["_id"]),
        "name": f["name"],
        "code": f["code"],
        "version": f.get("version"),
        "description": f.get("description"),
        "createdAt": f["createdAt"],
    }


async def create_framework(data: dict):
    db = get_db()

    framework = {
        "name": data["name"],
        "code": data["code"],
        "version": data.get("version"),
        "description": data.get("description"),
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }

    result = await db.frameworks.insert_one(framework)

    created = await db.frameworks.find_one({"_id": result.inserted_id})

    return serialize_framework(created)


async def list_frameworks():
    db = get_db()

    frameworks = []
    cursor = db.frameworks.find()

    async for f in cursor:
        frameworks.append(serialize_framework(f))

    return frameworks