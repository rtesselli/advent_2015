import json


def load_data():
    with open("data/day12.txt", 'r') as f:
        return json.load(f)


def find_numbers(payload: list | dict) -> int:
    counter = 0
    if isinstance(payload, list):
        for obj in payload:
            if isinstance(obj, int):
                counter += obj
            elif isinstance(obj, list) or isinstance(obj, dict):
                counter += find_numbers(obj)
        return counter
    elif isinstance(payload, dict):
        for obj in payload.values():
            if isinstance(obj, int):
                counter += obj
            elif isinstance(obj, list) or isinstance(obj, dict):
                counter += find_numbers(obj)
        return counter
    return 0


if __name__ == '__main__':
    data = load_data()
    print(find_numbers(data))
