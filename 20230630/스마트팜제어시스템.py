import threading
import random
import time

class SensorThread(threading.Thread):
    def __init__(self, sensor_type, interval):
        threading.Thread.__init__(self)
        self.sensor_type = sensor_type
        self.interval = interval
        self.value = 0
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            if self.sensor_type == "Temperature":
                self.value = random.randint(1, 50)  # 온도 범위 변경
            elif self.sensor_type == "Humidity":
                self.value = random.randint(1, 100)  # 습도 범위 변경
            print(f"{self.sensor_type}: {self.value}")
            time.sleep(self.interval)

    def stop(self):
        self.running = False

class ControlThread(threading.Thread):
    def __init__(self, temperature_thread, humidity_thread):
        threading.Thread.__init__(self)
        self.temperature_thread = temperature_thread
        self.humidity_thread = humidity_thread

    def run(self):
        while True:
            temperature = self.temperature_thread.value
            humidity = self.humidity_thread.value

            if temperature < 20:
                print("Temperature too low. Turning on the heater.")
                while temperature < 20:
                    temperature += 1
                    self.temperature_thread.value = temperature
                    time.sleep(1)

            if temperature >= 25:
                print("Temperature too high. Turning on the air conditioner.")
                while temperature >= 25:
                    temperature -= 1
                    self.temperature_thread.value = temperature
                    time.sleep(1)

            if humidity < 40:
                print("Humidity too low. Turning on the humidifier.")
                while humidity < 40:
                    humidity += 1
                    self.humidity_thread.value = humidity
                    time.sleep(1)

            if humidity >= 60:
                print("Humidity too high. Turning on the dehumidifier.")
                while humidity >= 60:
                    humidity -= 1
                    self.humidity_thread.value = humidity
                    time.sleep(1)

            time.sleep(1)

# 온도값을 수집하는 쓰레드 생성
temperature_thread = SensorThread("Temperature", 10)
# 습도값을 수집하는 쓰레드 생성
humidity_thread = SensorThread("Humidity", 10)

# 메인 쓰레드에서 제어 작업 수행하는 쓰레드 생성
control_thread = ControlThread(temperature_thread, humidity_thread)

# 각 쓰레드 시작
temperature_thread.start()
humidity_thread.start()
control_thread.start()

# 프로그램 실행 중지할 때까지 대기
time.sleep(60)

# 각 쓰레드 종료
temperature_thread.stop()
humidity_thread.stop()
control_thread.join()
