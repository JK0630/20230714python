# 181

apart = [['101호','102호'],['201호','202호'],['301호','302호']]

print(apart)

# 182

stock = [['시가',100,200,300],['종가',80,210,330]]

print(stock)

# 183

stock = {'시가':[100,200,300],'종가':[80,210,330]}

print(stock)

# 184

stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}

# 185

apart = [[101,102],[201,202],[301,302]]
for row in apart:
    for col in row:
        print(col,'호')

# 186

apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart[::-1]:
    for col in row:
        print(col,'호')

# 187


apart = [ [101, 102], [201, 202], [301, 302] ]

for row in apart[::-1]:
    for col in row[::-1]:
        print(col,'호')

# 188

apart = [[101,102],[201,202],[301,302]]
for row in apart:
    for col in row:
        print(col,'호')
        print('-----')

# 189

apart = [[101,102],[201,202],[301,302]]
for row in apart:
    for col in row:
        print(col,'호')
        if col%2 == 0:
            print('-----')

# 190

apart = [[101,102],[201,202],[301,302]]
for row in apart:
    for col in row:
        print(col,'호')
print('-----')

# 191

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for row in data:
    for col in row:
        print(col*1.00014)

# 192
for row in data:
    for col in row:
        print(col*1.00014)
    print("-"*4)

# 193
result = []
for row in data:
    for col in row:
        result.append(col*1.00014)

print(result)

# 194
result = []
for row in data:
    sub = []
    for col in row:
        sub.append(col*1.00014)
    result.append(sub)

print(result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

print(ohlc[1][0])
print(ohlc[2][3])
print(ohlc[3][3])
for row in ohlc[1:]:
    print(row[3])

# 196
for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

# 197
for row in ohlc[1:]:
    if row[0] <= row[3]:
        print(row[3])

# 198

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []

for row in ohlc[1:]:
    volatility.append(row[1]-row[2])

print(volatility)

# 199
차이 = []
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3]> row[0]:
        차이.append(row[3]-row[0])
print(차이)

# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
a = 0
for row in ohlc[1:]:
    a+=row[0]-row[3]
    print(a)

