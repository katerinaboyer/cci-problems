# this function calculates the sum of all elements in a given list, and the product of all the elements in a given list multiplied. 
# the runtime of this function O(N) after iterating over each item in a list once 
def foo(arr):
    sum = 0
    product = 1
    for i in range(0, len(arr)):        # O(N) runtime
        sum = sum + arr[i]
    for j in range(0, len(arr)):        # O(N) runtime
        product = product * arr[j]
    print("sum: ", sum)
    print("product: ", product)

# this function prints out every possible pairing of numbers in a given array, order matters
# the runtime is O(N^2) because for every element 1...N in the outer loop, the inner loop is called O(M) times
def print_pairs(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):    # O(N) runtime
            print(arr[i], ", ", arr[j]) # O(M) runtime

def call_functions():
    foo([1,2,3,4])
    print_pairs([1,2,3,4,5])

call_functions()