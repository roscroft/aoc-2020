import re
import networkx as nx
from utils import utils

# regex = r"(\w+ \w+) bags contain (?:(?:no other bags\.)|(?:(\d+) (\w+ \w+) bag(?:\.|, |s\.|s, ))+)"

def build_graph(data):
    DG = nx.DiGraph()
    start_regex = re.compile(r"(\w+ \w+) bags")
    end_regex = re.compile(r"(\d+) (\w+ \w+) bag")
    for line in data:
        # Start regex captures initial bag (no number on first bag)
        start_node = start_regex.match(line).group(1)
        # End regex captures later bags (with numbers, findall to get all)
        end_nodes = end_regex.findall(line)
        # end_nodes is a list of matches of the form [(weight, color)]
        for end_node in end_nodes:
            DG.add_edge(end_node[1], start_node, weight=int(end_node[0]))
    return DG

def part_1(DG, bag):
    dfs = nx.dfs_postorder_nodes(DG, source=bag)
    # DFS includes source node
    return sum(1 for _ in dfs) - 1

def part_2(DG, bag):
    topo_sort = list(nx.topological_sort(DG))
    for node in topo_sort:
        node_weight = 0
        for predecessor in DG.predecessors(node):
            pred_edge_weight = DG[predecessor][node]["weight"]
            pred_node_weight = DG.nodes[predecessor].get("weight")
            # Add the sum of edge weights plus the edge weights multiplied by the node weights
            node_weight += pred_edge_weight
            node_weight += pred_node_weight*pred_edge_weight if pred_node_weight else 0
        DG.nodes[node]["weight"] = node_weight
    return DG.nodes[bag]["weight"]

if __name__ == "__main__":
    day = 7
    data = utils.get_strs_from_file(f"data/aoc{day}_data.txt")
    DG = build_graph(data)
    bag = "shiny gold"
    print(f"Part 1 solution: {part_1(DG, bag)}")
    print(f"Part 2 solution: {part_2(DG, bag)}")