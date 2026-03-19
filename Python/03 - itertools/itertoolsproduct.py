import itertools

# Read input for the first list (space-separated integers)
A = list(map(int, input().split()))

# Read input for the second list (space-separated integers)
B = list(map(int, input().split()))

# Compute the Cartesian product and print the results
# The asterisk (*) unpacks the product iterable into arguments for the print function,
# which then prints them space-separated as individual tuples.
print(*itertools.product(A, B))
