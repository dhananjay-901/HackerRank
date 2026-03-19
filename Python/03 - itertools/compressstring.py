from itertools import groupby

# Read input from STDIN
s = input()

# Use groupby to group consecutive characters
# The print statement unpacks the generator expression result with a single space separator
print(*[ (len(list(group)), int(key)) for key, group in groupby(s) ])
