from Circuit import Circuit

if __name__ == '__main__':
    """
    PART 1
    """
    circuit = Circuit()
    circuit.init_wire(circuit.wire_one)
    circuit.init_wire(circuit.wire_two)

    """
    PRINT
    """
    # print(f"The lowest distance is: {circuit.log}")
    print(f"The lowest distance is: {circuit.get_min_intersection()}")






