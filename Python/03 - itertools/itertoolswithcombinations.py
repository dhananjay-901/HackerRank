from itertools import combinations

# Read input from STDIN
s, k_str = input().split()
k = int(k_str)

# Sort the string to ensure combinations are in lexicographical order
sorted_s = sorted(s)

# Iterate from combination sizes 1 up to and including k
for i in range(1, k + 1):
    # Generate combinations for the current size
    for comb in combinations(sorted_s, i):
        # Join the characters in the combination tuple and print
        print("".join(comb))
