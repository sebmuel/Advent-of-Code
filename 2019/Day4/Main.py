"""
You arrive at the Venus fuel depot only to discover it's protected by a password.
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
278384-824795
"""

def eval_pw(pw_list, func):
    valid_list = []
    for i, pw in enumerate(pw_list):
        if not func(pw):
            continue
        valid_list.append(pw)
    return valid_list

def is_sorted(pw):
    pw = str(pw)
    flag = 0
    if all(pw[i] <= pw[i + 1] for i in range(len(pw) - 1)):
        flag = 1
    return flag

def has_duplicate(pw):
    pw = str(pw)
    return len(set(pw)) != len(pw)


def final_condition(pw):
    tracker = {}
    for number in str(pw):
        if number in tracker and tracker.get(number) is not None:
            tracker[number] += 1
        else:
            tracker[number] = 1
    value_list = list(tracker.values())
    try:
        position = value_list.index(2)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    minimum, maximum = 278384, 824795
    pw_raw = [x for x in range(minimum, maximum+1)]
    test1, test2, test3 = 111111, 1150111, 123789
    sorted_pw = eval_pw(pw_raw, is_sorted)
    duped = eval_pw(sorted_pw, has_duplicate)
    final = eval_pw(duped, final_condition)
    print(len(final))



