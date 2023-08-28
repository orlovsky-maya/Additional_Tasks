class B:
    def __init__(self, x):
        self.x = 10

    def p(self):
        print("B p")
        print(self.x)


class C(B):
    def __init__(self, y, x):
        super().__init__(x)
        self.y = y

    def p(self):
        print("C p")
        s = super()
        print(s.p())


c = C(5)
b = super(c)
print(c.x)
