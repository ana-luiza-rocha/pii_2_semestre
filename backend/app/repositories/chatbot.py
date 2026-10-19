from datetime import datetime, timezone

from app.database.database import db


STEP_ALIASES = {
    "AM_01": "AM_1",
    "MI_1": "MI_01",
    "AM_CC_1": "AM_CC_01",
    "AM_OFM_1": "AM_OFM_01",
}

INPUT_STEPS = {
    "FB_ES_01": ("comment", "suggestion"),
    "FB_FR_01": ("comment", "complaint"),
    "FB_EE_01": ("comment", "compliment"),
    "AM_CC_07": ("score", "evaluation"),
    "AM_OFM_07": ("score", "evaluation"),
    "MI_CC_16": ("score", "evaluation"),
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

    input_type, feedback_type = INPUT_STEPS.get(code, (None, None))
    result["input_type"] = input_type
    result["feedback_type"] = feedback_type
    return result


def save_answer(submission_id, answer):
    answer["created_at"] = datetime.now(timezone.utc)
    db.rating.update_one(
        {"_id": str(submission_id)},
        {"$setOnInsert": answer},
        upsert=True,
    )
