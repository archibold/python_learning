def add(*args):
    return sum(args)

def calculate(x, **kw):
    n=x
    n += kw.get('add')
    n *= kw.get('multiply')
    return n


print(add(1,2))

print(add(123,7,30,40))

print(calculate(10, add=3, multiply=2))