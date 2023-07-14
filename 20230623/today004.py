import random
import time


class AirConditioner:
    def __init__(self):
        self.temperature = 0
        self.ac_status = "Off"
        self.ac_off_duration = 0

    def update_temperature(self, temperature):
        self.temperature = temperature
        if self.temperature >= 25:
            self.ac_status = "On"
            print(f"[온도: {self.temperature}][습도: {dehumidifier.humidity}] 에어컨 On")
        elif self.temperature < 20:
            self.ac_status = "Off"
            print(f"[온도: {self.temperature}][습도: {dehumidifier.humidity}] 에어컨 Off")

    def turn_off_ac(self):
        self.ac_status = "Off"
        self.ac_off_duration += 1
        if self.ac_off_duration >= 5:
            self.temperature = random.randint(0, 30)
            self.ac_off_duration = 0
            print(f"에어컨이 {self.ac_off_duration}초간 Off 상태로 유지되어 온도를 재설정합니다: {self.temperature}")


class Dehumidifier:
    def __init__(self):
        self.humidity = 0
        self.dehumidifier_status = "Off"
        self.dehumidifier_off_duration = 0

    def update_humidity(self, humidity):
        self.humidity = humidity
        if self.humidity >= 60:
            self.dehumidifier_status = "On"
            print(f"[온도: {air_conditioner.temperature}][습도: {self.humidity}] 제습기 On")
        elif self.humidity < 40:
            self.dehumidifier_status = "Off"
            print(f"[온도: {air_conditioner.temperature}][습도: {self.humidity}] 제습기 Off")

    def turn_off_dehumidifier(self):
        self.dehumidifier_status = "Off"
        self.dehumidifier_off_duration += 1
        if self.dehumidifier_off_duration >= 5:
            self.humidity = random.randint(0, 100)
            self.dehumidifier_off_duration = 0
            print(f"제습기가 {self.dehumidifier_off_duration}초간 Off 상태로 유지되어 습도를 재설정합니다: {self.humidity}")


air_conditioner = AirConditioner()
dehumidifier = Dehumidifier()

while True:
    temperature = random.randint(0, 30)
    humidity = random.randint(0, 100)
    air_conditioner.update_temperature(temperature)
    dehumidifier.update_humidity(humidity)

    if air_conditioner.ac_status == "On":
        air_conditioner.temperature -= 1
        print(f"에어컨 동작 중... 현재 온도: {air_conditioner.temperature}")
    else:
        air_conditioner.turn_off_ac()

    if dehumidifier.dehumidifier_status == "On":
        dehumidifier.humidity -= 1
        print(f"제습기 동작 중... 현재 습도: {dehumidifier.humidity}")
    else:
        dehumidifier.turn_off_dehumidifier()

    time.sleep(1)

