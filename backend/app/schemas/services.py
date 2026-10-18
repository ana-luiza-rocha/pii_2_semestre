from pydantic import BaseModel

class Service (BaseModel):

    model_config = ConfigDict(
        populate_by_name=True
    )

    id: PyObjectId = Field(alias="_id")
    code: str
    name: str
    initial_step: str