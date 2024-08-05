from pathlib import Path
from collections import Counter, defaultdict
from more_itertools import pairwise, triplewise


def read_strings() -> list[str]:
    return Path("../data/day05.txt").read_text().split("\n")


def has_3_vowels(string: str) -> bool:
    counts = Counter(string)
    return counts["a"] + counts["e"] + counts["i"] + counts["o"] + counts["u"] >= 3


def same_consecutive(string: str) -> bool:
    return any(first == second for first, second in pairwise(string))


def check_blacklist(string: str) -> bool:
    return "ab" not in string and "cd" not in string and "pq" not in string and "xy" not in string


def is_nice(string: str) -> bool:
    return has_3_vowels(string) and same_consecutive(string) and check_blacklist(string)


def has_2_pairs(string: str) -> bool:
    starts = defaultdict(list)
    for start, (first, second) in enumerate(pairwise(string)):
        starts[f"{first}{second}"].append(start)
    for pair in starts.keys():
        last_check = 0
        to_check = 1
        while True:
            if to_check >= len(starts[pair]):
                break
            if starts[pair][last_check] == starts[pair][to_check] - 1:
                starts[pair].pop(to_check)
            else:
                last_check = to_check
                to_check += 1
    return any(len(start_points) >= 2 for pair, start_points in starts.items())


def has_broken_repeat(string: str) -> bool:
    return any(first == third for first, second, third in triplewise(string))


def is_nice2(string: str) -> bool:
    return has_2_pairs(string) and has_broken_repeat(string)


if __name__ == '__main__':
    strings = read_strings()
    print(sum(is_nice(string) for string in strings))
    print(sum(is_nice2(string) for string in strings))
