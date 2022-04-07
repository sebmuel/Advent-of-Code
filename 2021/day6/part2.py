# Handle Input
import collections

with open('input.in') as file:
    array = file.read().split(",")       # remove comma
    array = [int(x) for x in array]       # convert every char of str in int and wrap them in list


def count_fishes_b(intervals):
    days = 256
    fishes = intervals.copy()

    fishDict = {}

    for fish in fishes:
        if fish not in fishDict:
            fishDict[fish] = 0
        fishDict[fish] += 1

    for day in range(days):
        defaultFishDict = collections.defaultdict(int)      # avoid Key errors by using function passed
        for timer, amount in fishDict.items():
            if timer == 0:
                defaultFishDict[6] += amount                # reset timer of fish
                defaultFishDict[8] += amount                # create new fish
            else:
                defaultFishDict[timer-1] += amount          # move fish amount to other (n-1) key

            fishDict = defaultFishDict

    return sum(fishDict.values())


print("Answer for Part2: ", count_fishes_b(array))






