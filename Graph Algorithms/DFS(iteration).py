# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:47:27 2021

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

 
def DFS(root_node,target_value):
    
    if root_node.value == target_value:
        return root_node
    
    node = root_node
    
    stack = [root_node.value]
    seen = [root_node.value]
    
    while len(stack) > 0:
        
        for child in node.children:
            flag = True #flag for seen children
            
            if child.value not in seen:
                node = child
                stack.append(child.value)
                seen.append(child.value)
                flag = False
                
                if child.value == target_value:
                    print("Target value found!")
                    return child
               
                break  
            
        if flag:
            stack.pop()
            if len(stack) > 0:
                for child_previous in node.children:
                    if child_previous.value == stack[-1]:
                        node = child_previous
                        break
                
        
    return -1

print(DFS(graph1.nodes[2], 'X'))

assert nodeA == DFS(nodeS, 'A')
assert nodeS == DFS(nodeP, 'S')
assert nodeR == DFS(nodeH, 'R')