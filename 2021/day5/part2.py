from collections import Counter

# Handle Input
with open('test.in') as file:
    data = file.read().splitlines()


def cordinates_part_1(lines):
    points = []
    for line in lines:

        x, y = line.split("->")
        x1, y1 = map(int, x.split(","))
        x2, y2 = map(int, y.split(","))

        if x1 == x2 or y1 == y2:
            for z in range(min(x1, x2), max(x1, x2) + 1):
                for u in range(min(y1, y2), max(y1, y2) + 1):
                    points.append((z, u))

    return len([point for point in Counter(points).values() if point > 1])


def cordinates_part_2(lines):
    points = []

    for line in lines:

        x, y = line.split("->")
        x1, y1 = map(int, x.split(","))
        x2, y2 = map(int, y.split(","))

        if x1 == x2 or y1 == y2:
            for z in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    points.append((z, y))

        else:
            x_handle = 1 if x1 > x2 else -1
            y_handle = 1 if y1 > y2 else -1

            a = x2
            b = y2
            points.append((a, b))
            for o in range(min(x1, x2), max(x1, x2)):
                a += x_handle
                b += y_handle
                points.append((a, b))

    return len([point for point in Counter(points).values() if point > 1])


print("Answer for Part1: ", cordinates_part_1(data))
print("Answer for Part2: ", cordinates_part_2(data))
