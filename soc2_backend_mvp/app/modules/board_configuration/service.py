from app.db import get_db
from datetime import datetime


async def update_board_config(company_id: str, framework_id: str, columns: list):
    db = get_db()

    await db.company_board_configs.update_one(
        {
            "companyId": company_id,
            "frameworkId": framework_id
        },
        {
            "$set": {
                "columns": columns,
                "updatedAt": datetime.utcnow()
            }
        },
        upsert=True
    )

    return {"message": "Board configuration updated"}


async def get_board_config(company_id: str, framework_id: str):
    db = get_db()

    config = await db.company_board_configs.find_one({
        "companyId": company_id,
        "frameworkId": framework_id
    })

    if not config:
        # default config
        return {
            "columns": [
                {"key": "not_started", "label": "Not Started", "order": 1},
                {"key": "in_progress", "label": "In Progress", "order": 2},
                {"key": "implemented", "label": "Implemented", "order": 3}
            ]
        }

    return {"columns": config["columns"]}