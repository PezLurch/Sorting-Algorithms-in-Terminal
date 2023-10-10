import time
import os
import random

from imports import random_permutation, display_permutation, swap

def bubble_sort(unsorted_list: list[int])-> list[int]:
    '''
    Sorts a list using the bubble sort algorithm.
    :param unsorted_list: The list to sort.
    :return: The sorted list.
    '''
    i = 0
    highest = len(unsorted_list) - 1
    while highest > 1:
        if i+1 <= highest:
            if unsorted_list[i]>unsorted_list[i+1]:
                unsorted_list = swap(i,i+1,unsorted_list)
            i += 1
        else:
            highest -= 1
            i = 0
    return unsorted_list


def show_bubble_sort(unsorted_list: list[int])-> list[int]:
    '''
    Sorts a list using the bubble sort algorithm and displays the sorting process using barcharts in the terminal.
    :param unsorted_list: The list to sort.
    :return: The sorted list.
    '''
    i = 0
    highest = len(unsorted_list) - 1
    while highest > 1:
        time.sleep(.015)
        os.system('clear')
        display_permutation(unsorted_list,i,i+1)
        if i+1 <= highest:
            if unsorted_list[i]>unsorted_list[i+1]:
                unsorted_list = swap(i,i+1,unsorted_list)
            i += 1
        else:
            highest -= 1
            i = 0
        time.sleep(.015)
        os.system('clear')
        display_permutation(unsorted_list,i-1,i)
        
    return unsorted_list

if __name__ == '__main__': 
    os.system('clear')
    our_length = 20
    unsorted_list = random_permutation(our_length)
    show_bubble_sort(unsorted_list)