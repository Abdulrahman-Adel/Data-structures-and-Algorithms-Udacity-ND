# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:39:10 2020

@author: Abdelrahman
"""
import time

def BubbleSort(arr):
    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp    
                
                
    return arr

arr = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]

tic = time.time()
print(BubbleSort(arr)) 
toc = time.time()        

print(toc-tic)   


#Helper Function
def is_time_bigger(time, time_to_compare):

    t_hours, t_min = time
    ttc_hours, ttc_min = time_to_compare

    if t_hours > ttc_hours:
        return True
    elif t_hours < ttc_hours:
        return False
    else:

        if t_min >= ttc_min:
            return True
        else:
            return False
        
        
def BubbleSort_2(arr):
    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if not is_time_bigger(arr[i],arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp    
                
                
    return arr    

sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)] 

tic = time.time()
print(BubbleSort_2(sleep_times)) 
toc = time.time()        

print(toc-tic)    
        