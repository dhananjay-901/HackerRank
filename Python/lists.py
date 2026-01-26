'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.'''

# insert i e insert integer e at position i
# remove e 
# append e
# sort
# pop
# reverse
# the code should be able to commit these actions during the runtime 
noa = int(input())
list =[]

for i in range(noa):
    n = str(input())
    a = n.split()
    list.append(a)
result = []
for command in list:
    if command[0] == "insert":
        result.insert(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        result.remove(int(command[1]))
    elif command[0] == "append":
        result.append(int(command[1]))
    elif command[0] == "sort":
        result.sort()
    elif command[0] == "pop":
        result.pop()
    elif command[0] == "reverse":
        result.reverse()
    elif command[0] == "print":
        print(result)
