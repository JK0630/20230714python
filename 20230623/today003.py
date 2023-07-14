class Car:
    def __init__(self):
        self.dist = 0  # 이동거리
        self.fuel = 100  # 연료

    def go(self):
        if self.fuel < 15:
            print("연료가 부족하여 이동할 수 없습니다.")
            self.stop()
            return
        self.dist += 10
        self.fuel -= 15
        print(f"직진합니다.현재 이동거리{self.dist}km, 남은 연료{self.fuel}L")

    def stop(self):
        self.fuel -= 5
        print(f"멈춥니다.현재 이동거리{self.dist}km, 남은 연료{self.fuel}L")

    def left(self):
        if self.fuel < 10:
            print("연료가 부족하여 좌회전할 수 없습니다.")
            self.stop()
            return
        self.dist += 5
        self.fuel -= 10
        print(f"좌회전합니다.현재 이동거리{self.dist}km, 남은 연료{self.fuel}L")

    def right(self):
        if self.fuel < 10:
            print("연료가 부족하여 우회전할 수 없습니다.")
            self.stop()
            return
        self.dist += 5
        self.fuel -= 10
        print(f"우회전합니다.현재 이동거리{self.dist}km, 남은 연료{self.fuel}L")

    def uturn(self):
        if self.fuel < 10:
            print("연료가 부족하여 유턴할 수 없습니다.")
            self.stop()
            return
        self.dist += 5
        self.fuel -= 10
        print(f"유턴합니다.현재 이동거리{self.dist}km, 남은 연료{self.fuel}L")


car = Car()

while True:
    command = input("명령을 입력하세요 (go, stop, left, right, uturn): ")
    if command == "go":
        car.go()
    elif command == "stop":
        car.stop()
    elif command == "left":
        car.left()
    elif command == "right":
        car.right()
    elif command == "uturn":
        car.uturn()
    else:
        print("올바른 명령을 입력하세요.")
    
    if car.fuel <= 0:
        print("연료가 0이하로 소진되어 자동차가 멈춥니다.")
        print(f"{car.dist}km만큼 이동하였습니다")
        break
