from collections import Counter

# Handle Input
with open('test.in') as file:
    data = file.read().splitlines()


def cordinates(lines):
    points = []
    for line in lines:

        x, y = line.split("->")
        x1, y1 = map(int, x.split(","))
        x2, y2 = map(int, y.split(","))

        if x1 == x2 or y1 == y2:
            for z in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    points.append((z, y))

    print(len([point for point in Counter(points).values() if point > 1]))


cordinates(data)