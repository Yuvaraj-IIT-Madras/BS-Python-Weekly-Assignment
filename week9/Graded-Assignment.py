# Question 1
# ----------

# def f(n):
#     if n < 10:
#         return 1
#     return 1 + f(n // 10)

# def g(n):
#     if n < 10:
#         return n
#     return n % 10 + g(n // 10)

# def h(n):
#     if n <= 1:
#         return n
#     return n * h(n - 1)

# f n is a positive integer, what does f(n) return? Note that your answer should be applicable for any positive integer n, and not just for a specific value.


# Sum of digits in n.


# Number of digits in n.


# Product of digits in n.


# First digit in n.


# Factorial of n.


# 2 points
# if n is a positive integer, what does g(n) return? Note that your answer should be applicable for any positive integer n, and not just for a specific value.


# Sum of digits in n.


# Number of digits in n.


# Product of digits in n.


# First digit in n.


# Factorial of n.

# Which of the following function calls returns the sum of the digits in 
# 100
# !
# 100!, where, 
# n
# !
# n! is the product of the first 
# n
# n positive integers?


# f(g(100))


# f(h(100))


# g(h(100))


# h(g(100))


# h(f(100))

# Which of the following function calls returns the number of digits in 
# 100
# !
# 100!, where, 
# n
# !
# n! is the product of the first 
# n
# n positive integers?


# f(g(100))


# f(h(100))


# g(h(100))


# h(g(100))


# h(f(100))

# Common Data for questions (5) and (6)

# Two lists are equal if and only if they satisfy both the following conditions:

# (1) They have the same number of elements. Call this the size of the list.

# (2) The 
# i
# t
# h
# i 
# th
#   element in the first list is the same as the 
# i
# t
# h
# i 
# th
#   element in the second list for 
# 0
# ≤
# i
# <
# size
# 0≤i<size. We are using zero-indexing here.

# If both lists are empty, then they are assumed to be equal.

# equality is a function that accepts two lists P and Q as arguments and returns True if the lists are equal and False otherwise. Questions (5) and (6) discusses multiple ways of implementing this function.


# 4 points
# Select all correct implementations of the function equality. [MSQ]

# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     size = len(P)
#     for i in range(size):
#         if P[i] != Q[i]:
#             return False
        
# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     size = len(P)
#     for i in range(size):
#         if P[i] != Q[i]:
#             return False
#     return True

# def equality(P, Q):
#     size = len(P)
#     for i in range(size):
#         if P[i] != Q[i]:
#             return False
#     return True

# def equality(P, Q):
#     for elem in P:
#         if elem not in Q:
#             return False
#     return True

# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     for elem in P:
#         if elem not in Q:
#             return False
#     return True

# def equality(P, Q):
# 	return P == Q

# Select all the correct recursive implementation of the function equality. [MSQ]

# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     if P[-1] != Q[-1]:
#         return False
#     return equality(P[:-1], Q[:-1])

# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     if len(P) == 0:
#         return True
#     if P[0] != Q[0]:
#         return False
#     return equality(P[:-1], Q[:-1])

# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     if len(P) == 0:
#         return True
#     if P[0] != Q[0]:
#         return False
#     return equality(P[1: ], Q[1: ])

# def equality(P, Q):
#     if len(P) != len(Q):
#         return False
#     if len(P) == 0:
#         return True
#     if P[-1] != Q[-1]:
#         return False
#     return equality(P[: -1], Q[: -1])

# 7) A binary number consists of a string of ones and zeros. For example, 101 and 110101 are binary numbers. Every binary number can be converted into its corresponding decimal number. If a1, a2, ..., an is an n-digit binary number, then its decimal counterpart is given by:
# a1 * 2^(n-1) + a2 * 2^(n-2) + ... + an-1 * 2^1 + an * 2^0

# For example, the decimal representation of the binary number 1011 is:
# 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 11

# Write a function named bin_to_dec that accepts a binary number bin as a non-empty string. It should return its decimal representation as an integer. Some sample instances are given below for your reference.

# bin_to_dec(bin) Returns
# bin_to_dec('101') 5
# bin_to_dec('0') 0
# bin_to_dec('1') 1
# bin_to_dec('101101') 45

