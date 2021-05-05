'''
Extra Mile
Modify the Guessing Game to allow 3 tries for the user to guess the number right.
'''

hd_num = 10                                                 
c=1
while True:
    user_num = int(input(f"Try {c}! Guess the number: "))
    if user_num == hd_num:
         print(f"You make it in {c} try! You're Genius")
         break
    elif c==3:
        print("You failed....Bye!!")
        break
    c+=1

'''
$python extramile.py
Try 1! Guess the number: 10
You make it in 1 try! You're Genius 

$python extramile.py                                    
Try 1! Guess the number: 4
Try 2! Guess the number: 3                                    Try 3! Guess the number: 7
You failed....Bye!!  

$python extramile.py                                    
Try 1! Guess the number: 3                                    Try 2! Guess the number: 10
You make it in 2 try! You're Genius                         

'''
