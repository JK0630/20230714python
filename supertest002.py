class A():
    pass

class B(A):
    def __init__(self) :
        self.test= 'a'
    pass

class C(A):

    pass
class D(A):
    pass

class E(D, C, B):
    def __init__(self) :
        self.test2= 'a'
        pass

print(E.mro())
print(E().test2)