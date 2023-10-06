import random 

option =("rock","paper","sicssors")
runing = True

while True:
 player = None

 computer = random.choice(option)
 while player not in option:
   player=input("Enter a choice (rock,paper,scissors): ")

 print("f Player :{player}")
 print("f computer {computer}")

 if player==computer:
     print("Its a tie")
    
 elif player == "rock" and computer == "sicssors":
  print("you win") 
  
 elif player == "paper" and computer == "rock":
  print("you win") 
  
 elif player == "sicssors" and computer == "paper":
  print("you win") 
  
 else:
  print("You lose!")  
  play_again = input("Play again (y/n):").lower()  
  
  if not play_again == "y":
    runing=False
    
  print("Thank for playing")  