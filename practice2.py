#write a function that takes a a list of strings as its input
#concatenate each strings all together
#and return the result

#START
#DEFINE FUNCTION that takes a LIST of STRINGS as its input
#SET VARIABLE result = ''  (empty string)
#SET iteration to iterate each element of the list
#ADD each element to the VARIABLE 'result' at each iteration
#PRINT 'result'

def concatenated(lst_strings):
    result = ''
    for string in lst_strings:
        result += string
    return result

print(concatenated(['abc', 'def', 'gds']))
