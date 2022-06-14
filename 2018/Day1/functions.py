import operator

def calc_freq(frequencies: [str]):
    frequency = 0
    log = []

    i = 0
    while True:

        for freq in frequencies:
            ops = {"+": operator.add, "-": operator.sub}
            _ops = freq[0]
            value = int(freq[1:])
            frequency = ops[_ops](frequency, value)
            if frequency not in log:
                log.append(frequency)
            else:
                return frequency
