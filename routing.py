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

P,D = dijkstra_generalized(graph, source = 'u', weight='cost')

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
 
 """
 Shortest paths via Dijkstra's algorithm,
 consistent with pseudocode on Slide 5-14.
 """
 import math
 # Definitions consistent with Kurose & Ross
 u = source
 def c(x, y):
     return graph[x][y][weight]
 N = frozenset(graph.nodes())
 NPrime = {u} # i.e. "set([u])"
 D = dict.fromkeys(N, math.inf)
 # Initialization
 for v in N:
     if graph.has_edge(u, v):
         D[v] = c(u, v)
         P[v] = [u] #add an entry to the predecessor dictionary, children nodes with a source
         
         D[u] = 0 # over-write inf entry for source
 # Loop
 while NPrime != N:
     candidates = {w: D[w] for w in N if w not in NPrime}
     w, Dw = min(candidates.items(), key=lambda item: item[1])
     NPrime.add(w)
 for v in graph[w]:
     if v not in NPrime:
         DvNew = D[w] + c(w, v)
         if DvNew < D[v]:
             D[v] = DvNew
             P[v] = [w] #add a current node with its predecessor
 return D
