import random 

options = ["rock", "paper", "scissors"] 

user_choice = input("Enter rock / paper / scissors: ").lower() 

computer_choice = random.choice(options) 

print("User choice:", user_choice) 
print("Computer choice:", computer_choice) 

if user_choice == computer_choice:
    print("Result: Draw") 
elif user_choice == "rock" and computer_choice == "scissors":
    print("Result: You Win") 
elif user_choice == "paper" and computer_choice == "rock":
    print("Result: You Win") 

elif user_choice == "scissors" and computer_choice == "paper":
    print("Result: You Win") 

elif user_choice in options:
    print("Result: Computer Wins") 

else:
    print("Invalid input") 
