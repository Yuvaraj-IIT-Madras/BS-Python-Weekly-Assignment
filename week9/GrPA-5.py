def ancestry(P:dict, Present:str, Past:str) -> list:
    """ 
    A recursive function to determine the ancestry of a person in a dictionary          
    return [Present]+ancestry(P, P[Present], Past) if Present != Past else [Present]
    """
    if Present != Past:
        return [Present]+ancestry(P, P[Present], Past)
    else:
        return [Present]

P = {"A":"B", "B":"C", "C":"D", "D":"E", "E":"F", "F":"G"}
print(ancestry(P, "A", "G")) # ['A']
