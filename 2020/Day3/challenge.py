def part1(rows):
    # build path
    # some high int cause im to stupid to figure out the math behind
    mirror_amount = 1000
    path = []
    for row in rows:
        path_multi = ''
        for i in range(mirror_amount + 1):
            path_multi += row
        path.append(path_multi)

    start = 0
    trees = 0
    # walk path
    for i in range(len(path) - 1):
        for j in range(start, start + 4, 1):
            start = j
        if path[i + 1][start] == '#':
            trees += 1

    return trees


def part2(rows, slopes):
    print(len(rows))
    # print(len(rows[0]))

    # build path
    # some high int cause im to stupid to figure out the math behind
    # you might need to increase the number if you increase the slope_right value further
    # or you just smarter than me and figure out the math :)
    mirror_amount = 500
    path = []
    for row in rows:
        path_multi = ''
        for i in range(mirror_amount + 1):
            path_multi += row
        path.append(path_multi)

    results = []
    for slope in slopes:
        trees = 0
        start = 0
        slope_right = slope[0]
        slope_down = slope[1]
        for i in range(start, len(path) - slope_down):
            for j in range(start, start + slope_right + 1, slope_down):
                start = j
            if path[i + slope_down][start] == '#':
                trees += 1
        results.append(int(trees))

    answer = 1
    for trees in results:
        answer *= trees

    return answer


def main():
    with open('input.txt', 'r') as txt:
        puzzle_input = txt.read().splitlines()

    # part 2 data
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    print(f"Answer Part1: {part1(puzzle_input)} trees")
    print(f"Answer Part2: {part2(puzzle_input, slopes)}")


if __name__ == '__main__':
    main()
