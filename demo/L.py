class A:
    y = 5

    def __init__(self, x, y):
        x = x
        self.y = y

    def func(self, y):
        def child(z):
            return y * self.x * z

        return child


if __name__ == '__main__':
    a = A(1, 2)
    A.x = 20
    A.y = 30
    print(a.func(1)(2))
