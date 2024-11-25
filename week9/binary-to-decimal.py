bin='00011111'

# Working block

def bin_to_dec(bin):
    
    if len(bin) == 1:
        return int(bin)
    
    init = bin[:-1]
    last = bin[-1]

    print("init : ",init)
    print("last : ",last)    
    print("type(bin) : ",type(bin))
    print("type(init) : ",type(init))
    print("type(last) : ",type(last))
    
    return bin_to_dec(init) * 2 + int(last)

# def bin_to_dec(bin):
#     if len(bin) == 1:
#         return int(bin)
#     init = bin[:-1]
#     last = bin[-1]
#     return bin_to_dec(init) + int(last) * 2

# def bin_to_dec(bin):
#     if bin == 0 or bin == 1:
#         return bin
#     init = bin[:-1]
#     last = bin[-1]
#     return bin_to_dec(init) + int(last) * 2

# def bin_to_dec(bin):
#     if len(bin) == 1:
#         return int(bin)
#     init = bin[:-1]
#     last = bin[-1]
#     return bin_to_dec(init) * 2 + last

#print(bin_to_dec(bin))