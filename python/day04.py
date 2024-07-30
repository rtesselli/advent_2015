import hashlib


def advent_coin(key: str, check_string: str) -> str:
    i = 0
    while True:
        combined = f"{key}{str(i)}"
        md5 = hashlib.md5(combined.encode()).hexdigest()
        if md5.startswith(check_string):
            return str(i)
        i += 1


if __name__ == '__main__':
    print(advent_coin("iwrupvqb", "00000"))
    print(advent_coin("iwrupvqb", "000000"))
