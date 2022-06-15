def get_coordinates(options_dictonary):
    coordinates = []
    for key in options_dictonary.keys():
        start_x = int(options_dictonary.get(key)[0][0])
        start_y = int(options_dictonary.get(key)[0][1])
        _length = int(options_dictonary.get(key)[1][0])
        height = int(options_dictonary.get(key)[1][1])
        stack = set()
        for x in range(start_x, _length + start_x):
            for y in range(start_y, height + start_y):
                stack.add((x, y))
        coordinates.append(stack)
    return coordinates