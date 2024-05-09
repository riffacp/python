import random
def user():
    user_choice=str(input("enter rock,paper,scissor")).lower()
    while user_choice not in["rock","paper","scissor"]:
        user_choice=str(input("enter rock,paper,scissor")).lower()
    return user_choice

        
def comp():
     return random.choice(["rock","paper","scissor"]) 
      
       
def winner(user,comp):
    if user==comp:
        return "its a tie"
    elif (user=="rock" and comp=="scissor") or (user=="paper"and comp=="rock")or(user=="scissor "and comp=="paper"):
        return "user is the winner"
    else:
        return "computer is the winner"
        
def game():
    print("lets play rock,paper,scissor")
    user_choice=user()
    comp_choice=comp()
    print(f'you chose:{user_choice}')
    print(f'computer chose: {comp_choice}')
    result=winner(user_choice,comp_choice)
    print(result)
    
    
    
game()    
          
    