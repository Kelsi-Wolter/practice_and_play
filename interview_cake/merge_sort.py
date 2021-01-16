# write a function that takes in 2 sorted lists and returns a merged
# sorted list


list1 = [1,3,7]
list2 = [0,5,9]

def merge_sort(list1, list2):
    '''
    >>> merge_sort([1,3,7], [0,5,9])
    [0, 1, 3, 5, 7, 9]
    >>> merge_sort([0,2,4,6,8], [1,3,5])
    [0, 1, 2, 3, 4, 5, 6, 8]
    >>> merge_sort([], [1])
    [1]
    '''

    merged = []

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
        

    if len(list1) > len(list2):
        for item in list1:
            merged.append(item)
    else:
        for item in list2:
            merged.append(item)

    return merged

#Bonus
        





