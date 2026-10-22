from datetime import datetime, timezone

from app.database.database import db


STEP_ALIASES = {
    "AM_01": "AM_1",
    "MI_1": "MI_01",
    "AM_CC_1": "AM_CC_01",
    "AM_OFM_1": "AM_OFM_01",
}

COMMENT_TYPES = {
    "FB_ES_01": "suggestion",
    "FB_FR_01": "complaint",
    "FB_EE_01": "compliment",
}


def find_step(code):
    code = STEP_ALIASES.get(code, code)
    result = db.step.find_one({"code": code}, {"_id": 0})
    if result is None:
        return None

    for option in result.get("options", []):
        target = option.get("next step")
        if target in STEP_ALIASES:
            option["next step"] = STEP_ALIASES[target]

    result["input_type"] = None
    result["feedback_type"] = None

    if code in COMMENT_TYPES:
        result["input_type"] = "comment"
        result["feedback_type"] = COMMENT_TYPES[code]
    elif code in ["AM_CC_07", "AM_OFM_04", "MI_CC_12"]:
        result["input_type"] = "score"
        result["feedback_type"] = "evaluation"
    return result


def save_answer(submission_id, answer):
    answer["created_at"] = datetime.now(timezone.utc)
    db.rating.update_one(
        {"_id": str(submission_id)},
        {"$setOnInsert": answer},
        upsert=True,
    )
