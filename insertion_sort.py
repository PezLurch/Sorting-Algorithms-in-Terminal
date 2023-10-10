import time
import os
import random

from imports import random_permutation, display_permutation, swap


def insertion_sort(unsorted_list: list[int]) -> list[int]:
    '''
    Sorts a list using the insertion sort algorithm. 
    :param: unsorted_list: The list to sort.
    :return: The sorted list.
    '''
    for i in range(len(unsorted_list)):
        j = i 
        while j > 0:
            if unsorted_list[j] < unsorted_list[j-1]:
                unsorted_list = swap(j-1,j,unsorted_list)
            j-= 1
    return unsorted_list


def show_insertion_sort(unsorted_list: list[int]) -> int:
    '''
    Sorts a list using the insertion sort algorithm and displays the sorting process using barcharts in the terminal.
    :param: unsorted_list: The list to sort.
    :return: The sorted list.
    '''
    for i in range(len(unsorted_list)):
        j = i 
        while j > 0:
            time.sleep(.015)
            os.system('clear')
            display_permutation(unsorted_list,j-1,j)
            if unsorted_list[j] < unsorted_list[j-1]:
                unsorted_list = swap(j-1,j,unsorted_list)
            time.sleep(.015)
            os.system('clear')
            display_permutation(unsorted_list,j-1,j)
            j-= 1
    return 0

if __name__ == '__main__': 
    os.system('clear')
    our_length = 20
    unsorted_list = random_permutation(our_length)
    show_insertion_sort(unsorted_list)
