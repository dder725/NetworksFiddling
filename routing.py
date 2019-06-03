# -*- coding: utf-8 -*-
import json
import os
from pprint import pprint # "pretty print"
filename = os.path.join('.', 'KuroseRoss5-16.json') # modify as required
netjson = json.load(open(filename))
pprint(netjson)

import networkx as nx # saves typing later on
graph = nx.Graph()
graph.add_nodes_from((
 (node['id'], node['properties']) # node-attributes
 for node in netjson['nodes']))
graph.add_edges_from((
 (link['source'], link['target'], {'cost': link['cost']}) # source-target-attributes
 for link in netjson['links']))
for node, data in graph.nodes(data=True):
 pprint((node, data))
for source, target, data in graph.edges(data=True):
     pprint((source, target, data)) # edges & attributes
for node in graph:
 pprint((node, dict(graph[node]))) # neighbours

node_positions = nx.spring_layout(graph)
edge_label_positions = nx.draw_networkx_edge_labels(
        graph,
        pos=node_positions,
        node_labels=nx.get_node_attributes(graph, name='name'),
        edge_labels=nx.get_edge_attributes(graph, name='cost'))
nx.draw_networkx(graph, pos=node_positions)
pprint("x")
def forwarding(predecessor, source):
    """ 
    Compute a forwarding table from a predecessor list. 
    """
    pass  # TODO
    
    
def dijkstra_generalized(graph, source, weight='weight', 
                         infinity=None, 
                         plus=None,
                         less=None,
                         min=None):
    """
    Least-cost or widest paths via Dijkstra's algorithm.
    """
    pass  # TODO: Please work from Lab 1 code
