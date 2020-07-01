import unittest

# this function calculates the sum of all elements in a given list, and the product of all the elements in a given list multiplied. 
# the runtime of this function O(N) after iterating over each item in a list once 
def foo(arr):
    sum = 0
    product = 1
    for i in range(0, len(arr)):    #O(N) runtime
        sum = sum + arr[i]
    for j in range(0, len(arr)):    #O(N) runtime
        product = product * arr[j]
    result = product + sum
    return result

assert foo([1,2,3,4]) == 34, "should be 34"