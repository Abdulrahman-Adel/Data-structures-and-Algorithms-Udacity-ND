# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:46:46 2020

@author: Abdelrahman
"""

import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        
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
                node.children[char].is_word = True
            else:
                node.children[char]
                node = node.children[char]

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                return node.children[char].is_word
            else:
                node = node.children[char]        