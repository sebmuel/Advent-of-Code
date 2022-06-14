from Functions.functs import *

if __name__ == '__main__':
    """
    TESTS
    """
    """
    test_input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    for i in range(len(test_input)):
        print(f"------------Test:{i+1}-----------------")
        print(create_id_dictonary(test_input[i]).get(2))
        print(create_id_dictonary(test_input[i]).get(3))
    """

    """
    INPUT HANDLING
    """
    with open("input.txt", "r") as ids:
        ids = [x.strip() for x in ids.readlines()]

    print(part1(ids))
