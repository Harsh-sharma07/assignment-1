name=input("plz enter your name")
print("welcome,",name,'\n')
starting_message="""
plz choose your task:
type 1 ----> for check balance
type 2 ----> for deposit amount
type 3 ----> for withdrawl
"""
print(starting_message)
task = int(input("plz enter your task:"))
current_avlbal=5000
if task>=1 and task<=3:
    if task==1:
        print("yoiur available balance is:",current_avlbal)
        ##code to check balance
    elif task==2:
        deposit=int(input("enter your deposit amount"))
        if deposit>=500:
            current_avlbal+=deposit
            print("you have successfully deposited your amount",deposit)
            print("your available balance",current_avlbal)
        else:
            print("enter amount greater than 500")
         
    ##code to deposit
    else:
        withdrawl_amt=int(input("enter amount to withdraw"))
    if withdrawl_amt<=current_avlbal:
        current_avlbal-=withdrawl_amt
        print("you have successfully withdrew your amount",withdrawl_amt)
        print("your available balance",current_avlbal)
    else:
        print("you have not sufficient balance")
      #withdrawl
else:
    print("choose valid task")


