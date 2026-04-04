import networkx as nx
from pathlib import Path
from itertools import permutations, pairwise
from typing import Sequence, Callable


def load_graph() -> nx.Graph:
    lines = Path("data/day09.txt").read_text().splitlines()
    g = nx.Graph()
    for line in lines:
        path, distance = line.split(" = ")
        from_, to = path.split(" to ")
        g.add_edge(from_, to, weight=int(distance))
    return g


def get_distance(g: nx.Graph, path: Sequence[str]) -> int:
    distance = 0
    for u, v in pairwise(path):
        distance += g[u][v]["weight"]
    return distance


def get_distance_brute_force(g: nx.Graph, fn: Callable = min) -> int:
    return fn(get_distance(g, path) for path in permutations(g.nodes))


if __name__ == '__main__':
    graph = load_graph()
    print(get_distance_brute_force(graph))
    print(get_distance_brute_force(graph, max))
