def part1(puzzle_input):

    counts = []
    for grp in puzzle_input:
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


def part2(puzzle_input):

    counts = []
    for grp in puzzle_input:
        person_answers = len(grp)

        if person_answers == 1:
            counts.append(len(grp[0]))
        else:
            stack = ''
            for person in grp:
                stack += person
            # need check here but what ???
            p = ''
            c = 0
            for s in stack:
                if s not in p:
                    c += 1
                    p += s

            if c == len(p):
                counts.append(c)
            c = 0
    print(sum(counts))



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

    forms = [x.split(" ") for x in data_formatted]
    #print(f"Part1: {part1(forms)}")
    part2(forms)


if __name__ == '__main__':
    main()
