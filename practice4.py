#write a function that takes a character in string as input
#determine the index of the 3rd occurrence of given character
#if the given character does not occur at least 3 times, return None

#START
#DEFINE a FUNCTION that takes a CHARACTER in STRING
#ITERATE each character and find the index of the character
#at each interation, increase index = 0 by 1

def find_nth_occurrence(character, string, n):
    index = -1
    for _ in range(n):
        index = string.find(character, index + 1)
        if index == -1:
            return None
    return index
    
print(find_nth_occurrence("a", "banana", 3))  

