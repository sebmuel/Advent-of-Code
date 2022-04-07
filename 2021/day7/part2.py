# Input Handle
with open('input.in') as file:
    horizontalPositions = file.read().split(",")
    horizontalPositions = [int(x) for x in horizontalPositions]

need = 168


def count_fuel(dataset):
    fuel = []
    positionToReach = [x for x in range(max(dataset))]

    for posTo in positionToReach:
        fuel_tank = []
        for position in dataset:
            currentPosition = position
            distance = (max(currentPosition, posTo) - min(posTo, currentPosition))
            fuel_count = 0
            cost = 0
            for way in range(distance):
                cost += 1
                fuel_count += cost
            fuel_tank.append(fuel_count)
        fuel.append(sum(fuel_tank))

    return min(fuel)











print("Answer for Part2: ", count_fuel(horizontalPositions))
