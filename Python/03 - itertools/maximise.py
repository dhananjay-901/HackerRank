import itertools

def maximize_it(K, M, lists):
    # Square each element in each list and apply modulo M
    # Note: Applying modulo at each step can sometimes be incorrect
    # based on the problem constraints, it's better to do it at the end
    # when calculating the sum for each product.
    # A cleaner approach is to square elements and then apply modulo in the final sum.
    # Let's stick to the approach that squares first and then mods in the sum.

    # Generate all possible combinations (Cartesian product)
    all_combinations = itertools.product(*lists)
    
    max_s = 0
    for combination in all_combinations:
        current_sum = sum(x**2 for x in combination) % M
        if current_sum > max_s:
            max_s = current_sum
            
    return max_s

# --- Input Handling ---

# Read K and M from the first line
try:
    K, M = map(int, input().split())
except ValueError:
    # Handle cases where input might not be on the same line or similar
    pass 

lists = []
for _ in range(K):
    # Read each line, skip the first element (which is the count Ni)
    row = list(map(int, input().split()[1:]))
    lists.append(row)

# Calculate and print the result
result = maximize_it(K, M, lists)
print(result)
