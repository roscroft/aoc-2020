import re
import networkx as nx
from utils import utils

def build_graph(data):
    DG = nx.DiGraph()
    for line in data:
        start_node = re.match(r"(\w+ \w+) bags", line).group(1)
        for end_node in re.findall(r"(\d+) (\w+ \w+) bag", line):
            DG.add_edge(end_node[1], start_node, weight=int(end_node[0]))
    return DG

def part_1(DG, bag):
    return sum(1 for _ in nx.dfs_postorder_nodes(DG, source=bag)) - 1

def part_2(DG, bag):
    for node in list(nx.topological_sort(DG)):
        DG.nodes[node]["weight"] = sum([DG[pred][node]["weight"]*(DG.nodes[pred].get("weight") + 1) for pred in DG.predecessors(node)])
    return DG.nodes[bag]["weight"]

if __name__ == "__main__":
    DG = build_graph(utils.get_strs_from_file(f"data/aoc7_data.txt"))
    print(f"Part 1 solution: {part_1(DG, 'shiny gold')}")
    print(f"Part 2 solution: {part_2(DG, 'shiny gold')}")