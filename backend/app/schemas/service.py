from pydantic import BaseModel, Field, ConfigDict
from app.core.object_id import PyObjectId

class Service (BaseModel):

    model_config = ConfigDict(
        populate_by_name=True
    )

    id: PyObjectId = Field(alias="_id")
    code: str
    name: str
    initial_step: str