# Created by Yihong Liu at 2021/4/21
# -*- coding: utf-8 -*-
"""
This script ...
"""

import random

import networkx as nx
import numpy as np
import pandas as pd
from IPython.display import clear_output
from joblib import Parallel, delayed
from matplotlib import pyplot as plt
from tqdm import tqdm


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
        # with trange(max_iter) as t:
        #     for i in t:
        #         t.set_description("MODE: linear threshold ITER: %i" % i)
        #         list_nodes_await_to_be_activated = []
        #         for u in set_inactive_nodes:
        #             neighbor_of_u = set(underlying_graph.predecessors(u))  # TODO: check predecessor or successor
        #             active_neighbor_of_u = set_active_nodes.intersection(neighbor_of_u)
        #             cumulative_weight_of_u = sum(
        #                 [underlying_graph.get_edge_data(v, u)['weight'] for v in active_neighbor_of_u])
        #             if cumulative_weight_of_u > dict_individual_threshold[u]:
        #                 list_nodes_await_to_be_activated.append(u)
        #         if len(list_nodes_await_to_be_activated) == 0:  # TODO: check early termination condition
        #             # print("MODE: linear threshold - EARLY TERMINATION")
        #             break
        #         set_active_nodes.update(list_nodes_await_to_be_activated)
        #         set_inactive_nodes.difference_update(set(list_nodes_await_to_be_activated))
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
                # print("MODE: linear threshold - EARLY TERMINATION")
                break
            set_active_nodes.update(list_nodes_await_to_be_activated)
            set_inactive_nodes.difference_update(set(list_nodes_await_to_be_activated))
    elif mode == 'independent cascade':
        activation_history = []
        # dict_edges_probability = generate_edges_probability(edges_set=underlying_graph.edges())
        # with trange(max_iter) as t1:
        #     for i in t1:
        #         t1.set_description("MODE: independent cascade ITER: %i" % i)
        #         activation_attempts = []
        #         for u in set_active_nodes:
        #             neighbor_of_u = set(underlying_graph.successors(u))  # TODO: check successor or all neighbor?
        #             inactive_neighbor_of_u = set_inactive_nodes.intersection(neighbor_of_u)
        #             for v in inactive_neighbor_of_u:
        #                 if (u, v) in activation_history:  # only a single chance
        #                     continue
        #                 activation_attempts.append((u, v))
        #         for t in activation_attempts:
        #             u, v = t[0], t[1]
        #             if v in set_inactive_nodes:
        #                 activation_history.append((u, v))
        #                 c = underlying_graph.get_edge_data(u, v)['c']
        #                 p = p_cascade  # dict_edges_probability[(u, v)]
        #                 activating_probability = generate_activating_probability(p, c)
        #                 flip_a_coin = np.random.binomial(n=1, p=activating_probability)
        #                 if flip_a_coin == 1:
        #                     set_active_nodes.add(v)
        #                     set_inactive_nodes.remove(v)
        #         if len(activation_attempts) == 0:  # TODO: check early termination condition
        #             # print("MODE: independent cascade - EARLY TERMINATION")
        #             break

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
                # print("MODE: independent cascade - EARLY TERMINATION")
                break
    elif mode == 'weighted cascade':
        activation_history = []
        # with trange(max_iter) as t1:
        #     for i in t1:
        #         t1.set_description("MODE: weighted cascade ITER: %i" % i)
        #         activation_attempts = []
        #         for u in set_active_nodes:
        #             neighbor_of_u = set(underlying_graph.successors(u))  # TODO: check successor or all neighbor?
        #             inactive_neighbor_of_u = set_inactive_nodes.intersection(neighbor_of_u)
        #             for v in inactive_neighbor_of_u:
        #                 if (u, v) in activation_history:  # only a single chance
        #                     continue
        #                 activation_attempts.append((u, v))
        #         for t in activation_attempts:
        #             u, v = t[0], t[1]
        #             if v in set_inactive_nodes:
        #                 activation_history.append((u, v))
        #                 c = underlying_graph.get_edge_data(u, v)['c']
        #                 p = 1 / underlying_graph.get_edge_data(u, v)['dv']  # dict_edges_probability[(u, v)]
        #                 activating_probability = generate_activating_probability(p, c)
        #                 flip_a_coin = np.random.binomial(n=1, p=activating_probability)
        #                 if flip_a_coin == 1:
        #                     set_active_nodes.add(v)
        #                     set_inactive_nodes.remove(v)
        #         if len(activation_attempts) == 0:  # TODO: check early termination condition
        #             # print("MODE: weighted cascade - EARLY TERMINATION")
        #             break
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
                # print("MODE: weighted cascade - EARLY TERMINATION")
                break
    return initial_set, len(set_active_nodes)


def random_draw(underlying_graph, k):
    # # here the underlying graph can be multigraph or directed graph
    set_all_nodes = set(underlying_graph.nodes())
    initial_set = random.sample(set_all_nodes, k)
    return set(initial_set)


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
    return set(array_node_and_closeness[-k:, 0].astype(int)), array_node_and_closeness


def hill_climbing_greedy(underlying_graph, k, max_iter, exp_iter, p_cascade=0.01, mode='linear threshold'):
    set_all_nodes = set(underlying_graph.nodes())
    greedy_initial_set = set()
    dict_tracking = dict()
    for iter_cnt1 in range(k):
        set_valid_nodes = set_all_nodes - greedy_initial_set
        dict_diffusion_result_pool = dict()
        for iter_cnt2 in range(exp_iter):
            parallelized_diffusion_result = \
                Parallel(n_jobs=-1, verbose=1)(delayed(begin_diffusion)(greedy_initial_set.union({u}),
                                                                        underlying_graph=underlying_graph,
                                                                        max_iter=max_iter,
                                                                        mode=mode,
                                                                        p_cascade=p_cascade) for u in set_valid_nodes)
            for element in parallelized_diffusion_result:
                focal_set = element[0]
                focal_frozenset = frozenset(list(focal_set))
                if focal_frozenset not in dict_diffusion_result_pool.keys():
                    dict_diffusion_result_pool[focal_frozenset] = 0
                dict_diffusion_result_pool[focal_frozenset] += element[1]
            # array_parallelized_diffusion_result = np.array(parallelized_diffusion_result)
            # array_parallelized_diffusion_result = array_parallelized_diffusion_result[
            #    array_parallelized_diffusion_result[:, 1].argsort()]
        # greedy_initial_set = array_parallelized_diffusion_result[-1, 0]
        greedy_initial_frozenset = max(dict_diffusion_result_pool, key=dict_diffusion_result_pool.get)
        greedy_initial_set = set(list(greedy_initial_frozenset))
        dict_tracking[iter_cnt1 + 1] = greedy_initial_set
    clear_output(wait=True)
    return greedy_initial_set, dict_tracking


def read_data():
    # read email data from http://networkrepository.com/email-dnc.php
    adj_list = pd.read_csv('data/email-dnc.edges',
                           skiprows=0,
                           delimiter=',',
                           names=['FROM', 'TO', 'TIME'])
    # this is a multigraph
    multigraph = nx.from_pandas_edgelist(adj_list[['FROM', 'TO']],
                                         source='FROM',
                                         target='TO',
                                         create_using=nx.MultiGraph)
    # this is the directed graph, derived from the multigraph
    directed_graph = nx.DiGraph()

    for edge in set(multigraph.edges()):
        # get statistics
        u, v = edge[0], edge[1]
        num_edges_u_v = multigraph.number_of_edges(u, v)
        degree_u = multigraph.degree(u)
        degree_v = multigraph.degree(v)
        # construct graphs for influence models
        directed_graph.add_edge(u, v, c=num_edges_u_v, weight=num_edges_u_v / degree_v, du=degree_u, dv=degree_v)
        directed_graph.add_edge(v, u, c=num_edges_u_v, weight=num_edges_u_v / degree_u, du=degree_v, dv=degree_u)

    return multigraph, directed_graph


def experiments_and_plot(multi_graph, directed_graph, max_k=10, num_exp=500, max_iter=500, mode='linear threshold',
                         p_cascade=0.01, exp_iter=20):
    temp_list1 = []
    temp_list2 = []
    temp_list3 = []
    temp_list4 = []
    # precompute all the sets for hill-climbing greedy and centrality heuristic
    _, list_centrality = centrality_heuristic(multi_graph, k=max_k)
    _, dict_track = hill_climbing_greedy(directed_graph,
                                         k=max_k,
                                         max_iter=max_iter,
                                         exp_iter=exp_iter,
                                         p_cascade=p_cascade,
                                         mode=mode)

    # experiments
    for k in tqdm(range(max_k)):
        target_set1 = random_draw(multi_graph, k=k + 1)
        target_set2 = degree_heuristic(multi_graph, k=k + 1)
        target_set3 = set(list_centrality[-(k + 1):, 0].astype(int))
        target_set4 = dict_track[k + 1]

        parallelized_diffusion_result1 = \
            Parallel(n_jobs=-1, verbose=1)(delayed(begin_diffusion)(target_set1,
                                                                    underlying_graph=directed_graph,
                                                                    max_iter=max_iter,
                                                                    mode=mode,
                                                                    p_cascade=p_cascade) for l in range(num_exp))
        clear_output(wait=True)
        parallelized_diffusion_result2 = \
            Parallel(n_jobs=-1, verbose=1)(delayed(begin_diffusion)(target_set2,
                                                                    underlying_graph=directed_graph,
                                                                    max_iter=max_iter,
                                                                    mode=mode,
                                                                    p_cascade=p_cascade) for l in range(num_exp))
        clear_output(wait=True)
        parallelized_diffusion_result3 = \
            Parallel(n_jobs=-1, verbose=1)(delayed(begin_diffusion)(target_set3,
                                                                    underlying_graph=directed_graph,
                                                                    max_iter=max_iter,
                                                                    mode=mode,
                                                                    p_cascade=p_cascade) for l in range(num_exp))
        clear_output(wait=True)
        parallelized_diffusion_result4 = \
            Parallel(n_jobs=-1, verbose=1)(delayed(begin_diffusion)(target_set4,
                                                                    underlying_graph=directed_graph,
                                                                    max_iter=max_iter,
                                                                    mode=mode,
                                                                    p_cascade=p_cascade) for l in range(num_exp))
        clear_output(wait=True)
        temp_list1.append(np.array(parallelized_diffusion_result1)[:, 1])
        temp_list2.append(np.array(parallelized_diffusion_result2)[:, 1])
        temp_list3.append(np.array(parallelized_diffusion_result3)[:, 1])
        temp_list4.append(np.array(parallelized_diffusion_result4)[:, 1])

    # plot
    S1 = np.array(temp_list1).astype(float)
    S2 = np.array(temp_list2).astype(float)
    S3 = np.array(temp_list3).astype(float)
    S4 = np.array(temp_list4).astype(float)

    mu1 = S1.mean(axis=1)
    sigma1 = S1.std(axis=1)

    mu2 = S2.mean(axis=1)
    sigma2 = S2.std(axis=1)

    mu3 = S3.mean(axis=1)
    sigma3 = S3.std(axis=1)

    mu4 = S4.mean(axis=1)
    sigma4 = S4.std(axis=1)

    fig, ax = plt.subplots(1)

    ax.plot(np.arange(max_k) + 1, mu1, lw=2, label='random draw', color='blue')
    ax.fill_between(np.arange(max_k) + 1, mu1 + sigma1, mu1 - sigma1, facecolor='blue', alpha=0.5)

    ax.plot(np.arange(max_k) + 1, mu2, lw=2, label='degree heuristic', color='yellow')
    ax.fill_between(np.arange(max_k) + 1, mu2 + sigma2, mu2 - sigma2, facecolor='yellow', alpha=0.5)

    ax.plot(np.arange(max_k) + 1, mu3, lw=2, label='centrality heuristic', color='pink')
    ax.fill_between(np.arange(max_k) + 1, mu3 + sigma3, mu3 - sigma3, facecolor='pink', alpha=0.5)

    ax.plot(np.arange(max_k) + 1, mu4, lw=2, label='hill-climbing greedy', color='orangered')
    ax.fill_between(np.arange(max_k) + 1, mu4 + sigma4, mu4 - sigma4, facecolor='orangered', alpha=0.5)

    ax.set_title(r'Final Size: empirical $\mu$ and $\pm \sigma$ interval')
    ax.legend(loc='upper left')
    ax.set_xlabel('Size of Initial Target Set')
    ax.set_ylabel('Size of Final Active Size')
    ax.grid()

    pass


def main():
    multigraph, directed_graph = read_data()

    target_set1 = random_draw(multigraph, k=3)
    target_set2 = degree_heuristic(multigraph, k=3)
    target_set3, list_centrality = centrality_heuristic(multigraph, k=3)
    target_set4, dict_track = hill_climbing_greedy(directed_graph, k=3, max_iter=300, exp_iter=20, p_cascade=0.01,
                                                   mode='independent cascade')


if __name__ == "__main__":
    main()
