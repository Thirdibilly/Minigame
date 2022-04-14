import random
import string


# HANGMAN GAME
word_list = ["APPLE", "DENTIST", "PROGRAMMING", "ROUTER"]

def run_hangman(word):
    blank_word = "_" * len(word) # The word as '_'
    success = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    hangman_state = display_hangman(tries)
    print(f"HANGMAN!\n{hangman_state}\n{blank_word}\n")

    while not success and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(blank_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                blank_word = "".join(word_as_list)
                if "_" not in blank_word:
                    success = True
        elif len(guess) == len(word):
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                success = True
                blank_word = word
        else:
            print(f"Not a valid guess.")    
        hangman_state = display_hangman(tries)
        print(f"{hangman_state}\n{blank_word}\n")
    if success:
        print("You guessed the word!")
    else:
        print(f"You ran out of tries. The word was {word}")

def display_hangman(remaining_tries):
    states = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                 -----
                """,
                # Head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                 -----
                """,
                # Head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                 -----
                """,
                # Head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                 -----
                """,
                # Head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                 -----
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                 -----
                """,
                # Rope
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                 -----
                """,
                # Initial state
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                 -----
                """
    ]
    return states[remaining_tries]

# PALINDROME CHECK
def run_palindrome():
    word = input("Enter a word to check if it is a palindrome: ").upper() # Making the word uppercase
    word = word.translate(str.maketrans('', '', string.punctuation)) # Eliminating punctuation
    isPalindrome = word == word[::-1] # checking if it is a palindrome comparing the original string with the reversed version of the string

    if isPalindrome:
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")

# GAMES MAIN MENU
def menu():
    while True:
        print("""

BILLY's GAMES
---------------
1. Hangman
2. Palindrome
0. Quit""")
        game_selected = input()
        print("\n")
        if game_selected == '1':
            word = random.choice(word_list)
            run_hangman(word)
        elif game_selected == '2':
            run_palindrome()
        elif game_selected == '0':
            break

if __name__ == "__main__":
    menu()
