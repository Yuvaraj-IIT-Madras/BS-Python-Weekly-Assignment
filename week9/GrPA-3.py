# WEEK9-GrPA 3

# The Collatz function is defined for a positive integer n as follows:

# If n is odd: f(n) = 3n + 1
# If n is even: f(n) = n / 2
# We consider the repeated application of the Collatz function starting with a given integer n, which results in the following sequence:

# f(n), f(f(n)), f(f(f(n))), ...

# It is conjectured that no matter which positive integer n you start from, the sequence will always reach 1. For example, if n = 10, the sequence is:

# Seq No. 1: n = 10, f(n) = 5
# Seq No. 2: n = 5, f(n) = 16
# Seq No. 3: n = 16, f(n) = 8
# Seq No. 4: n = 8, f(n) = 4
# Seq No. 5: n = 4, f(n) = 2
# Seq No. 6: n = 2, f(n) = 1

# Thus, if you start from n = 10, you need to apply the function f six times in order to first reach 1.


def Collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + Collatz(n//2)
    else:
        return 1 + Collatz(3*n + 1) 

print(Collatz(10)) #6
print(Collatz(1)) #0
print(Collatz(2)) #1
print(Collatz(3)) #7
print(Collatz(4)) #2
print(Collatz(5)) #5
print(Collatz(6)) #8
print(Collatz(7)) #16
print(Collatz(8)) #3
print(Collatz(9)) #19
print(Collatz(10)) #6
print(Collatz(11)) #14
print(Collatz(12)) #9
