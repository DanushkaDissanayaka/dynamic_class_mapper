# Custom Class Mapper For Python

When it comes to mapping dictionaries from external sources like MongoDB query results or API responses to class attributes, we often perform this task manually. However, manual mapping can be time consuming and may lead to runtime errors if the properties do not match correctly. Additionally over time this can make our codebase messy and harder to maintain.

The ModelBase class (custom_class) provides a robust and flexible way to map dictionary data to class attributes including handling nested structures and custom value formatting. By using Type for metadata, you can streamline the process of initializing complex objects from dictionaries, reducing boilerplate code and improving maintainability.

### Usage

```python
class Employee(ModelBase):
    id:str = Type(alias='t_id')
    name:str
    age:int
    title:str
    department:List[Department]
    image:str = Type(alias='_image', default_factory = PathMapper('image/employee').to_url)
```

Read more in  [blogpost](https://medium.com/@dsjayamal/python-mapping-dictionary-to-class-attributes-1a3786f05fe5)
