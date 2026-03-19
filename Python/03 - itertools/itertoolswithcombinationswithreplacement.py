from itertools import combinations_with_replacement

# Read input: string and size
s, k = input().split()

# Sort string to get combinations in lexicographic order,
# then generate combinations with replacement
result = combinations_with_replacement(sorted(s), int(k))

# Join characters and print each combination on a new line
for c in result:
    print("".join(c))
