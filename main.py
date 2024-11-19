import random
'''

1 for snake
-1 for water
0 for gun

'''

computer = random.choice ([-1,0,1])
youstr = input("enter your choice:")
youDict = {"s":1 , "w" : -1 ,"g" : 0} 
reverseDict = {  1 : "snake"  , -1 : "water"  , 0 : "Gun" }

you = youDict[youstr]

print ( f"You choose{reverseDict[you]}\n Computer choose {reverseDict[computer]}")


if (computer == you):
     print("It's a Draw")

else:
    
     if (computer ==-1 and you ==1):
         print("you win!")
    
    
     elif (computer ==-1 and you ==0):
        print("you loose!")
    

     elif (computer ==1 and you ==-1):
        print("you loose!")
    
    
     elif (computer ==1 and you ==0):
           print("you win!")    
       
    
     elif (computer ==0 and you ==-1):
           print("you win!")
    
    
     elif (computer ==0 and you ==1):
           print("you loose!")    
       
    
     else:
         print("Something went wrong!")    
    
