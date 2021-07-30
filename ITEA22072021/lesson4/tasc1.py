# from python_shell import Shell
# import urllib.request


class A:
    def __setattr__(self, key, value):
        print(f"I will set {key}={value}")
        return super().__setattr__(key, value)

    def __getattribute__(self, item):
        print(f"I call {item}")
        return "Hello"

    def __delattr__(self, item):
        # Prevent deletion of attribute
        raise AttributeError("You can't delete item!")


# a = A()
# b = A()
#a.y = 1



# ....
# del a
# ...

# a.x = 100
# print(a.x)
# del a.x


def dynamic_assign():
    field_name = input("Enter field name: ")
    value = input("Enter value: ")
    obj = A()

    setattr(obj, field_name, value)
    # obj.<field_name> = value
    print(
        #obj.<field_name>
        getattr(obj, field_name)
    )

dynamic_assign()
