from random import randint
from functions import get_int, get_int_within_range

value = {
    "1": "Rock",
    "2": "Paper",
    "3": "scissors"
}
def get_rounds():
    while True:
        try:
            rounds = get_int("How many rounds to play: ")
            if rounds % 2 == 1:
                return rounds
            else:
                raise ValueError("Must be an odd number")
        except ValueError as e:
            print(e)

def main():
    # scores for computer and 
    comp_score = 0
    user_score = 0
    rounds = get_rounds()

    print("Select a Value:\n1. Rock\n2. Paper\n3. Scissors")
    
    for i in range(rounds):
        user_choice = get_int_within_range("Select a number within 1 - 3: ", 1, 3)
        print(f"You chose {value[str(user_choice)]}")

        comp_choice = randint(1, 3)
        print(f"Computer chose {value[str(comp_choice)]}")

        if comp_choice == 1 and user_choice == 2:
            print("You won this round")
            user_score += 1
        elif comp_choice == 2 and user_choice == 3:
            print("You won this round")
            user_score += 1
        elif comp_choice == 3 and user_choice == 1:
            print("You won this round")
            user_score += 1

        elif user_choice == 1 and comp_choice == 2:
            print("Computer won this round")
            comp_score += 1
        elif user_choice == 2 and comp_choice == 3:
            print("Computer won this round")
            comp_score += 1
        elif user_choice == 3 and comp_choice == 1:
            print("Computer won this round")
            comp_score += 1
        
        else:
            print("This round was a stalemate")
            comp_score += 1
            user_score += 1
    
    
    print("\nFinal Scores:")
    print(f"You: {user_score} | Computer: {comp_score}")



if __name__ == "__main__":
    main()