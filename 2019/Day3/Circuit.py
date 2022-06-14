class Circuit:

    wire_one: [str]
    wire_two: [str]
    log: [[str, str]]
    run_counter: int
    current_x, current_y = 0, 0
    step_counter = 0

    def __init__(self):
        self.run_counter = 0
        self.log = []
        self.intersections = []
        with open("input.txt", "r") as wires:
            self.wire_one = wires.readline().strip().split(",")
            self.wire_two = wires.readline().strip().split(",")

    def init_wire(self, wire: [str]):
        self.current_y, self.current_x = 0, 0
        self.log.append([])
        self.intersections.append([])
        self.step_counter = 0
        for path in wire:
            direction = path[:1]
            steps = int(path[1:])
            self.wire_navigation(direction, steps)
        self.run_counter += 1

    def wire_navigation(self, direction, steps):
        if direction == "R":
            for _ in range(self.current_x, self.current_x + steps):
                self.current_x += 1
                self.step_counter += 1
                self.log[self.run_counter].append((self.current_y, self.current_x))
        elif direction == "L":
            for _ in range(self.current_x, (self.current_x - steps), -1):
                self.current_x -= 1
                self.step_counter += 1
                self.log[self.run_counter].append((self.current_y, self.current_x))
        elif direction == "U":
            for _ in range(self.current_y, self.current_y + steps, 1):
                self.current_y += 1
                self.step_counter += 1
                self.log[self.run_counter].append((self.current_y, self.current_x))
        elif direction == "D":
            for _ in range(self.current_y, (self.current_y - steps), -1):
                self.current_y -= 1
                self.step_counter += 1
                self.log[self.run_counter].append((self.current_y, self.current_x))

    def split_array(self, array: list):
        log = self.log[:]
        set1, set2 = set(log[0]), set(log[1])
        return set1, set2

    def get_intersections(self):
        set1, set2 = self.split_array(self.log)
        return set1.intersection(set2)

    def get_min_intersection(self):
        wire1, wire2 = list(self.log[0]), list(self.log[1])
        intersections = self.get_intersections()
        distances = []
        for i, intersection in enumerate(intersections):
            distances.append(len(wire1[:wire1.index(intersection) + 1]) + len(wire2[:wire2.index(intersection) + 1]))

        return min(distances)

