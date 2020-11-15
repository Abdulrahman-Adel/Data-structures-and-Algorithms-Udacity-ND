# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:32:36 2020

@author: Abdelrahman
"""

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
        
        
class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
        
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

        return s    


    def insert_with_loop(self, new_value):
        node = self.root

        if node is None:
            self.set_root(value=new_value)

        else:
            new_node = Node(new_value)
            node_inserted = False

            while not node_inserted:
                comparison = self.compare(node, new_node)

                if comparison == 0:
                    node.set_value(new_node)
                    node_inserted = True

                elif comparison < 0:

                    if node.has_left_child():
                        node = node.get_left_child()
                    else:  # No node at left
                        node.set_left_child(new_node)
                        node_inserted = True
                else:

                    if node.has_right_child():
                        node = node.get_right_child()
                    else:
                        node.set_right_child(new_node)
                        node_inserted = True

    def insert_with_recursion(self, value):
        node = self.root

        if node is None:
            self.set_root(value=value)

        else:
            self._insert_with_recursion_rec(node, value)

    def _insert_with_recursion_rec(self, node, value):

        new_node = Node(value)
        comparison = self.compare(node, new_node)

        if comparison == 0:
            node.set_value(new_node)
        elif comparison < 0:  # Left side
            if node.has_left_child():
                self._insert_with_recursion_rec(node=node.get_left_child(), value=value)
            else:  # No node at left
                node.set_left_child(new_node)
        else:
            if node.has_right_child():
                self._insert_with_recursion_rec(node=node.get_left_child(), value=value)
            else:
                node.set_right_child(new_node)

    def search(self, value):
        new_node = Node(value)
        node = self.get_root()
        if node is None:
            return False

        while True:
            comparison = self.compare(node, new_node)
            
            if comparison == 0:
                return True

            elif comparison < 0:
                
                if node.has_left_child():
                    node = node.get_left_child()
                else:  # No node at left
                    return False
            else:

                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
                
    def search_with_rec(self, value):
        node = self.root

        if node is None:
            return None

        else:
            return self._search_rec(node, value)

    def _search_rec(self, node, value):
        new_node = Node(value)
        comparison = self.compare(node, new_node)

        if comparison == 0:
            return True
        elif comparison < 0:  # Left side
            if node.has_left_child():
                return self._search_rec(node=node.get_left_child(), value=value)
            else:
                return False
        else:
            if node.has_right_child():
                return self._search_rec(node=node.get_left_child(), value=value)
            else:
                return False  
            
    def minValueNode( node): 
        current = node 
  
        # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
  
        return current         


    def deleteNode(self,root, key): 
  
        # Base Case 
        if root is None: 
            return root
  
        # If the key to be deleted is smaller than the root's 
        # key then it lies in  left subtree 
        if key < root.value: 
            root.left = self.deleteNode(root.left, key) 
            
            # If the kye to be delete is greater than the root's key 
            # then it lies in right subtree 
        elif(key > root.value): 
             root.right = self.deleteNode(root.right, key) 
                
             # If key is same as root's key, then this is the node 
             # to be deleted 
        else: 
          
            # Node with only one child or no child 
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  
              
            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 
  
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            temp = self.minValueNode(root.right) 
  
            # Copy the inorder successor's content to this node 
            root.value = temp.value 
            
            # Delete the inorder successor 
            root.right = self.deleteNode(root.right , temp.value) 
  
  
        return root 
                      
                
tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)

print(tree)

tree.deleteNode(tree.get_root(),2)

print(tree)
                
                
                
                