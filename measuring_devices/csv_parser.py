from csv import reader
from matplotlib import pyplot

x: list[float] = []
y: list[float] = []

for row in reader(open('tek00012.csv')):
    x.append(float(row[0]))
    y.append(float(row[1]))

pyplot.title("Line graph")
pyplot.plot(x, y, color="blue")
pyplot.show()

print("maximum y value:", max(y))
print("y width:", max(y) - min(y))

THRESHOLD: int = 10
positives: list = []
for index in range(len(y)):
    if y[index] >= THRESHOLD:
        positives.append((x[index], y[index]))

print("Point:", positives[0])
print("Point:", positives[-1])
print("WIDTH:", positives[-1][0] - positives[0][0])
