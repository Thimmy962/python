# Python Program to illustrate 
# Hangman Game 
import random 
from functions import get_alpha, IsNotAlphaError, LengthError


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


    revealed = ['_' if c.isalpha() else c for c in word]
    unique = set(word.strip()) # create a counter instance
    entered  = set() # Set of correct input by user

    
    while "_" in revealed:
        try: 
            choice = get_alpha("Choose an alphabet: ") 

            if choice in unique:  # If the choice is among the letters of the word
                for i, char in enumerate(word):  # Loop through the random word
                    if char == choice:
                        revealed[i] = choice  # Update revealed list
                        entered.add(choice)  # Add choice to entered set

                print(' '.join(revealed))

        except LengthError as e:
            print(e)

        except IsNotAlphaError as e:
            print(e)
    
    print("Congratulations! You've guessed the word correctly.")
