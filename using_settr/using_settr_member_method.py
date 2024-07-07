class Employe:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


def map_with_setattr(list_employees):
    employees_list = [Employe(e) for e in list_employees]
    return employees_list