def part1(rows):
    tree_count = 0
    start = 0
    for j in range(len(rows) - 1):
        for i in range(start, start + 5):
            start += 1
            if rows[j+1][i] == '#' and i == 4:
                tree_count += 1
    print(tree_count)


def main():
    with open('input.txt', 'r') as txt:
        puzzle_input = txt.read().splitlines()

    part1(puzzle_input)


if __name__ == '__main__':
    main()
