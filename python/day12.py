import json


def load_data():
    with open("data/day12.txt", 'r') as f:
        return json.load(f)


def find_numbers(payload: list | dict, skip_red: bool = False) -> int:
    counter = 0
    if isinstance(payload, list):
        for obj in payload:
            if isinstance(obj, int):
                counter += obj
            elif isinstance(obj, list) or isinstance(obj, dict):
                counter += find_numbers(obj, skip_red)
        return counter
    elif isinstance(payload, dict):
        if skip_red and "red" in payload.values():
            return 0
        for obj in payload.values():
            if isinstance(obj, int):
                counter += obj
            elif isinstance(obj, list) or isinstance(obj, dict):
                counter += find_numbers(obj, skip_red)
        return counter
    return 0


if __name__ == '__main__':
    data = load_data()
    print(find_numbers(data))
    print(find_numbers(data, skip_red=True))
