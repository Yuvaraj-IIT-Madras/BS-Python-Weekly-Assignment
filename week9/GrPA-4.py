# Fibonacci

# Fibonacci is a young resident of the Italian city of Pisa. He spends a lot of time visiting the Leaning Tower of Pisa, one of the iconic buildings in the city, that is situated close to his home. During all his visits to the tower, he plays a strange game while climbing the marble steps of the tower.

# The Game

# Fibonacci likes to climb the steps either one at a time, two at a time, or three at a time. This adds variety to the otherwise monotonous task of climbing. He wants to find the total number of ways in which he can climb n steps, assuming that the order of his individual steps matters. Your task is to help Fibonacci compute this number.

# For example, if he wishes to climb three steps, the case of n = 3, he could do it in four different ways:

# (1, 1, 1): do it in three moves, one step at a time
# (1, 2): do it in two moves, first take a single step, then a double step
# (2, 1): do it in two moves, first take a double step, then a single step
# (3): do it in just one move, directly leaping to the third step
# To take another example, if n = 5, then some of the sequences could be:

# (1, 3, 1)
# (1, 1, 3)
# (3, 1, 1)
# (2, 1, 1, 1)
# (1, 2, 1, 1)
# (1, 2, 1, 2)
# Each sequence is one of the ways of climbing five steps. The point to note here is that each element of a sequence can only be 1, 2, or 3.

# Write a recursive function named steps that accepts a positive integer n as an argument. It should return the total number of ways in which Fibonacci can ascend n steps. Note that the order of his steps is important.

# For example, the following calls should return the following values:

# print(steps(1)) # 1
# print(steps(2)) # 2
# print(steps(3)) # 4
# print(steps(4)) # 7
# print(steps(5)) # 13
# print(steps(6)) # 24
# print(steps(7)) # 44

# Note: The function should be recursive and should not use any loops.

# Write your code here

def steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return steps(n-1) + steps(n-2) + steps(n-3)

print(steps(1)) # 1
print(steps(2)) # 2
print(steps(3)) # 4
print(steps(4)) # 7
print(steps(5)) # 13


