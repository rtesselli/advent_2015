from pathlib import Path
import networkx as nx


def load_commands() -> dict[str, str]:
    lines = Path("data/day07.txt").read_text().splitlines()
    out = {}
    for line in lines:
        op, key = line.split(" -> ")
        out[key] = op
    return out


def get_op_graph(ops: dict[str, str]) -> nx.DiGraph[str]:
    graph = nx.DiGraph()
    for target, op in ops.items():
        if "AND" in op:
            left, right = op.split(" AND ")
            if left != "1":
                graph.add_edge(left, target)
            graph.add_edge(right, target)
        elif "OR" in op:
            left, right = op.split(" OR ")
            graph.add_edge(left, target)
            graph.add_edge(right, target)
        elif "SHIFT" in op:
            var = op.split(" ")[0]
            graph.add_edge(var, target)
        elif "NOT" in op:
            var = op.split(" ")[-1]
            graph.add_edge(var, target)
        elif op.isalpha():
            graph.add_edge(op, target)
    return graph


def compute(ops: dict[str, str]) -> dict[str, int]:
    graph = get_op_graph(ops)
    results = {}
    for key in nx.topological_sort(graph):
        op = ops[key]
        if "AND" in op:
            left, right = op.split(" AND ")
            if left == "1":
                results[key] = 1 & results[right]
            else:
                results[key] = results[left] & results[right]
        elif "OR" in op:
            left, right = op.split(" OR ")
            results[key] = results[left] | results[right]
        elif "LSHIFT" in op:
            left, right = op.split(" LSHIFT ")
            results[key] = results[left] << int(right)
        elif "RSHIFT" in op:
            left, right = op.split(" RSHIFT ")
            results[key] = results[left] >> int(right)
        elif "NOT" in op:
            var = op.split(" ")[-1]
            results[key] = ~results[var]
        else:
            if op.isnumeric():
                results[key] = int(op)
            else:
                results[key] = results[op]
    for k, v in results.items():
        results[k] = v % 65536
    return results


if __name__ == '__main__':
    commands = load_commands()
    values = compute(commands)
    print(values["a"])
