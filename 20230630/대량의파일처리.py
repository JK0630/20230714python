import random
import os
import matplotlib.pyplot as plt

# 100개의 txt 파일 생성
for i in range(1, 101):
    file_name = f"{i}.txt"
    with open(file_name, "w") as file:
        numbers = [str(random.randint(1, 100)) for _ in range(10)]
        file.write(" ".join(numbers))

# 숫자 분포를 히스토그램으로 표시
histogram_data = []
for i in range(1, 101):
    file_name = f"{i}.txt"
    with open(file_name, "r") as file:
        numbers = file.read().split()
        histogram_data.extend(numbers)

plt.hist(list(map(int, histogram_data)))
plt.show()

# 숫자 30의 개수 출력
count_30 = histogram_data.count("30")
print("Number of occurrences of 30:", count_30)

# 중복된 숫자 제거 후 요소의 총 개수 출력
unique_numbers = set(histogram_data)
total_unique_count = len(unique_numbers)
print("Total count of unique elements:", total_unique_count)
