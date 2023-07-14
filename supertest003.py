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
        # super().__init__(30, ‘a’) # C클래스만 초기화된다
        # 각 부모클래스의 초기화가 필요한 경우
        # C.__init__(self, 30, ‘a’) # 또는 super(D, self).__init(30, ‘a’)
        # B.__init__(self, ‘b’) # 또는 super(C, self).__init(‘b’)
        # A.__init__(self, 5) # 또는 super(B, self).__init(5)
        print('D end')

result = D()
result.test()

print(D.__mro__) # D C B H A object


