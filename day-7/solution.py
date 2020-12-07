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
    return G.reverse() # directions need to point towards outer bags

def find_outer_bags(graph, root):
    outer_bags = []
    for node in graph:
        if graph.out_degree(node)==0 and nx.has_path(graph, root, node): #it's a leaf, so one of the outer bags
            for p in nx.shortest_simple_paths(graph, root, node):
                for n in p[1:]:
                    outer_bags.append(n)
    return set(outer_bags)

def count_total_bags(graph, root):
    bags = 0
    for node in graph:
        if graph.out_degree(node)==0 and nx.has_path(graph, root, node): #it's a leaf, so one of the outer bags
            for p in nx.shortest_simple_paths(graph, root, node):
                print(p)
                if len(p) > 1:
                    print(graph[p[0]][p[1]]['weight'])
                    #bags += sum([graph[p[i]][p[i+1]]['weight'] for i in range(len(p)-1)])
    return bags
    
graph = build_graph(parse_inputs(inputs))
test_graph = build_graph(parse_inputs(test_inputs))
print(find_outer_bags(test_graph, "shiny gold"))
assert len(find_outer_bags(test_graph, "shiny gold")) == 4

print(len(find_outer_bags(graph, "shiny gold")))

test_graph_2 = build_graph(parse_inputs(test_inputs_2))
print(count_total_bags(test_graph_2, "shiny gold"))
assert count_total_bags(test_graph_2, "shiny gold") == 126