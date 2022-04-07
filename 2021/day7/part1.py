# Input Handle
with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]

need = 168


def count_fuel(dataset):

    fuel = []
    # outer loop -> smallest to the biggest position
    for pos in range(min(dataset), max(dataset) + 1):
        passFuel = []
        for cost, currentPos in enumerate(dataset):
            passFuel.append(sum([abs(currentPos - pos)]))
        fuel.append(passFuel)
        print(passFuel)

    return min(fuel)


print("Answer for Part1: ", count_fuel(horizontalPositions))
