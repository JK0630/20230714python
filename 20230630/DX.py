import random
import time

class Office:
    def __init__(self):
        self.width = 10
        self.height = 5
        self.password = "1234"
        self.entry_door = "Close"
        self.window = "Close"
        self.aircon = "Off"
        self.computer = "Off"
        self.worker = "Absent"

    def toggle_aircon(self):
        if self.aircon == "Off":
            self.aircon = "On"
        else:
            self.aircon = "Off"

    def toggle_computer(self):
        if self.computer == "Off":
            self.computer = "On"
        else:
            self.computer = "Off"
            
    def toggle_window(self):
        if self.window == "Close":
            self.window = "Open"
        else:
            self.window = "Close"

    def toggle_entry_door(self):
        if self.entry_door == "Close":
            self.entry_door = "Open"
        else:
            self.entry_door = "Close"



    def assign_worker(self, worker_name):
        self.worker = worker_name

    def random_action(self):
        actions = [
            self.toggle_aircon,
            self.toggle_computer,
            self.toggle_window,
            self.toggle_entry_door
        ]
        random_action = random.choice(actions)
        random_action()

office = Office()
office.assign_worker("김정")

while True:
    office.random_action()
    print("근무자:", office.worker)
    print("출입문:", office.entry_door)
    print("창문:", office.window)
    print("에어컨:", office.aircon)
    print("컴퓨터:", office.computer)
    print("--------------------")
    time.sleep(1)
