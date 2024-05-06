def convert(n) :
    #empty list 
    result=[]
    for num in str(n) :
        result.append(int(num))
    result.reverse()
    return result 
print(convert(123456))   

######### Another Solution #########

def convert_number(n) :
    #empty list 
    result=[]
    for num in str(n) :
        result.insert(0 ,int(num))
    return result

print(convert_number(9987456321))










