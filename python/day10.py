from itertools import groupby


def iterate(n: int, iterations: int = 40) -> int:
    n = str(n)
    for _ in range(iterations):
        new_n = []
        for k, group in groupby(n):
            counts = len(list(group))
            new_n.append(str(counts))
            new_n.append(k)
        n = "".join(new_n)
    return len(n)


if __name__ == '__main__':
    print(iterate(1321131112))
    print(iterate(1321131112, iterations=50))
