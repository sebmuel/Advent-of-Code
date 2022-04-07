from readInput import read_input
from chunkString import chunkString


with open("input.txt") as fin:
    data = [i for i in fin.read().strip().split("\n")]

one = ""
two = ""
three = ""
four = ""
five = ""
six = ""
seven = ""
eight = ""
nine = ""
ten = ""
eleven = ""
twelve = ""

for column in data:
    one += column[0]
    two += column[1]
    three += column[2]
    four += column[3]
    five += column[4]
    six += column[5]
    seven += column[6]
    eight += column[7]
    nine += column[8]
    ten += column[9]
    eleven += column[10]
    twelve += column[11]


def mostBit(str):
    ones = str.count("1")
    zero = str.count("0")
    if ones > zero:
        return 1
    else:
        return 0


one = str(mostBit(one))
two = str(mostBit(two))
three = str(mostBit(three))
four = str(mostBit(four))
five = str(mostBit(five))
six = str(mostBit(six))
seven = str(mostBit(seven))
eight = str(mostBit(eight))
nine = str(mostBit(nine))
ten = str(mostBit(ten))
eleven = str(mostBit(eleven))
twelve = str(mostBit(twelve))

gammaRate = one+two+three+four+five+six+seven+eight+nine+ten+eleven+twelve


bit_s = gammaRate
inverse_s = ''

for i in bit_s:

    if i == '0':
        inverse_s += '1'

    else:
        inverse_s += '0'


gammaRate = int(gammaRate, 2)
epsilonRate = int(inverse_s, 2)

print(gammaRate*epsilonRate)
