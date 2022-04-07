# Handle Input
with open('input.in') as file:
    data = file.read().split(",")       # remove comma
    data = [int(x) for x in data]       # convert every char of str in int and wrap them in list


def count_fishes_a(intervals):
    days = 80

    fishes = [i for i in intervals]
    for x in range(0, days):
        for i, fish in enumerate(fishes):
            if fishes[i] > 0:
                fishes[i] -= 1
            elif fishes[i] == 0:
                fishes[i] = 6
                fishes.append(9)        # set 1 higher than 8 because we are not skipping new fishes

    return len(fishes)


print("Answer for Part1: ", count_fishes_a(data))






