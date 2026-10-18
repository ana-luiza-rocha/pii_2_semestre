from pydantic import BaseModel, Field, ConfigDict, Path
from app.core.object_id import PyObjectId

class Option(BaseModel):
    text: str
    next_step: str

class Step (BaseModel):

    model_config = ConfigDict(
        populate_by_name=True
    )

    id: PyObjectId = Field(alias="_id")
    code: str
    service_name: str
    message: str
    video_path: Path | None = None
    website_path: Path | None = None
    options: list[Option]
