from collections import namedtuple

Employee= namedtuple('Employee', 'name, age, title, department, image, t_id')

def map_with_named_tuple(list_employees):
    employees_list = [Employee(**e) for e in list_employees]
    return employees_list
