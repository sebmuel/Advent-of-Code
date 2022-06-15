"""
PART 1
"""

def create_id_dictonary(_id: str) -> dict[int, str]:
    packet_ids = dict()
    for c in _id:
        if c in packet_ids.keys():
            packet_ids[c] += 1
        else:
            packet_ids[c] = 1
    # switch keys and values with each other
    return {value: key for key, value in packet_ids.items()}

def part1(ids: [str]):
    pairs = 0
    triples = 0
    for _id in ids:
        char_map = create_id_dictonary(_id)
        if char_map.get(2) is not None:
            pairs += 1
        if char_map.get(3) is not None:
            triples += 1
    return pairs * triples


"""
PART 2
"""

def compare_ids(_id_one, _id_two):
    match = 0
    for i in range(len(_id_one)):
        index_a = _id_one[i]
        index_b = _id_two[i]
        if index_a == index_b:
            match += 1
    return match

def remove_diff(_id_one: str, _id_two: str):
    final_id = ""
    for char in _id_one:
        if char not in _id_two:
            final_id = _id_one.replace(char, "")
            return final_id

def part2(ids: [str]):
    for _id_one in ids:
        for _id_two in ids[1:]:
            if compare_ids(_id_one, _id_two) == len(_id_one) - 1 and _id_two != _id_one:
                return remove_diff(_id_one, _id_two)
