from pydantic import BaseModel, Field, ConfigDict
from app.core.object_id import PyObjectId

class Rating_Type (BaseModel):
    COMPLIMENT = "compliment"
    EVALUATION = "evaluation"
    COMPLAINT = "complaint"
    SUGGESTION = "suggestion"

class Rating (BaseModel):

    model_config = ConfigDict(
        populate_by_name=True
    )

    id: PyObjectId = Field(alias="_id")
    type: Rating_Type
    comment: str
    score: int = Field(ge=1, le=5)
    chat_history: list