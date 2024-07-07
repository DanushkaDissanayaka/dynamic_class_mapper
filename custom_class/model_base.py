from .type import Type

class ModelBase:

    def __init__(self, payload):
          # Iterate over all annotated class attributes
        for key, _class in self.__annotations__.items():

            # Initialize default variables
            _attr_key_in_payload = key
            _attr_mapper = None

            # Check if the current attribute is an instance of Type
            if hasattr(self, key) and type(self.__getattribute__(key)) is Type:
                attr: Type = self.__getattribute__(key)

                # Use the alias if it is set
                if attr.alias:
                    _attr_key_in_payload = attr.alias
                
                # Set the default factory if it is callable
                if attr.default_factory and callable(attr.default_factory):
                    _attr_mapper = attr.default_factory

            # Try to set the attribute from the payload
            try:
                if _attr_key_in_payload in payload:
                    # Check if the attribute is a List and process accordingly
                    if vars(_class).get('_name') == 'List' and len(vars(_class).get('__args__')):
                        # Map each element in the list to the appropriate class
                        _list = [vars(_class).get('__args__')[0](e) for e in payload[_attr_key_in_payload]]
                        self.__setattr__(key, _list)
                    else:
                        # Directly set the attribute
                        self.__setattr__(key, _class(payload[_attr_key_in_payload]))

                    # Apply the default factory if available
                    if _attr_mapper:
                        self.__setattr__(key, _attr_mapper(self.__getattribute__(key)))
                else:
                    # Set attribute to None if not in payload
                    self.__setattr__(key, None)
            except Exception as e:
                # Print error message and set attribute to None in case of failure
                print(f"Error setting attribute {key}: {e}")
                self.__setattr__(key, None)