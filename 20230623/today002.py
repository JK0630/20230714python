import random
import matplotlib.pyplot as plt


vocabulary = {}

with open("mynote.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        number, word, meaning = line.strip().split(", ")
        vocabulary[number] = {"word": word, "meaning": meaning}

score = 0
correct_answers = 0
wrong_answers = 0
selected_numbers = []
answer_results = []

while True:
    if len(selected_numbers) == len(vocabulary):
        print("모든 영단어를 다 학습하였습니다.")
        break

    available_numbers = [number for number in vocabulary.keys() if number not in selected_numbers]
    number = random.choice(available_numbers)

    selected_numbers.append(number)

    word = vocabulary[number]["word"]
    meaning = vocabulary[number]["meaning"]

    answer = input(f"{word}의 뜻은 무엇인가요? (종료하려면 0을 입력하세요): ")
    if answer == "0":
        
        break

    if answer == meaning:
        print("정답입니다!")
        score += 20
        correct_answers += 1
        answer_results.append(1) 
    else:
        print(f"오답입니다. 정답은 '{meaning}'입니다.")
        score -= 10
        wrong_answers += 1
        answer_results.append(0)
    if score < 0:
        score = 0

    print(f"[점수: {score}][정답수: {correct_answers}][오답수: {wrong_answers}]\n")


words = list(vocabulary.values())
x = range(1, len(words) + 1)
y = answer_results

fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.set_xticks(x)
ax.set_xticklabels([word["word"] for word in words], rotation=45, ha='right')
ax.set_xlabel("영단어")
ax.set_ylabel("정답 여부 (정답: 1, 오답: 0)")
ax.set_title("각 단어별 정답 및 오답 점수")
plt.show()

