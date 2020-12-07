import networkx as nx
from utils import utils

# regex = r"(\w+ \w+) bags contain (?:no other bags\.)|(?:(\d+) (\w+ \w+) bag(?:\.|s\.|s, ))+

def build_graph(data):
    DG = nx.DiGraph()
    for line in data:
        line = line.replace("bags", "bag")
        line = line.replace(".", "")
        # Start and end node(s) separated by " contain "
        start_node, ends = line.split(" contain ")
        # split end nodes on ", "
        end_nodes = ends.split(", ")
        for end_node in end_nodes:
            if end_node != "no other bag":
                end_node_data = end_node.split(" ")
                edge_weight = int(end_node_data[0])
                end_node = " ".join(end_node_data[1:])
                # Digraph edges go from end to start to make problem solving easy. Adding 
                # an edge between two nodes adds the two nodes to the node set (no duplicates).
                DG.add_edge(end_node, start_node, weight=edge_weight)
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
    data = utils.get_strs_from_file("data/aoc7_data.txt")
    DG = build_graph(data)
    bag = "shiny gold bag"
    print(f"Part 1 solution: {part_1(DG, bag)}")
    print(f"Part 2 solution: {part_2(DG, bag)}")