def part1(passports, keys):
    valid_list = []
    for passport in passports:
        valid = []
        for key in keys:
            if passport.find(key) != -1:
                valid.append(key)
        valid_list.append(valid)

    valid_passports = 0
    for valid in valid_list:
        req = 0
        opt = 0
        for value in valid:
            req += 1
            if value == 'cid':
                opt += 1
        if req == 7 and opt == 1 or req == 8:
            valid_passports += 1
    return valid_passports


def main():
    with open('input.txt', 'r')as text:
        puzzle_input = text.read().splitlines()

    keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')
    stack = []
    x = 0
    for i, passport in enumerate(puzzle_input):
        if passport == '' or i == len(puzzle_input) - 1:
            complete_pass = ' '.join(puzzle_input[x:i])
            stack.append(complete_pass)
            x = i + 1

    print(f"{part1(stack, keys)}")


if __name__ == '__main__':
    main()
