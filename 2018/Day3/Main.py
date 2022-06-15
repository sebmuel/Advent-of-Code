from functions.functions import get_coordinates


if __name__ == '__main__':

    """
    INPUT HANDLING
    """
    with open("input.txt", "r") as claims:
        claims = [x.strip() for x in claims.readlines()]

    options_dictonary = dict()

    for i, claim in enumerate(claims, 1):
        values = claim[claim.find("@") + 2:]
        start, dimension = values.split()
        start = start[:-1]
        x, y = start.split(",")
        t = tuple((x, y))
        rectangle = tuple(dimension.split("x"))
        options_dictonary[i] = [t, rectangle]

    """
    PART 1
    """
    rectangle_coordinates = get_coordinates(options_dictonary)

    count = 0
    for rectangle in rectangle_coordinates:
        for rectangle_compare in rectangle_coordinates[1:]:
            if len(rectangle_compare.intersection(rectangle)) > 0:
                count += 1
    print((count-1) * 2)
