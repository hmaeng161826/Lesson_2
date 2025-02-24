#write a function that takes two lists of numbers as input
#merge two list
#when merging, the element of the first list should become the elements at
#the even indexes and second list at the odd indexes
#return the list

def merged(list1, list2):
    merged_list = []
    max_length = max(len(list1), len(list2))
    for i in range(max_length):
        if i < len(list1):
            merged_list.append(list1[i])
        if i < len(list2):
            merged_list.append(list2[i])
    return merged_list
print(merged([1, 2, 3], [4, 5, 6])) # => [1, 4, 2, 5, 3, 6]