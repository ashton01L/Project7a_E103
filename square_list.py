# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/30/2024
# Description: Define a function named 'square_list' that takes as a parameter
# a list of numbers and replaces each value with the square of that value.
# It should not return anything - it should mutate the original list.

def square_list(numlist): # defined a function called 'square_list'
    """
    Defines a function, 'square_list', which mutates a given list of numbers,
    'numlist', to the squared value of those numbers.
    :param numlist: list of numbers to be taken as a parameter and then squared
    by the function.
    :return: No return prompted based on instructions.
    """

    # Evaluates each number, n, in the range of the length of 'numlist' and repopulates
    # 'numlist' with the squared values of each of those numbers, n.
    for n in range(len(numlist)):
        numlist[n] = numlist[n] ** 2

# numlist = [7, -3, 12, 9] # list of numbers to square
# square_list(numlist) # squares the list of numbers given
# print(numlist)  # this will print [49, 9, 144, 81]
