import random 


n1=input("enter the first number ")
n2=input("enter the second number ")
target=random.randint(int(n1),int(n2))
inputV = input("guess the number between "+" "+ n1 +" and"+" "+ n2 +" : ")

if(inputV.isdigit()):
    inputValue = int(inputV)
                     

    for i in range(0,11):
        if inputValue == target and i<=3:
            print('piiiii MASTERRR !')
            break
        else:
            if inputValue == target and i>3:
                print("you win !")
                break
            elif inputValue > target:
               print("its less than "+ str(inputValue))
            else:
               print("its greater than "+ str(inputValue))
        inputValue=int(input("you got another try guess again: "))





