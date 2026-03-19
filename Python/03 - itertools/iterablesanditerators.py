from itertools import combinations

# Read input values
# The first integer N is read but not strictly needed in the combinations approach
N = int(input()) 
# Read the list of letters
letters = input().split()
# Read the number of indices to select
K = int(input())

# Generate all possible combinations of K indices (represented as tuples of characters)
all_combinations = list(combinations(letters, K))
total_combinations = len(all_combinations)

# Count combinations that contain the letter 'a'
count_with_a = 0
for combo in all_combinations:
    if 'a' in combo:
        count_with_a += 1

# Calculate and print the probability rounded to 3 decimal places
probability = count_with_a / total_combinations
print(round(probability, 3))

