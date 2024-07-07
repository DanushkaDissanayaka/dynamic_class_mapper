from .employee import Employee

def map_with_custom_class(list_employees):
    employees_list = [Employee(e) for e in list_employees]
    return employees_list
