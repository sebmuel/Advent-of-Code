class UpgradedBoardComputer:
    code = [str]
    pointer: int = 0
    system_id = 1
    output = []

    def __init__(self, code: list[str]):
        self.code = code

    def read_code(self):
        for _ in self.code:
            code = self.code[self.pointer]
            opcode = code[-2:]
            parameter_modes = list(code[:-2].zfill(3))[::-1]
            self.run_code(opcode, parameter_modes)

    def run_code(self, opcode: str, parameter_modes: []) -> None:
        if opcode == "99":
            return
        elif opcode == "01" or opcode == "1":
            self._add(parameter_modes)
            self.move_pointer(4)
        elif opcode == "02" or opcode == "2":
            self.multi(parameter_modes)
            self.move_pointer(4)
        elif opcode == "03" or opcode == "3":
            self.dunno()
            self.move_pointer(2)
        elif opcode == "04" or opcode == "4":
            self.dunno_two()
            self.move_pointer(2)

    def multi(self, parameter_modes):
        instruction = self.code[self.pointer+1:self.pointer + 4]
        parameters = list(zip(list(instruction), list(parameter_modes)))
        value_one = parameters[0][0] if parameters[0][1] == "1" else self.code[int(parameters[0][0])]
        value_two = parameters[1][0] if parameters[1][1] == "1" else self.code[int(parameters[1][0])]
        out_index = parameters[2][0]
        self.code[int(out_index)] = str(int(value_one) * int(value_two))

    def _add(self, parameter_modes):
        instruction = self.code[self.pointer+1:self.pointer + 4]
        parameters = list(zip(instruction, parameter_modes))
        value_one = parameters[0][0] if parameters[0][1] == "1" else self.code[int(parameters[0][0])]
        value_two = parameters[1][0] if parameters[1][1] == "1" else self.code[int(parameters[1][0])]
        out_index = int(parameters[2][0])
        self.code[out_index] = str(int(value_one) + int(value_two))

    """
    Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, 
    the instruction 3,50 would take an input value and store it at address 50.
    """

    def dunno(self):
        instruction = self.code[self.pointer + 1:self.pointer + 2]
        out_index = int(instruction[0])
        self.code[out_index] = str(self.system_id)

    def dunno_two(self):
        instruction = self.code[self.pointer+1:self.pointer + 2]
        self.output.append(self.code[int(instruction[0])])

    def move_pointer(self, steps: int):
        self.pointer += steps