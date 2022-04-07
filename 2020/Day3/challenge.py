def part1(rows):
    # find pattern
    stack1 = rows
    stack2 = []

    while len(rows):
        stack2.append(rows[0])
        stack1.pop(0)
        if stack2 == stack1:
            print('found pattern')
    print(f"Stack1: {stack1}, Stack2: {stack2}")

def main():
    with open('input.txt', 'r') as txt:
        puzzle_input = txt.read().splitlines()

    part1(puzzle_input)


if __name__ == '__main__':
    main()
