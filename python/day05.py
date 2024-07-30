from pathlib import Path
from collections import Counter
from more_itertools import pairwise


def read_strings() -> list[str]:
    return Path("../data/day05.txt").read_text().split("\n")


def has_3_vowels(string: str) -> bool:
    counts = Counter(string)
    return counts["a"] + counts["e"] + counts["i"] + counts["o"] + counts["u"] >= 3


def same_consecutive(string: str) -> bool:
    for first, second in pairwise(string):
        if first == second:
            return True
    return False


def check_blacklist(string: str) -> bool:
    return "ab" not in string and "cd" not in string and "pq" not in string and "xy" not in string


def is_nice(string: str) -> bool:
    return has_3_vowels(string) and same_consecutive(string) and check_blacklist(string)


if __name__ == '__main__':
    strings = read_strings()
    print(sum(1 for string in strings if is_nice(string)))
