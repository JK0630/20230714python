class Person():
    def __init__(self,age,name) :
        self.age =age
        self.name = name

class Korean(Person):
    def __init__(self, age, name,city):
        super().__init__(age, name)
        self.city=city

class Student(Korean):
    def __init__(self, age, name, city,subject):
        super().__init__(age, name, city)
        self.subject = subject

student1  = Student(30, 'kim','Asan','Python')
student2  = Student(25, 'lee','Seoul','Java')
student3  = Student(40, 'park','Jeju','AI')

print(f'나이(age) : {student1.age}, {student2.age}, {student3.age}')
print(f'이름(name) : {student1.name}, {student2.name}, {student3.name}')
print(f'도시(city) : {student1.city}, {student2.city}, {student3.city}')
print(f'과목(subject) : {student1.subject}, {student2.subject}, {student3.subject}')


a = {}
a['age'] =50
print(a['age'])

class Student1():
    __slots__ = ("age")
    def __init__(self):
        self.age= ''
s1 = Student1()

s1.age =30
print(s1.__dir__())


class aa():
    cnt2 = 0
    def __init__(self):
        self.cnt = 0
    @classmethod
    def run(cls):
        print(id(cls))
        cls.cnt2 += 1

    def add(self):
        self.cnt += 1
    @staticmethod
    def subtract(x1,x2):
        return x1+x2
    
# a = aa()
# a = aa()
# a = aa()
# a.add()
# a.add()
# a.add()
# print(a.cnt)
# print(a.subtract(10,20))

aa.run()
print(id(aa))