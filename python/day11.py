from itertools import groupby


def step(password: str, idx: int = -1) -> str:
    if abs(idx) > len(password):
        raise IndexError("Idx out of bound")
    temp = list(password)
    temp[idx] = chr(ord(temp[idx]) + 1)
    if temp[idx] == '{':
        temp[idx] = 'a'
        return step("".join(temp), idx=idx - 1)
    return "".join(temp)


def include_straight(password: str) -> bool:
    def is_straight(idx: int) -> bool:
        return ord(password[idx]) == ord(password[idx + 1]) - 1 == ord(password[idx + 2]) - 2

    return any(is_straight(idx) for idx, c in enumerate(password[:-2]))


def valid_chars(password: str) -> bool:
    return "i" not in password and "o" not in password and "l" not in password


def has_pairs(password: str) -> bool:
    counts = [len(list(group)) for _, group in groupby(password)]
    return sum(count // 2 for count in counts) >= 2


def comply(password: str) -> bool:
    return include_straight(password) and valid_chars(password) and has_pairs(password)


def next_password(password: str) -> str:
    while not comply(password):
        password = step(password)
    return password


if __name__ == '__main__':
    print(next_password("cqjxjnds"))
