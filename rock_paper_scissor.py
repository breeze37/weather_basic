#basic rock paper scissor game

import random
l=["Rock", "Paper", "Scissor"]

while True:
    ucount=0
    ccount=0
    uc=int(input('''
Game start:
1. Start
2. Exit
'''))
    if uc==1:
        pass
        for a in range(1,6):
            userinp=int(input('''
1. Rock
2. Paper
3. Scissor
'''))
            if userinp==1:
                uchoice="Rock"
            elif userinp==2:
                uchoice="Paper"
            elif userinp==3:
                uchoice="Scissor"
            else:
                uchoice="Error"
            cpchoice=random.choice(l)
            
            if cpchoice==uchoice:
                print("User choice is : ", uchoice)
                print("Computer choice is : ", cpchoice)    
                print("It's a draw")
                ucount=ucount+1
                ccount=ccount+1
            elif uchoice=="Rock" and cpchoice=="Paper":
                print("User choice is : ", uchoice)
                print("Computer choice is : ", cpchoice)    
                print("Computer wins!")
                ccount=ccount+1
            elif uchoice=="Paper" and cpchoice=="Scissor":
                print("User choice is : ", uchoice)
                print("Computer choice is : ", cpchoice)    
                print("Computer wins")
                ccount=ccount+1
            elif uchoice=="Scissor" and cpchoice=="Rock":
                print("User choice is : ", uchoice)
                print("Computer choice is : ", cpchoice)    
                print("Computer wins")
                ccount=ccount+1   
            else:
                print("User choice is : ", uchoice)
                print("Computer choice is : ", cpchoice)
                print("You win!") 
                ucount=ucount+1  
        
        if ucount==ccount:
            print("\nYour score : ", ucount)
            print("\nComputer's score : ", ccount)
            print("\nThe match is a draw")
        elif ucount>ccount:
            print("\nYour score : ", ucount)
            print("\nComputer's score : ", ccount)
            print("\nYou are the final winner")
        elif ucount<ccount:
            print("\nYour score : ", ucount)
            print("\nComputer's score : ", ccount)
            print("\nComputer is the final winner")                
    else:
        break
    