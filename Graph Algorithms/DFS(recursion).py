# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:20:08 2021

@author: Abdelrahman
"""

class Node:
    def __init__(self,val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph():
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
            
            
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 

graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)           


def dfs_recursion(node,visited):
    
    if node is None:
        return False
    
    visited[node.value] = True
    print(node.value)
    
    for child in node.children:
        if child.value not in visited:
            dfs_recursion(child,visited)
            
def dfs_recursion_start(start_node):
    visited = {}
    dfs_recursion(start_node, visited)
    

dfs_recursion_start(nodeG)    
            