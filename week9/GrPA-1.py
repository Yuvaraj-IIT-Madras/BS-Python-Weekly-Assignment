def reverseList(inputList):
    
    return inputList[::-1]

originalList = input("Enter the list of values with space between each element").split()
reversedList = reverseList(originalList)
print(reversedList)
