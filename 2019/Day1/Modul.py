"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.
"""
import math


class Module:
    mass: int
    required_fuel: int
    required_fuel_extra: int

    def __init__(self, mass: int):
        self.required_fuel = self.calc_fuel(mass)
        self.required_fuel_extra = self.calc_extra_fuel(mass)

    @staticmethod
    def calc_fuel(mass: int):
        return math.floor(mass / 3) - 2

    @staticmethod
    def calc_extra_fuel(mass: int):
        required_fuel = 0
        while Module.calc_fuel(mass) > 0:
            mass = Module.calc_fuel(mass)
            required_fuel += mass
        return required_fuel

