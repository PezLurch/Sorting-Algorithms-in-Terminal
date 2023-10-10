import random 
def random_permutation(length: int)-> list[int]:
    '''
    Returns a random permutation of the numbers 1 to length as an array.

    :param length: The length of the permutation.
    :return: A random permutation of the numbers 1 to length as an array.
    '''
    a = list(range(1,length+1))
    random.shuffle(a)
    return(a)


def display_permutation(perm: list[int],x: int,y: int):
    '''
    Displays a permutation as a bar chart in the terminal. It highlights two of the bars specified by  indices x and y.

    :param perm: The permutation to display.
    :param x: The first element to highlight.
    :param y: The second element to highlight.
    '''
    row = ''
    for i in range(len(perm),0,-1):
        for k in range(len(perm)):
            if perm[k] >= i:
                if k == x or k == y:
                    row += u" \u2588 "
                else: row += u" \u2591 "
            else: row += "   "
        print(row)
        row = ''

def swap(i:int ,j: int ,unsorted_list: list[int])-> list[int]:
    '''
    Function that swaps two entries in a list. It returns the list with the two entries swapped.

    :param: i: The first index to swap.
    :param: j: The second index to swap.
    :param: unsorted_list: The list to swap the entries in.
    :return: The list with the two entries swapped.
    '''
    helper = unsorted_list[i]
    unsorted_list[i] = unsorted_list[j]
    unsorted_list[j] = helper
    return unsorted_list