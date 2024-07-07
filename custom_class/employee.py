from typing import List
from .department import Department
from .type import Type
from .model_base import ModelBase
from .path_mapper import PathMapper


class Employee(ModelBase):
    id:str = Type(alias='t_id')
    name:str
    age:int
    title:str
    department:List[Department]
    image:str = Type(alias='_image', default_factory = PathMapper('image/employee').to_url)
