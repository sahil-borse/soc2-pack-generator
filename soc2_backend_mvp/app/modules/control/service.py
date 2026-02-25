from datetime import datetime
from bson import ObjectId
from app.db import get_db


def serialize_control(c):
    return {
        "id": str(c["_id"]),
        "frameworkId": c["frameworkId"],
        "controlCode": c["controlCode"],
        "title": c["title"],
        "category": c.get("category"),
        "description": c.get("description"),
        "defaultReviewFrequency": c.get("defaultReviewFrequency"),
        "createdAt": c["createdAt"],
    }


async def create_control(data: dict):
    db = get_db()

    control = {
        "frameworkId": data["frameworkId"],
        "controlCode": data["controlCode"],
        "title": data["title"],
        "category": data.get("category"),
        "description": data.get("description"),
        "defaultReviewFrequency": data.get("defaultReviewFrequency"),
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }

    result = await db.controls.insert_one(control)

    created = await db.controls.find_one({"_id": result.inserted_id})

    return serialize_control(created)


async def list_controls(framework_id: str):
    db = get_db()

    controls = []
    cursor = db.controls.find({"frameworkId": framework_id})

    async for c in cursor:
        controls.append(serialize_control(c))

    return controls