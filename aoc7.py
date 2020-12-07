import networkx as nx
import utils

def build_graph(data):
    DG = nx.DiGraph()
    for line in data:
        # Takes in a line of data of the form: r"(\w+ \w+) bags contain (?:(\d+) (\w+ \w+) bag(?:.|s.|s, ))+"
        start_node, ends = line.split(" contain ")
        start_node = start_node.replace("bags", "bag")
        DG.add_node(start_node)
        # ends is of the form (no other bags.)|(<number> <color> <color> bag(s?)(.|, ))+
        # split ends on ,
        end_nodes = ends.split(", ")
        for end_node in end_nodes:
            if end_node != "no other bags.":
                end_node = end_node.replace(".", "")
                end_node = end_node.replace("bags", "bag")
                # No weight is more than 9
                edge_weight = int(end_node[0])
                end_node = end_node[2:]
                DG.add_node(end_node)
                DG.add_edge(end_node, start_node, weight=edge_weight)
    return DG

def part_1(DG):
    dfs = nx.dfs_postorder_nodes(DG, source="shiny gold bag")
    # for some reason the DFS includes the source node
    return sum(1 for _ in dfs) - 1

def part_2(DG):
    topo_sort = list(nx.topological_sort(DG))
    for node in topo_sort:
        node_weight = 0
        for predecessor in DG.predecessors(node):
            # Add edge weights
            node_weight += DG[predecessor][node]["weight"]
            # Add predecessor node weights * edge weights. Trust me
            pred_node_weight = DG.nodes[predecessor].get("weight")
            if pred_node_weight:
                node_weight += pred_node_weight*DG[predecessor][node]["weight"]
        DG.nodes[node]["weight"] = node_weight
    return DG.nodes["shiny gold bag"]["weight"]

if __name__ == "__main__":
    data = utils.get_strs_from_file("aoc7_data.txt")
    DG = build_graph(data)
    print(f"Part 1 solution: {part_1(DG)}")
    print(f"Part 2 solution: {part_2(DG)}")