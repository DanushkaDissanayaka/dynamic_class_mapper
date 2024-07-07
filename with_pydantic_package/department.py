from pydantic import BaseModel, Field


class Department(BaseModel):
    name:str
    id:str = Field(alias='t_id')