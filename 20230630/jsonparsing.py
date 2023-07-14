import json

with open ("test_data.json") as f:
    data = json.load(f)

# print(data)

points = data['shapes'][0]['points']

x = []
y = []

for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

x0 = min(x)
y0 = min(y)
x1 = max(x)
y1 = max(y)

print(f"최소값:x{x0}, y{y0} 최대값:x{x1}, y{y1}")