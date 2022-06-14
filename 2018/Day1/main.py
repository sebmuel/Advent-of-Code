from functions import *

if __name__ == '__main__':
    """
    INPUT HANDLING
    """
    with open("input.txt", "r") as frequencies:
        freq = [x.strip() for x in frequencies]

    """
    PART1
    """
    print(f"Part 1: {part1(freq)}")

    """
    PART2
    """
    print(f"Part 2: {part2(freq)}")

