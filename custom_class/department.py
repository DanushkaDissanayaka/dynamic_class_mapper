from .type import Type
from .model_base import ModelBase


class Department(ModelBase):
    name:str
    id:str = Type(alias='t_id')