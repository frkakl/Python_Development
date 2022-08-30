import random
import time


pc_won = "AI Won, Go and Work Hard."
player_won = "You Won, How it Possible."

round = int(input("How Many Round You Wanna Play? 1-3-5 = "))
i = 1
while i <= round:
    player_1 = input("Select Rock, Paper or Scissor : ").upper()
    pc = random.choice(["Rock","Paper","Scissor"]).upper()
    print("AI selected: " + pc)

    if player_1 == "rock" and pc == "paper":
        print(pc_won)
    elif player_1 == "paper" and pc == "scissor":
         print(pc_won)
    elif player_1 == "scissor" and pc =="rock":
         print(pc_won)
    elif player_1 == pc:
        print("Draw, Come and Fight with Me Again")
    else:
            print(player_won)   
    i += 1

time.sleep(3)