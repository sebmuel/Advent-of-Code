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
