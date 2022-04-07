with open("input.txt") as fin:
    data = [i for i in fin.read().strip().split("\n")]


def mostBit(str):
    ones = str.count("1")
    zero = str.count("0")
    if ones > zero:
        return 1
    else:
        return 0


def loop(bitlist, i, n=bool):
    a = ""
    b = ""
    for bin in bitlist:
        if bin[i] == "1":
            a += bin[i]
        else:
            b += bin[i]
    if n:
        if len(a) > len(b) or len(a) == len(b):
            bitlist = [x for x in bitlist if not x[i] == "1"]
            return bitlist
        else:
            bitlist = [x for x in bitlist if not x[i] == "0"]
            return bitlist
    else:
        if len(a) > len(b) or len(a) == len(b):
            bitlist = [x for x in bitlist if not x[i] == "0"]
            return bitlist
        else:
            bitlist = [x for x in bitlist if not x[i] == "1"]
            return bitlist


def search(list, i, n=bool):
    while len(list) > 1:
        list = loop(list, i, n)
        i += 1
    return list


oxygenGeneratorRating = search(data, 0, n=False)
scrubberRating = search(data, 0, n=True)

oxygenGeneratorRating = str(oxygenGeneratorRating[0])
scrubberRating = str(scrubberRating[0])

print(int(oxygenGeneratorRating, 2) * int(scrubberRating, 2))
