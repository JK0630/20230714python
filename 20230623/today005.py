
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 60
        self.health = 5

    def run(self):
        print(f"[체중: {self.weight}][건강상태: {self.health}] run")
        self.weight -= 1
        self.health -= 1
        self.check_health()

    def golf(self):
        print(f"[체중: {self.weight}][건강상태: {self.health}] golf")
        self.weight -= 2
        self.health -= 2
        self.check_health()

    def swim(self):
        print(f"[체중: {self.weight}][건강상태: {self.health}] swim")
        self.weight -= 2
        self.health -= 1
        self.check_health()

    def eat(self):
        print(f"[체중: {self.weight}][건강상태: {self.health}] eat")
        self.weight += 2
        self.health += 1
        self.check_health()

    def rest(self):
        print(f"[체중: {self.weight}][건강상태: {self.health}] rest")
        self.weight += 1
        self.health += 1
        self.check_health()

    def check_health(self):
        if self.health <= 0:
            print("건강이 나빠져 프로그램을 종료합니다.")
            exit()

        if self.weight < 40:
            self.weight = 40
        elif self.weight > 100:
            self.weight = 100


person = Person("John", 30)

while True:
    choice = input("1: run, 2: golf, 3: swim, 4: eat, 5: break - 종료하려면 0을 입력하세요: ")

    if choice == "0":
        break
    elif choice == "1":
        person.run()
    elif choice == "2":
        person.golf()
    elif choice == "3":
        person.swim()
    elif choice == "4":
        person.eat()
    elif choice == "5":
        person.rest()

