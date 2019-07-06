def func1(i, info):
    x = 12345
    print(locals())
    locals()["x"] = 6789
    print("x=", x)


y = 54321
func1(1, "first")
globals()["y"] = 9876
print("y=", y)


def func2(i):
    while i > 2:
        i -= 1
        yield i


g = func2(10)
x = next(g)
print('result ==', x)
x = next(g)
print('result ==', x)


def func3(start, *stop, **step):
    print('func3 start')
    print(start)
    print(stop)
    print(step)
    print('func3 end')


def func4(name, age, *args, city, number):
    print('func4 start')
    print(name)
    print(age)
    print(args)
    print(city)
    print(number)
    print('func4 end')


def func5(name, age, *, city, number):
    print('func5 start')
    print(name)
    print(age)
    print(city)
    print(number)
    print('func5 end')


range(5)
func3(5, 1, 26, 89, city='Beijing', number=8)
func4(5, 1, 26, 89, 'dad', 'guokun', city='Beijing', number=8)
func5(5, 1, city='Beijing', number=8)
