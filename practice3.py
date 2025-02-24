#write a function that take a list of integers
#returns a new list with element indiced at even numbers 

#START
#DEFINE a FUNCTION that takes a LIST of INTEGERS as input
#SET EMPTY LIST to include only even numbers indiced elements
#IF index of the number is even number (index % 2 == 0), APPEND to EMPTY LIST
#RETURN a new list

def every_other_element(list_integers):
    new_list = []
    for integer in list_integers:
        if list_integers.index(integer) % 2 == 0:
            new_list.append(integer)
    return new_list

print(every_other_element([1,4,7,2,5]))

#2nd attempt
def every_other_element(list_integers):
    index = 0
    new_list = []
    while index < len(list_integers):
        new_list.append(list_integers[index])
        index += 2
    return new_list

print(every_other_element([1,4,7,2,5]))

#3rd attempt
def every_other_element(list_integers):
    return list_integers[::2]
print(every_other_element([1,4,7,2,5]))