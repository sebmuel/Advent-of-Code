def part1(puzzle_input):
    forms = [x.split(" ") for x in puzzle_input]
    counts = []
    for grp in forms:
        if len(grp) == 1:
            counts.append(len(grp[0]))
        else:
            dupe = ''
            for qst in grp:
                for answer in qst:
                    if answer not in dupe:
                        dupe += answer
            counts.append(len(dupe))
    return sum(counts)


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

    print(f"Part1: {part1(data_formatted)}")


if __name__ == '__main__':
    main()
