def linear(P, Q, k):
    """
    A recursive function to determine if a list is scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[0] == k*Q[0]:
        return linear(P[1:], Q[1:], k)
    else:
        return False
    
P = [1,2,3]
Q = [2,4,6]
k = 2
print(linear(P, Q, k)) # True
print(linear([1,2,3], [2,4,6], 3)) # False
print(linear([1,2,3], [2,4,6], 1)) # False
print(linear([1,2,3], [2,4,6], 2)) # True
print(linear([1,2,3], [2,4,6], 0)) # False
print(linear([1,2,3], [2,4,6], 4)) # False
print(linear([1,2,3], [2,4,6], 5)) # False
print(linear([1,2,3], [2,4,6], 6)) # True




