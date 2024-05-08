def longest_word(sentence) :
    count=0
    word_list=sentence.split()
    for word in word_list :
        if len(word)> count :
            count =len(word)
            longest= word
    return longest

print(longest_word("this is the longest woooooooord"))


######### another solution ##########

def longestWord(sentence) :
    longest=""
    word_list=sentence.split()
    for word in word_list :
        if len(word) > len(longest) :
            longest= word
    return longest

print(longestWord("this is the longest woooooooord"))
