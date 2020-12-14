import re
import networkx as nx
from networkx.algorithms.shortest_paths import weighted

with open("inputs.txt") as f:
    inputs = f.read()
with open("test_inputs.txt") as f:
    test_inputs = f.read()
with open("test_inputs_2.txt") as f:
    test_inputs_2 = f.read()

def parse_inputs(inputs):
    lines = inputs.splitlines()
    containers = {}
    for l in lines:
        # get the containing colour
        key = l.split("bags")[0].strip()
        # parse out what it can contain
        contents = l.split("contain")[1].strip()
        if contents == "no other bags.":
            containers[key] = {}
        else:
            can_contain = {}
            options = contents.split(",")
            pattern = r"(\d+) (.*) bag"
            for option in options:
                number, colour = re.search(pattern, option).groups()
                can_contain[colour] = {"weight": int(number)}
            containers[key] = can_contain
    return containers

def build_graph(contents):
    G = nx.DiGraph(contents)
    return G

def find_outer_bags(graph, root):
    rev_graph = graph.reverse()
    predecessors = nx.dfs_predecessors(rev_graph, root)
    return len(predecessors)

def count_total_bags(graph, root):
    # recursive search of neighbours from root node
    def search(node):
        count = 1
        for n in graph.neighbors(node):
            count += graph[node][n]["weight"] * search(n)
        return count
    return search(root) - 1
    
graph = build_graph(parse_inputs(inputs))
test_graph = build_graph(parse_inputs(test_inputs))
print(find_outer_bags(test_graph, "shiny gold"))
assert find_outer_bags(test_graph, "shiny gold") == 4

print(find_outer_bags(graph, "shiny gold"))

test_graph_2 = build_graph(parse_inputs(test_inputs_2))
print(count_total_bags(test_graph_2, "shiny gold"))
assert count_total_bags(test_graph_2, "shiny gold") == 126

print(count_total_bags(graph, "shiny gold"))