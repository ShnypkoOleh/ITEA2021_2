def power(x):
    def internal(y):
        return y**x
    return internal
p=power(4)
print(p(5))