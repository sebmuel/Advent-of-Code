from readInput import read_input
import re


class Submarine:
    depth = 0
    horizontal = 0
    aim = 0

    def forward(self, x):
        self.horizontal += x
        self.depth += self.aim*x

    def down(self, x):
        self.aim += x

    def up(self, x):
        self.aim -= x


commands = read_input('input.txt', 'false')

for command in commands:
    step = int(re.search(r'\d+', command).group())
    direction = re.sub(r'\s*\d+\s*', '', command)

    if direction == 'forward':
        Submarine.forward(Submarine, step)

    if direction == 'down':
        Submarine.down(Submarine, step)

    if direction == 'up':
        Submarine.up(Submarine, step)

print(Submarine.horizontal * Submarine.depth)
