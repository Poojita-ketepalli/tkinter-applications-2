import random
print("Winning rules of the Rock Paper Scissor game as follows:\n"+"Rock Vs Paper --> Paper wins\n" + "Rock Vs Scissor --> Rock wins\n" + "Paper Vs Scissor --> Scissor wins")
while True:
    print("enter choice\n 1.Rock\n 2.Paper\n 3.Scissor\n")
    choice=int(input("User turn"))
    while choice>3 or choice<1:
        choice=int(input("enter valid input:"))
    if(choice==1):
        choice_name="Rock"
    elif(choice==2):
        choice_name="Paper"
    else:
        choice_name="Scissor"

    print("Your choice is:"+choice_name+'\n')

    print("Now its computer's turn")
    comp_choice=random.randint(1,3)

    if(comp_choice==1):
        comp_choice_name="Rock"
    elif(comp_choice==2):
        comp_choice_name="Paper"
    else:
        comp_choice_name="Scissor"

    print("computer choice is:"+comp_choice_name+'\n')

    print(choice_name+"Vs"+comp_choice_name)

    if((choice==1 and comp_choice==2) or (choice==2 and comp_choice==1)):
        result="Paper"
    elif((choice==1 and comp_choice==3) or (choice==3 and comp_choice==1)):
        result="Rock"
    else:
        result="Scissor"
    if(result==choice_name):
        print("<==USER WINS==>")
    elif(choice_name==comp_choice_name):
        print("<==THE MATCH IS TIE==>")
    else:
        print("<==COMPUTER WINS==>")

    print("DO YOU WANT TO PLAY AGAIN?(Y/N)")
    ans=input()
    if(ans=='n' or ans=='N'):
        break
    print("THANKS FOR PLAYING:):):)")
    
    
