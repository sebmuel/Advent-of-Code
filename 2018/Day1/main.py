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
    # frequencies = calc_freq(freq)
    # print(frequencies)

    """
    PART2
    """
    print(calc_freq(freq))

