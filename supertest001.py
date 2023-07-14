class A():
    def __init__(self):
        print('A start')
        super().__init__()
        print('A end')
    def test(self):
        print('A')

class B():
    def __init__(self):
        print('B start')
        super().__init__()
        print('B end')
    def test(self):
        print('B') 

class C():
    def __init__(self):
        print('C start')
        super().__init__()
        print('C end')
    def test(self):
        print('C')

class D(C, B, A):
    def __init__(self):
        print('D start')
        super().__init__()
        # super().test() # C
        # super(B, self).test() # A
        # B.test(self) # B --> self 인자 있음
        print('D end')

result = D()

print(D.__mro__) # D C B H A object