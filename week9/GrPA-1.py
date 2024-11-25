def reverse_list_recursive(L):
    """
    A recursive function to reverse a list L.

    Arguments:
        L: list, type of elements could be anything
    Returns:
        list: The reversed list.
    """
    # Base case: If the list is empty or has one element, it's already reversed
    if len(L) <= 1:
        return L
    
    # Recursive case: Reverse the rest of the list and append the first element
    return reverse_list_recursive(L[1:]) + [L[0]]

# Example usage
input_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list_recursive(input_list)
print("Original List:", input_list)
print("Reversed List:", reversed_list)

def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
        L: list, type of elements could be anything
    Return:
        result: list
    """
    if len(L) <= 1:
        return L
    
    print("[str(L[-1]),reverse(L[:-1])] : ",[str(L[-1]),reverse(L[:-1])])
    return [L[-1]]+reverse(L[:-1])    

L = [1,2,3]
print(reverse(L))



# def reverseList(inputList):
    
#     return inputList[::-1]

# originalList = input("Enter the list of values with space between each element").split()
# reversedList = reverseList(originalList)
# print(reversedList)
