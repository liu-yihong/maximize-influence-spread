# Created by Yihong Liu at 2021/4/20
# -*- coding: utf-8 -*-
"""
This script ...
"""
import networkx as nx
import pandas as pd

# adj_list = pd.read_csv("data/facebook_combined.txt.gz",
#                        compression='gzip',
#                        skiprows=4,
#                        delimiter='\t',
#                        names=['FROM', 'TO'])

# read email data from http://networkrepository.com/email-dnc.php
adj_list = pd.read_csv('data/email-dnc.edges',
                       skiprows=0,
                       delimiter=',',
                       names=['FROM', 'TO', 'TIME'])

# count duplicates
count_duplicates = adj_list.groupby(['FROM', 'TO'], as_index=False).size().sort_values(by='size')

# this is a multi-graph
collab_multigraph = nx.from_pandas_edgelist(adj_list[['FROM', 'TO']],
                                            source='FROM',
                                            target='TO',
                                            create_using=nx.MultiGraph)
# check # edges between nodes
[[u[0], u[1], collab_multigraph.number_of_edges(u[0], u[1])] for u in set(collab_multigraph.edges())]

directed_graph = nx.DiGraph()

for edge in set(collab_multigraph.edges()):
    # get statistics
    u, v = edge[0], edge[1]
    num_edges_u_v = collab_multigraph.number_of_edges(u, v)
    degree_u = collab_multigraph.degree(u)
    degree_v = collab_multigraph.degree(v)
    # construct graphs for influence models
    directed_graph.add_edge(u, v, c=num_edges_u_v, weight=num_edges_u_v / degree_v, du=degree_u, dv=degree_v)
    directed_graph.add_edge(v, u, c=num_edges_u_v, weight=num_edges_u_v / degree_u, du=degree_v, dv=degree_u)

