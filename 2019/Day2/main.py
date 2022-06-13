from BoardComputer import *

if __name__ == '__main__':

    """
    INPUT HANDLING
    """
    with open("input.txt", "r") as puzzle_input:
        int_codes = puzzle_input.read().split(",")
        int_codes = [int(x) for x in int_codes]

    """
    PART 1
    """
    code_one = CodePart1(int_codes)

    code_one.eval_code()
    """
    PART 2
    """
    """    code_two = CodePart2(int_codes)
        part_two: int
        for noun in range(1, 100):
            for verb in range(100):
                output = code_two.search_output(noun, verb, 19690720)
                if output:
                    part_two = output
                    break
    """
    """
    PRINT
    """
    print(f"The Final Code at Position 0 is : {code_one.int_codes[0]}")

