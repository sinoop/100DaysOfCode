import random
from os import system, name

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_value = 0
paper_value = 1
scissors_value = 2
user_selection = 0
computer_selection = 0
user_score = 0
computer_score = 0

outcomes = {
    str(rock_value) + str(rock_value): -1,
    str(rock_value) + str(paper_value): 1,
    str(rock_value) + str(scissors_value): 0,
    str(paper_value) + str(paper_value): -1,
    str(paper_value) + str(rock_value): 0,
    str(paper_value) + str(scissors_value): 1,
    str(scissors_value) + str(scissors_value): -1,
    str(scissors_value) + str(rock_value): 1,
    str(scissors_value) + str(paper_value): 0
}


def display_logo(value):
    if value == rock_value:
        print(rock)
    if value == paper_value:
        print(paper)
    if value == scissors_value:
        print(scissors)


# define our clear function
def clear():
    # for windows 
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while (user_selection >= 0):
    print(f"""
    ---------------------------------------------------------------------
    User : {user_score}                       Computer : {computer_score}                  
    ---------------------------------------------------------------------
    """
          )
    user_selection = int(input("Which one do you choose ? \n 0 - Rock \n 1 - Paper\n 2 - Scissors\nType the "
                               "corresponding index : "))
    if 3 > user_selection >= 0:
        print("You chose : ")
        display_logo(user_selection)
        computer_selection = random.randint(0, 2)
        print("Computer chose : ")
        display_logo(computer_selection)
        # print(str(user_selection)+str(computer_selection))
        winner_indicator = outcomes[str(user_selection) + str(computer_selection)]
        if winner_indicator == 0:
            print("You won...!!!")
            user_score += 1
        elif winner_indicator == 1:
            print("Computer won...!!!")
            computer_score += 1
        else:
            print("Its a tie")
    else:
        print("\n\n---------------------------------------------------------------------\n",
              "!!!!!....Wrong Selection....!!!!!\n",
              "---------------------------------------------------------------------\n")
    clear()