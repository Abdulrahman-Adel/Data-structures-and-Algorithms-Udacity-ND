# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:37:47 2020

@author: Abdelrahman
"""

basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}

def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie
    
    for char in word:
        if char not in current_node:
            return False
        
        current_node = current_node[char]
    
    return current_node['word_end']


# Test words
test_words = ['ap', 'add']
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
        
        
#######################
########Tries##########
#######################

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """

        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char] = TrieNode()
                node = node.children[char]
                node.is_word = True
            else:
                node.children[char] = TrieNode()
                node = node.children[char]

        pass

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                try:
                    node = node.children[char]
                    return node.is_word
                except KeyError:
                    return False
            else:
                try:
                    node = node.children[char]
                except KeyError:
                    return False
        