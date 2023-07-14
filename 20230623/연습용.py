import random
import matplotlib.pyplot as plt

# 영단어와 뜻을 저장할 파일 이름
filename = "mynote.txt"

# 영단어와 뜻을 저장할 딕셔너리
vocabulary = {}

# 파일에서 영단어와 뜻 읽어오기
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        number, word, meaning = line.strip().split(", ")
        vocabulary[number] = {"word": word, "meaning": meaning}

# 퀴즈 점수와 정답 수, 오답 수 초기화
score = 0
correct_answers = 0
wrong_answers = 0

while True:
    # 랜덤한 번호 선택
    number = str(random.randint(1, 30))

    # 선택된 번호에 해당하는 영단어와 뜻 가져오기
    word = vocabulary[number]["word"]
    meaning = vocabulary[number]["meaning"]

    # 영단어 뜻 맞추기
    answer = input(f"{word}의 뜻은 무엇인가요? (종료하려면 0을 입력하세요): ")
    if answer == "0":
        break

    if answer == meaning:
        print("정답입니다!")
        score += 20
        correct_answers += 1
    else:
        print(f"오답입니다. 정답은 '{meaning}'입니다.")
        score -= 10
        wrong_answers += 1
    if score < 0:
        score = 0

    print(f"[점수: {score}][정답수: {correct_answers}][오답수: {wrong_answers}]\n")

# 영단어별 점수 막대그래프로 표현
words = list(vocabulary.values())
word_scores = [score for score in range(0, score + 1, 20)]
x = range(len(words))
plt.bar(x, word_scores)
plt.xlabel("영단어")
plt.ylabel("점수")
plt.xticks(x, [word["word"] for word in words], rotation=45)
plt.title("영단어별 점수")
plt.show()
