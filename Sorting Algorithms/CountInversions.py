# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:52:05 2020

@author: Abdelrahman
"""


def count_inversions(items):
    if len(items) <= 1:
        return items, 0

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    inversions_left = 0
    inversions_right = 0

    left, inversions_left = count_inversions(left)
    right, inversions_right = count_inversions(right)

    merged, inversions = merge(left, right)

    return merged, inversions_left + inversions_right + inversions


def merge(left, right):
    merged = []
    inversions = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            inversions += 1
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged, inversions