# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:52:43 2021

@author: Abdelrahman
"""

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)
            
            
            
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)


#from collections import deque

def BFS(start_node,target_value):
    queue = []
    seen_values = [start_node.value]
    
    queue.append(start_node)
    
    if start_node.value == target_value:
        return start_node

    node = start_node

    while len(queue) > 0:
        for child in node.children:
            
            if child.value not in seen_values:
                seen_values.append(child.value)
                queue.append(child)
                
                if child.value == target_value:
                    return child
                
        del queue[0]
        if len(queue) > 0:
            node = queue[0]
        

    return -1
    
    
assert nodeA == BFS(nodeS, 'A')
assert nodeS == BFS(nodeP, 'S')
assert nodeR == BFS(nodeH, 'R')

