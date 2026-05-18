from pathlib import Path


def load_stats() -> dict:
    lines = Path("data/day14.txt").read_text().splitlines()
    out = {}
    for line in lines:
        terms = line.split()
        subj = terms[0]
        speed = int(terms[3])
        resistance = int(terms[6])
        rest = int(terms[-2])
        out[subj] = {
            "speed": speed,
            "resistance": resistance,
            "rest": rest
        }
    return out


def get_winner_distance(stats: dict, step: int = 1000) -> int:
    distances = {}
    for subj, stat in stats.items():
        cycle_time = stat["resistance"] + stat["rest"]
        cycle, remainder = divmod(step, cycle_time)
        if remainder > stat["resistance"]:
            distance = stat["speed"] * stat["resistance"] * (cycle + 1)
        else:
            distance = stat["speed"] * stat["resistance"] * cycle + stat["speed"] * remainder
        distances[subj] = distance
    print(distances)
    return max(distances.values())


if __name__ == '__main__':
    reindeer_stats = load_stats()
    print(get_winner_distance(reindeer_stats, step=2503))
