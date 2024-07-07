from typing import List
from pydantic import BaseModel, Field, field_validator
from .path_mapper import PathMapper
from .department import Department


class Employee(BaseModel):
    id:str = Field(alias='t_id')
    name:str
    age:int
    title:str
    department:List[Department]
    image_url:str = Field(alias='image')

    @field_validator("image_url", mode="before")
    @classmethod
    def to_image_url(cls, raw: str) -> str:
        return PathMapper('image/employee').to_url(raw)
