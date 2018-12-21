# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:48:41 2018

@author: CXL
"""

graph = {}
graph["yuepu"] = {}
graph["yuepu"] ["changpian"] = 5
graph["yuepu"] ["haibao"] = 0

graph["changpian"] = {}
graph["changpian"] ["jita"] = 15
graph["changpian"] ["jiazigu"] = 20

graph["haibao"] = {}
graph["haibao"]["jita"] = 30
graph["haibao"] ["jiazigu"] = 35

graph["jita"] = {}
graph["jita"]["gangqin"] = 20

graph["jiazigu"] = {}
graph["jiazigu"]["gangqin"] = 10

graph ["gangqin"] = {}


infinity = float ("inf")
costs = {}
costs["changpian"] = 5
costs["haibao"] = 0
costs["jita"] = infinity     
costs["jiazigu"] = infinity
costs["gangqin"] = infinity


parents = {}
parents["changpian"] = "yuepu"
parents["haibao"] = "yuepu"
parents["jita"] =None
parents["jiazigu"] =None
parents["gangqin"] = None
processed = []  


def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost <lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node


def find_shortest_path():
    node = "gangqin" 
    shortest_path = ["gangqin"]  
    while parents[node] != "yuepu": 
        shortest_path.append(parents[node])  
        node = parents[node]   
    shortest_path.append("yuepu")   
    return shortest_path
    

if __name__=="__main__":
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost=costs[node]
        neighbors=graph[node]
        for n in neighbors.keys():
            new_cost=cost+neighbors[n]
            if costs[n]>new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    shortest_path = find_shortest_path()  
    shortest_path.reverse()  
    print("最短路径:")
    print(shortest_path)    
    print("节点：开销")
    print(costs)
    print("节点：父亲点")
    print(parents)
