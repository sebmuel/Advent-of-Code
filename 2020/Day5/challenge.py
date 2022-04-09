def part1(seats, partitioning):
    rows = seats["rows"]
    columns = seats["columns"]
    ids = []

    for partition in partitioning:
        row_search, column_search = partition[:7], partition[7:]
        current_row = rows

        for direction in row_search:
            if direction == 'F':
                current_row = current_row[:len(current_row)//2]
            elif direction == 'B':
                current_row = current_row[len(current_row) // 2:]
        row, current_row = current_row, rows

        current_col = columns
        for direction in column_search:
            if direction == 'R':
                current_col = current_col[len(current_col) // 2:]
            elif direction == 'L':
                current_col = current_col[:len(current_col) // 2]
        col,  current_col = current_col, columns

        ids.append(int(row[0]) * 8 + int(col[0]))

    return max(ids), sorted(ids)


def part2(ids):
    for i in range(len(ids) - 1):
        if ids[i + 1] - ids[i] != 1:
            return ids[i] + 1

def main():
    with open("input.txt", "r") as txt:
        partitioning = txt.read().splitlines()

    rows = [x for x in range(128)]
    columns = [x for x in range(8)]

    seats = {
        "rows": rows,
        "columns": columns
    }

    answer, ids = list(part1(seats, partitioning))

    print(f"Part1: {answer}")
    print(f"Part2: {part2(ids)}")


if __name__ == '__main__':
    main()