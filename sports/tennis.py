

t = 100
    
def func_t():
    print('tennis')

class c_t():
    def __init__(self):
        self.t = 100
    def __call__(self):
        print('속성 ', self.t)

if __name__ =='__main__':
    for i in range(3):
        print(i)