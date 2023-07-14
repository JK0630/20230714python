import random
import time

class Person:
    def __init__(self, id='a0000', age=20,user1=0,user2=0,user3=0):
        self.id = id
        self.age = age
        self.use1 = user1
        self.use2 = user2
        self.use3 = user3

    def golf(self):
        self.use1 += 1

    def run(self):
        self.use2 += 1

    def swim(self):
        self.use3 += 1

people = []
for i in range(100):
    # 10살부터 100살까지 랜덤한 나이 설정
    age = random.randint(10, 100)
    if age < 20:
        # 나이가 20살 미만인 경우 id는 'a'로 시작하고 4자리 숫자로 표현
        id = 'a' + str(i+1).zfill(4)
    else:
        # 나이가 20살 이상인 경우 id는 's'로 시작하고 4자리 숫자로 표현
        id = 's' + str(i+1).zfill(4)
    person = Person(id, age)
    people.append(person)

def sports_facility():
    facility_usage = []
    for person in people:
        # True 또는 False 중 랜덤하게 선택하여 스포츠 시설 참가 여부 결정
        if random.choice([True, False]):
            # golf, run, swim 중에서 랜덤하게 선택하여 운동 종류 결정
            sport = random.choice(['golf', 'run', 'swim'])
            if sport == 'golf':
                # golf 이용 횟수 증가
                person.golf()
            elif sport == 'run':
                # run 이용 횟수 증가
                person.run()
            elif sport == 'swim':
                # swim 이용 횟수 증가
                person.swim()
            # 이용 중인 고객 리스트에 추가
            facility_usage.append(person)
    return facility_usage

def save_current_usage(usage_list):
    # 현재 이용 현황을 txt 파일로 저장
    with open('current_usage.txt', 'w',encoding='utf-8') as file:
        for i, person in enumerate(usage_list):
            # 번호와 이용자 수를 포함한 형식으로 저장
            line = f"{i+1} [이용자수 {len(usage_list)}]\n"
            file.write(line)

while True:
    # 1초마다 스포츠 시설 이용 현황을 업데이트하고 반환
    current_usage = sports_facility()
    # 이용 중인 고객 수 출력
    print(f"[이용자수: {len(current_usage)}] {'고객 적음' if len(current_usage) <= 50 else '고객 많음'}")
    # 현재 이용 현황을 txt 파일로 저장
    save_current_usage(current_usage)
    # 1초 대기
    time.sleep(1)
    print(people)
