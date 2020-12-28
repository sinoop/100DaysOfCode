from words import word_list
from hang_man_ascii_art import hang_man
import random
from os import system,name
from time import sleep

TOTAL_LIVES = 8

def draw_screen_display(score, masked_word, character_serial_numbers, error_count, hang_man, guessed_items):
    sleep(1)
    clear()
    print(f"""
    --------------------------- Welcome to Hangman ---------------------------
    Score : {score} | Remaining Lives = {TOTAL_LIVES - error_count}

    {list_to_str(masked_word)}

    {list_to_str("{:d}".format(x) for x in range(1, len(masked_word)+1))}    

    {hang_man[error_count]}

    Guesses : {list_to_str(guessed_items)}     
    """)

def is_valid_guess(input_str):
    if len(input_str) != 1:
        print("You can enter only one character as guess. Please retry..")
        return False
    elif input_str < 'a' and input_str > 'z':
        print("You cannot enter symbols or numbers as input. Please retry..")
        return False
    else:
        return True

# define our clear function
def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def list_to_str(list_to_process, delimiter = "  "):
    str = ""
    for item in list_to_process:
        str += (delimiter + item + delimiter)
    return str    

random_chosen_word = random.choice(word_list)
random_chosen_word_len = len(random_chosen_word)
random_chosen_word_dict = {}

masked_word = []
index = 0
for char in random_chosen_word:
    masked_word.append("_")
    if char in random_chosen_word_dict:
        random_chosen_word_dict[char].append(index)
    else:        
        random_chosen_word_dict[char] = [index]
    index += 1

character_serial_numbers = ""
error_count = 0

for i in range(1, random_chosen_word_len + 1 ):
    character_serial_numbers += " " + str(i) + " "

guessed_items = []
score = 0

while True:
    draw_screen_display (score, masked_word, character_serial_numbers, error_count, hang_man, guessed_items)
    guess = input("Guess a char : ").lower()    
    if is_valid_guess(guess):
        if guess in guessed_items:
            print(f"You already guessed {guess}.. Please enter some other character")
            continue
        else:
            guessed_items.append(guess)

        if guess in random_chosen_word_dict:            
            indices = random_chosen_word_dict[guess]
            score += len(indices)
            for index in indices:                                
                masked_word[index] = guess

            if score >= random_chosen_word_len:
                print("You guessed the word correctly. Congrats...!!")
                break
        else:
            error_count += 1
            print(f"{guess} is not present in the word. You lose a life.")
            if error_count >= 7:
                print(f"You are out of lives. Game over. Correct word was : {random_chosen_word}")
                break

draw_screen_display (score, masked_word, character_serial_numbers, error_count, hang_man, guessed_items)
