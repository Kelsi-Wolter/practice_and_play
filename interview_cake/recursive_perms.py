# Write a recursive function for generating all permutations of an input string. 
# Return them as a set.

# Don't worry about time or space complexity—if we wanted efficiency 
# we'd write an iterative version.

# To start, assume every character in the input string is unique.

#NOT COMPLETE

def all_perms(string):

    take in a string and rearrange all characters in every possible way
    compile each permutation into a set

    each letter in each index of the string
    for each index, it could be any of the letters in the string
    + same function acting on the rest of the indices

    loop through each indice
    at each indice try each character + recursive call for other indices
    base case = complete permutation of string

    perm_set = set()
    for i in range(len(string)):
        for char in string:
            if len(string) > 1:
                perm = char + all_perms(string[i+1:])
            else:
                return char

            perm_set.add()

    return perm_set


            