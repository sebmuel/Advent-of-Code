class CodePart1:

    current_position: int
    int_codes = [int]

    def __init__(self, int_codes: [int], current_position=0):
        self.int_codes = int_codes.copy()
        self.current_position = current_position

    def move_position(self, steps: int):
        self.current_position += steps

    def eval_code(self):

        for int_code in self.int_codes:
            opcode = self.int_codes[self.current_position]
            if opcode == 99:
                return
            elif opcode == 1:
                input1_index = self.int_codes[self.current_position + 1]
                input2_index = self.int_codes[self.current_position + 2]
                output_index = self.int_codes[self.current_position + 3]
                input1_value = self.int_codes[input1_index]
                input2_value = self.int_codes[input2_index]
                self.int_codes[output_index] = input1_value + input2_value
            elif opcode == 2:
                input1_index = self.int_codes[self.current_position + 1]
                input2_index = self.int_codes[self.current_position + 2]
                output_index = self.int_codes[self.current_position + 3]
                input1_value = self.int_codes[input1_index]
                input2_value = self.int_codes[input2_index]
                self.int_codes[output_index] = input1_value * input2_value
            self.move_position(4)

    def restore_gravity_assist(self, pos1: int, pos2: int):
        self.int_codes[1] = pos1
        self.int_codes[2] = pos2


class CodePart2(CodePart1):

    reset_memory: [int]

    def __init__(self, int_codes: [int]):
        super(CodePart2, self).__init__(int_codes)
        self.reset_memory = int_codes.copy()

    def search_output(self, noun: int, verb: int, search_value: int):
        self.reset_program()
        self.restore_gravity_assist(noun, verb)
        self.eval_code()
        output = self.int_codes[0]
        if output == search_value:
            return 100 * noun + verb
        return False

    def reset_program(self):
        self.int_codes = self.reset_memory.copy()
        self.current_position = 0