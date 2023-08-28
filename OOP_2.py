class B:

    def method_1(self):
        print('method_1_class_B')

    def method_2(self):
        self.method_1()


class C(B):

    def method_1(self):
        print('method_1_class_C')


c = C()
c.method_2()
