import re
import networkx as nx

with open("inputs.txt") as f:
    inputs = f.read()
with open("test_inputs.txt") as f:
    test_inputs = f.read()

def parse_inputs(inputs):
    lines = inputs.splitlines()
    containers = {}
    for l in lines:
        # get the containing colour
        key = l.split("bags")[0].strip()
        # parse out what it can contain
        contents = l.split("contain")[1].strip()
        if contents == "no other bags.":
            containers[key] = None
        else:
            can_contain = {}
            options = contents.split(",")
            pattern = r"(\d+) (.*) bags?"
            for option in options:
                number, colour = re.search(pattern, option).groups()
                can_contain[colour] = int(number)
            containers[key] = can_contain
    return containers

def build_graph(contents):
    graph = nx.DiGraph({c: v for c, v in contents.items()}) # TODO: this doesn't work yet
    return graph
    
print(build_graph(parse_inputs(test_inputs)))