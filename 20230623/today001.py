import json

with open ("test_data.json") as f:
    data = json.load(f)

points= data['shapes'][0]['points']

print(points)

x =[]
y =[]
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

print(min(x),min(y))
print(max(x),max(y))
x0 = min(x)
y0 = min(y)
x1 = max(x)
y1 = max(y)

file = open('x,y최대최소값.txt','w')
file.write(f"{x0},{y0}\n{x1},{y1}")
file.close()