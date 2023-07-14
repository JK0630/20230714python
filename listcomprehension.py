data = [i for i in range(1, 100, 2)]
print(data)


data = list(map(lambda x: float(x + 10), data))
print(data)

lotto = [i for i in range(1, 46)]
print(lotto)

import random

random.shuffle(lotto)
result = lotto[:6]
print(result)

result2 = {str(i):i for i in range(1,5)}
print(result2)

result3 = {i for i in range(1,5)}
print(result3)