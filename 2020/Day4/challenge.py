import re


def part1(passports, keys):

    data_set = []
    for passport in passports:
        d = {}
        strings = passport.split()
        for data in strings:
            key, value = data.split(":")
            d[key] = value
        data_set.append(d)

    id_checked = []
    for data in data_set:
        stack = {}
        key: object
        for key in keys:
            if key in data:
                stack[key] = data[key]
        id_checked.append(stack.copy())
        stack.clear()
    validated_id = []
    for id in id_checked:
        valids = len(id)
        if valids == 8:
            validated_id.append(id)
        elif valids == 7 and 'cid' not in id:
            validated_id.append(id)
    return len(validated_id)

def part2(passports, keys):

    data_set = []
    for passport in passports:
        d = {}
        strings = passport.split()
        for data in strings:
            key, value = data.split(":")
            d[key] = value
        data_set.append(d)

    id_checked = []
    for data in data_set:
        stack = {}
        key: object
        for key in keys:
            if key in data:
                stack[key] = data[key]
        id_checked.append(stack.copy())
        stack.clear()
    validated_id = []
    for id in id_checked:
        valids = len(id)
        if valids == 8:
            for key in keys:
                if validate_values(key, id):
                    pass



        elif valids == 7 and 'cid' not in id and validate_values(id):
            validated_id.append(id)

    return len(validated_id)


# helpers
def validate_values(pass_key,id):
    valid = False

    for key, value in id.items():
        if key == pass_key and 1920 <= int(value) <= 2002:
            valid = True
        elif key == pass_key and 2010 <= int(value) <= 2020:
            valid = True
        elif key == pass_key and 2020 <= int(value) <= 2030:
            valid = True
        elif key == pass_key:
            unit, unit_value = value[-2:], value[:-2]
            if unit == pass_key and 150 <= int(unit_value) <= 193:
                valid = True
            elif unit == pass_key and 59 <= int(unit_value) <= 76:
                valid = True
        elif key == pass_key and re.search("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", value):
            valid = True
        elif key == pass_key and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid = True
        elif key == pass_key and len(value) == 8:
            valid = True

    return valid


def main():
    with open('input.txt', 'r')as text:
        puzzle_input = text.read().splitlines()

    keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

    stack = []
    passports = []

    while len(puzzle_input):
        if puzzle_input[0] != '':
            stack.append(puzzle_input[0])
        else:
            passports.append(' '.join(stack.copy()))
            stack.clear()
        if len(puzzle_input) == 1:
            passports.append(' '.join(stack.copy()))
        puzzle_input.pop(0)

    #print(f"Part1: {part1(passports, keys)} Valid ID`s")
    print(f"Part2: {part2(passports, keys)} Valid ID`s")


if __name__ == '__main__':
    main()
