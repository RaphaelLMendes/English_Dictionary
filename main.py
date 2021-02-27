import json
from difflib import get_close_matches

#Creating dictionairy from json file
data = json.load(open('JSON+Data+Inside/data.json'))

def translate(word):

    # Finding words with close matches
    closeWord = get_close_matches(word,data.keys())

    #Checking if word typed is in the data set
    if word in data:
        meaning = data[word]
        print = '\n'.join(meaning)
    elif word.capitalize() in data:
        meaning = data[word.capitalize()]
        print = '\n'.join(meaning)
    elif word.upper() in data:
        meaning = data[word.upper()]
        print = '\n'.join(meaning)
    elif len(closeWord)>0:          #if not, we will check if they made a typo
        ask = input('\ndid you mean.. '+ closeWord[0]+'?(y/n)           \n').lower()
        if ask == 'y':
            meaning = data[closeWord[0]]
            print = '\n'.join(meaning)
        else:
            print = 'That word doesnt exist, please try again.'
    else:
        print = 'That word doesnt exist, please try again.'
    return print

word = input('Please type a word: ').lower()

print(translate(word))
input()
