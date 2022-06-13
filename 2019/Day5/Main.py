from Day5.Classes.UpgradedBoardComputer import UpgradedBoardComputer

"""
optcode, 
1002,4,3,4,33

ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
                                  
This instruction multiplies its first two parameters. The first parameter, 4 in 
position mode, works like it did before - 
its value is the value stored at address 4 (33). The second parameter, 3 in immediate 
mode, simply has value 3. The result of this operation, 33 * 3 = 99, is written 
according to the third parameter, 
4 in position mode, which also works like it did before - 99 is written to address 4.
"""

if __name__ == '__main__':
    string = "1002,4,3,4,33".split(",")

    t = UpgradedBoardComputer(string)
    t.read_code()
