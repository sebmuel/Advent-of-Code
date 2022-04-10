def part1(puzzle_input):
    i = 0
    for grp in puzzle_input:
        for qst in grp:
            if qst != ' ':
                i += 1
    print(i)



def main():
    with open("input.txt", "r") as txt:
        puzzle_input = txt.read().splitlines()

    stack = []
    data_formatted = [] = []

    while len(puzzle_input):
        if puzzle_input[0] != '':
            stack.append(puzzle_input[0])
        else:
            data_formatted.append(' '.join(stack.copy()))
            stack.clear()
        if len(puzzle_input) == 1:
            data_formatted.append(' '.join(stack.copy()))
        puzzle_input.pop(0)

    part1(data_formatted)



if __name__ == '__main__':
    main()