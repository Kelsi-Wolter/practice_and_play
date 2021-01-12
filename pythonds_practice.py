

# iterate through and generate random character choices until goal string
# is produced

# write a function that generates a string 28 characters long

# write a function that scores each generated string by comparing to goal string

# third function to call both functions until goal string is made, print
# string every 1000x tries

import random 

CHARS = 'abcdefghijklmnopqrstuvwxyz '
GOAL = 'methinks it is like a weasel'

def string_generator():
    str_try = ''

    for char in range(28):
        char = random.choice(CHARS)
        str_try += char 

    return str_try

def string_score(trial):
    score = 0 
    
    for i in range(len(GOAL) - 1):
        if trial[i] == GOAL[i]:
            score += 1

    return score

   

def function_caller():
    attempts = 0

    while True:
        string = string_generator()
        if string_score(string) != 28:
            attempts += 1
            # if attempts % 1000 == 0:
            #     print(string)
        else:
            attempts += 1
            break
    
    return f'Found goal string on attempt {attempts}'



# Then, adjust the function so that if a character is correct, the function only changes one
# other character at a time

def string_generator2():
    str_try = ''

    for char in range(28):
        char = random.choice(CHARS)
        str_try += char 

    return str_try

def string_score2(trial):
    score = 0 
    fill_in_string = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    for i in range(len(GOAL) - 1):
        if trial[i] == GOAL[i]:
            score += 1
            fill_in_string[i] = trial[i]

    return score, fill_in_string

def string_adj(trial_str):
    

def function_caller2():
    attempts = 0
    string = string_generator()
    score, fill_in_string = string_score(string)

    while True:
        if score != 28:
            attempts += 1
            # some way to keep all the chars that are correct
            # change one of the chars that is incorrect
            char_to_adj = fill_in_string.index(1)
            fill_in_string[char_to_adj] = random.choice(CHARS)
            string = ''.join(fill_in_string)
            score = string_score(string) #TODO returns both score and list of chars


            # if attempts % 1000 == 0:
            #     print(string)
        else:
            attempts += 1
            break
    
    return f'Found goal string on attempt {attempts}' 
    
