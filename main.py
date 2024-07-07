import random
import perfplot
import json
from faker import Faker

from custom_class.cutom_class_method import  map_with_custom_class
from named_tuple.named_tuple import map_with_named_tuple
from using_settr.using_settr_member_method import map_with_setattr
from with_pydantic_package.pydantic_method import map_with_paydantic

# _dictionarys = [{"t_id":"4c1b83ae-a2f7-4433-aa91-e6c3865b38e1","name":"Frants","age":27,"title":"Human Resources Assistant IV","department":[{"name":"Services","t_id":"9013297d-ba91-4e87-9484-815813515a5e"},{"name":"Human Resources","t_id":"3ae9d7dd-3133-4235-9cd8-0a6d4a362388"},{"name":"Legal","t_id":"46ddab11-a468-4447-bd95-182fd79b5cee"},{"name":"Human Resources","t_id":"54ea2295-875b-4345-a8f2-edeee55b5f48"},{"name":"Marketing","t_id":"37298cb5-c04b-4288-b4da-be3021acb0ad"}],"image":"maecenas.jpg"}]


# tupple = map_with_named_tuple(_dictionarys)
# custom = map_with_custom_class(_dictionarys)
# pydantic = map_with_paydantic(_dictionarys)
# setattr = map_with_setattr(_dictionarys)

# print(setattr[0].name)


def get_data():
    # load test data
    with open('data.json') as f:
            return json.load(f)
    

def generate_data(data_samples:int):
    fake = Faker()
    _dictionarys = []
    for i in range(0, data_samples):
        _dictionary = {"t_id":fake.uuid4(),"name":fake.name(),"age":random.randint(21, 50),"title":fake.company() ,"department":[{"name":fake.company(),"t_id":fake.uuid4()} for i in range(0, random.randint(2,6))],"image":f"{fake.first_name_male()}.jpg"}
        _dictionarys.append(_dictionary)
    

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(_dictionarys, f, ensure_ascii=False, indent=4)
        return _dictionarys

# generate_data(100000)
_dictionarys = get_data()


if __name__ == '__main__':
    out = perfplot.bench(
        setup=lambda n: _dictionarys[:n],
        kernels=[
            lambda a: map_with_custom_class(a),
            lambda a: map_with_paydantic(a),
            lambda a: map_with_named_tuple(a),
            lambda a: map_with_setattr(a)
        ],
        labels=["Custom Class", 
                "Paydantic", 
                'Named Tuple', 
                'Setattr'],
        n_range=[k for k in range(0, 105000, 5000)],
        xlabel="No of objects",
        equality_check=None
    )

    print(out.__repr__())
    out.show()