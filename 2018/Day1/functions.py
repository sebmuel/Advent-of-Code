import operator
from itertools import cycle


def part1(frequencies: [str]):
    frequency = 0
    for freq in frequencies:
        ops = {"+": operator.add, "-": operator.sub}
        _ops = freq[0]
        value = int(freq[1:])
        frequency = ops[_ops](frequency, value)
    return frequency


def part2(frequencies: [str]):
    frequency = 0
    log = set()
    for freq in cycle(frequencies):
        ops = {"+": operator.add, "-": operator.sub}
        _ops = freq[0]
        value = int(freq[1:])
        frequency = ops[_ops](frequency, value)
        if frequency in log:
            return frequency
        log.add(frequency)
