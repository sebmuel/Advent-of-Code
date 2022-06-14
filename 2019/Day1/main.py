from Day1.Modul import Module

if __name__ == '__main__':

    """
    INPUT HANDLING
    """

    with open("test_input.txt", "r") as lines:
        masses = lines.read().splitlines()
        masses = [int(x) for x in masses]

    """
    PART 1
    """
    modules: [Module] = [Module(x) for x in masses]

    total_fuel = 0
    for module in modules:
        total_fuel += module.required_fuel

    """
    PART 2
    """

    total_fuel_extra = 0
    for module in modules:
        total_fuel_extra += module.required_fuel_extra

    print(f"TOTAL FUEL REQUIRED -> {total_fuel}")
    print(f"TOTAL FUEL REQUIRED + EXTRA -> {total_fuel_extra}")
