# Python Program to illustrate 
# Hangman Game 
import random 
from functions import get_alpha



from collections import Counter
  
someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
  
someWords = someWords.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word = random.choice(someWords)

  
if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a fruit') 
  
    for i in word: 
         # For printing the empty spaces for letters of the word 
        print('_', end=' ') 
    print()

    c = Counter(word.strip()) # create a counter instance

    unique = sorted(c) # A sorted counter unstance works like a set
    
    entered  = set() # Set of correct input by user
    

    true = True
    
    while true:
        try: 
            choice = get_alpha("Choose an alphabet: ")

            if choice in unique:
                for i in word: # Loop through the random word
                    if choice == i: # if user input is the current letter
                        print(i, end=" ")
                        entered.add(i)

                    else:
                        print("_", end=" ")
                print()

        except ValueError:
            print(ValueError)


        if entered == unique:
            true = False
