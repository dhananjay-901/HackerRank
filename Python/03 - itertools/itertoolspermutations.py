from itertools import permutations

# Read input from STDIN
s_k = input().split()
s = s_k[0]
k = int(s_k[1])

# Sort the string first to ensure lexicographical order of permutations
sorted_s = sorted(s)

# Generate permutations of the sorted string with length k
perms = list(permutations(sorted_s, k))

# Print each permutation on a new line
for perm in perms:
    print("".join(perm))
