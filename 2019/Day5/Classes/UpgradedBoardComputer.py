class UpgradedBoardComputer:
    code = [str]
    pointer: int = 0

    def __init__(self, code: list[str]):
        self.code = code

    def read_code(self):
        for int_code in self.code:
            code = self.code[self.pointer]
            opcode = code[-2:]
            parameter_modes = list(code[:-2].zfill(3))[::-1]
            self.run_code(opcode, parameter_modes)

    def run_code(self, opcode: str, parameter_modes: str) -> None:
        if opcode == "99":
            return
        elif opcode == "01":
            self._add(parameter_modes)
        elif opcode == "02":
            self.multi(parameter_modes)
        elif opcode == "03":
            print("Multi")
        elif opcode == "04":
            print("Multi")

    def multi(self, parameter_modes):
        instruction = self.code[self.pointer + 1:4]
        parameters = list(zip(list(instruction), list(parameter_modes)))
        value_one = parameters[0][0] if parameters[0][1] == "1" else self.code[int(parameters[0][0])]
        value_two = parameters[1][0] if parameters[1][1] == "1" else self.code[int(parameters[1][0])]
        out_index = parameters[2][0]
        self.code[int(out_index)] = str(int(value_one) * int(value_two))
        self.pointer += 4
        print(self.code)

    def _add(self, parameter_modes):
        instruction = self.code[self.pointer + 1:4]
        parameters = list(zip(instruction, parameter_modes))
        value_one = parameters[0][0] if parameters[0][1] == "1" else self.code[int(parameters[0][0])]
        value_two = parameters[1][0] if parameters[1][1] == "1" else self.code[int(parameters[1][0])]
        out_index = parameters[2][0]
        self.code[int(out_index)] = str(int(value_one) + int(value_two))
        self.pointer += 4
        print(self.code)

    """
    Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, 
    the instruction 3,50 would take an input value and store it at address 50.
    """

    def dunno(self):
        pass
