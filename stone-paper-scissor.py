import random
stone = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image =[stone,paper,scissor]

user_choice = int(input("Enter your choice : 0-stone , 1-paper , 2-scissor\n"))
if user_choice >= 3 and user_choice < 0:
    print("you enter invalid number , you lose!")
else:
    print("you chose:")
    print(game_image[user_choice])
    
    computer_choice = random.randint(0,2)
    print("computer chose:")
    print(game_image[computer_choice])



    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose!")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win!")
    elif computer_choice == user_choice:
        print("It is a draw!")
