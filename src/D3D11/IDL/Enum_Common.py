class EnumField:
    def __init__(self, field_name, enum_type):
        self.field_name = field_name
        self.enum_type = enum_type
        self.private_name = f"_{field_name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.enum_type(getattr(instance, self.private_name))

    def __set__(self, instance, value):
        setattr(instance, self.private_name, int(value))
