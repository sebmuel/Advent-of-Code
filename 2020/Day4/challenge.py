



def main():
    with open('input.txt', 'r')as text:
        puzzle_input = text.read().splitlines()

    data_list = []
    for line in puzzle_input:
        passports = line.split()
        if len(passports) == 0:
            continue
        for pass_data in passports:
            data_set = pass_data.strip()
            print(data_set)
        print(data_list)


if __name__ == '__main__':
    main()