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
    max_length = len(rows[0])
    depth = len(rows)
    trees = []
    for slope in slopes:
        x, y = 0, 0
        x_inc, y_inc = slope[0], slope[1]
        t = 0
        while y < depth:
            if rows[y][x] == '#':
                t += 1
            x += x_inc
            y += y_inc
            if x >= max_length:
                x %= max_length
        trees.append(t)

    count = 0
    for tree in trees:
        if count == 0:
            count += tree
        else:
            count *= tree

    return count


def main():
    with open('input.txt', 'r') as txt:
        puzzle_input = txt.read().splitlines()

    # part 2 data
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    print(f"Answer Part1: {part1(puzzle_input)} trees")
    print(f"Answer Part2: {part2(puzzle_input, slopes)}")


if __name__ == '__main__':
    main()
