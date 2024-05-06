# abcdefghijklmnopqrstuvwxyz
import string 

def find_missing_letters(givenletters):
    alpha= string.ascii_lowercase
    strat=alpha.index(givenletters[0])
    for letters in alpha[strat:] :
        if letters not in givenletters:
            return letters
    return f"No missing letters in sequence "

print(find_missing_letters("defgijk"))
print(find_missing_letters("abcdfg"))    
print(find_missing_letters("xyz"))
