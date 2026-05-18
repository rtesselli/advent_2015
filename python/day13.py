from collections import defaultdict
from pathlib import Path
from itertools import permutations, pairwise


def load_preferences() -> dict:
    lines = Path("data/day13.txt").read_text().splitlines()
    data = defaultdict(dict)
    for line in lines:
        terms = line.split()
        subj = terms[0]
        target = terms[-1][:-1]
        sign = 1 if terms[2] == 'gain' else -1
        amount = int(terms[3])
        data[subj][target] = sign * amount
    return data


def get_best_happiness(preferences: dict) -> int:
    attendees = list(preferences.keys())
    first = attendees.pop(0)
    best_score = 0
    for permutation in permutations(attendees):
        sequence = [first] + list(permutation)
        score = 0
        for a, b in pairwise(sequence):
            score += preferences[a][b]
            score += preferences[b][a]
        score += preferences[sequence[0]][sequence[-1]]
        score += preferences[sequence[-1]][sequence[0]]
        best_score = max(best_score, score)
    return best_score


if __name__ == '__main__':
    links = load_preferences()
    print(get_best_happiness(links))
    original_keys = links.keys()
    links["Riccardo"] = {t: 0 for t in original_keys}
    for s in original_keys:
        links[s]["Riccardo"] = 0
    print(get_best_happiness(links))
