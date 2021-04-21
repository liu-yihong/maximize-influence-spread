# Created by Yihong Liu at 2021/4/21
# -*- coding: utf-8 -*-
"""
This script ...
"""

import networkx as nx
import numpy as np
import random
from joblib import Parallel, delayed


def generate_individual_threshold(nodes_set):
    dict_individual_threshold = dict()
    for u in nodes_set:
        dict_individual_threshold[u] = np.random.rand()
    return dict_individual_threshold


def generate_edges_probability(edges_set, low=0.01, high=0.1):
    dict_edges_probability = dict()
    for e in edges_set:
        dict_edges_probability[e] = np.random.uniform(low, high)
    return dict_edges_probability


def generate_activating_probability(p, c):
    return 1 - np.power(1 - p, c)


def begin_diffusion(initial_set, underlying_graph, max_iter, mode, p_cascade=0.01):
    set_all_nodes = set(underlying_graph.nodes())
    set_active_nodes = initial_set.copy()
    set_inactive_nodes = set_all_nodes - set_active_nodes
    # check arguments
    assert len(initial_set) != 0, "The Initial Set CANNOT be Empty!"
    assert initial_set.issubset(set_all_nodes), "The Initial Set Must Be Covered By the Underlying Graph!"
    assert mode in {'linear threshold', 'independent cascade', 'weighted cascade'}, 'Mode Not Implemented!'
    # determine the underlying diffusion process
    if mode == 'linear threshold':
        # generate randomly individual threshold
        dict_individual_threshold = generate_individual_threshold(nodes_set=set_all_nodes)
        for i in range(max_iter):
            list_nodes_await_to_be_activated = []
            for u in set_inactive_nodes:
                neighbor_of_u = set(underlying_graph.predecessors(u))  # TODO: check predecessor or successor
                active_neighbor_of_u = set_active_nodes.intersection(neighbor_of_u)
                cumulative_weight_of_u = sum(
                    [underlying_graph.get_edge_data(v, u)['weight'] for v in active_neighbor_of_u])
                if cumulative_weight_of_u > dict_individual_threshold[u]:
                    list_nodes_await_to_be_activated.append(u)
            if len(list_nodes_await_to_be_activated) == 0:
                print("MODE: linear threshold - EARLY TERMINATION")
                break
            set_active_nodes.update(list_nodes_await_to_be_activated)
            set_inactive_nodes.difference_update(set(list_nodes_await_to_be_activated))
    elif mode == 'independent cascade':
        activation_history = []
        # dict_edges_probability = generate_edges_probability(edges_set=underlying_graph.edges())
        for i in range(max_iter):
            activation_attempts = []
            for u in set_active_nodes:
                neighbor_of_u = set(underlying_graph.successors(u))  # TODO: check successor or all neighbor?
                inactive_neighbor_of_u = set_inactive_nodes.intersection(neighbor_of_u)
                for v in inactive_neighbor_of_u:
                    if (u, v) in activation_history:  # only a single chance
                        continue
                    activation_attempts.append((u, v))
            for t in activation_attempts:
                u, v = t[0], t[1]
                if v in set_inactive_nodes:
                    activation_history.append((u, v))
                    c = underlying_graph.get_edge_data(u, v)['c']
                    p = p_cascade  # dict_edges_probability[(u, v)]
                    activating_probability = generate_activating_probability(p, c)
                    flip_a_coin = np.random.binomial(n=1, p=activating_probability)
                    if flip_a_coin == 1:
                        set_active_nodes.add(v)
                        set_inactive_nodes.remove(v)
            if len(activation_attempts) == 0:
                print("MODE: independent cascade - EARLY TERMINATION")
                break
    elif mode == 'weighted cascade':
        activation_history = []
        for i in range(max_iter):
            activation_attempts = []
            for u in set_active_nodes:
                neighbor_of_u = set(underlying_graph.successors(u))  # TODO: check successor or all neighbor?
                inactive_neighbor_of_u = set_inactive_nodes.intersection(neighbor_of_u)
                for v in inactive_neighbor_of_u:
                    if (u, v) in activation_history:  # only a single chance
                        continue
                    activation_attempts.append((u, v))
            for t in activation_attempts:
                u, v = t[0], t[1]
                if v in set_inactive_nodes:
                    activation_history.append((u, v))
                    c = underlying_graph.get_edge_data(u, v)['c']
                    p = 1 / underlying_graph.get_edge_data(u, v)['dv']  # dict_edges_probability[(u, v)]
                    activating_probability = generate_activating_probability(p, c)
                    flip_a_coin = np.random.binomial(n=1, p=activating_probability)
                    if flip_a_coin == 1:
                        set_active_nodes.add(v)
                        set_inactive_nodes.remove(v)
            if len(activation_attempts) == 0:
                print("MODE: weighted cascade - EARLY TERMINATION")
                break
    return initial_set, len(set_active_nodes)


def random_draw(underlying_graph, k):
    set_all_nodes = set(underlying_graph.nodes())
    initial_set = random.sample(set_all_nodes, k)
    return initial_set


def degree_heuristic(underlying_graph, k):
    # here the underlying graph is the multigraph
    list_node_and_degree = []
    for u in underlying_graph.nodes():
        du = underlying_graph.degree(u)
        list_node_and_degree.append([u, du])
    array_node_and_degree = np.array(list_node_and_degree)
    array_node_and_degree = array_node_and_degree[array_node_and_degree[:, 1].argsort()]
    return set(array_node_and_degree[-k:, 0])


def centrality_heuristic(underlying_graph, k):
    # here the underlying graph is the multigraph
    dict_closeness_for_nodes = nx.closeness_centrality(underlying_graph)
    array_node_and_closeness = np.array(list(dict_closeness_for_nodes.items()))
    array_node_and_closeness = array_node_and_closeness[array_node_and_closeness[:, 1].argsort()]
    return set(array_node_and_closeness[-k:, 0])


def hill_climbing_greedy(underlying_graph, k, max_iter, p_cascade, mode):
    set_all_nodes = set(underlying_graph.nodes())
    greedy_initial_set = set()
    for iter_cnt in range(k):
        parallelized_diffusion_result = \
            Parallel(n_jobs=-1)(delayed(begin_diffusion)(greedy_initial_set.union({u}),
                                                         underlying_graph=underlying_graph,
                                                         max_iter=max_iter,
                                                         mode=mode,
                                                         p_cascade=p_cascade) for u in set_all_nodes)
        array_parallelized_diffusion_result = np.array(parallelized_diffusion_result)
        array_parallelized_diffusion_result = array_parallelized_diffusion_result[
            array_parallelized_diffusion_result[:, 1].argsort()]
        greedy_initial_set = array_parallelized_diffusion_result[-1, 0]
    return greedy_initial_set
