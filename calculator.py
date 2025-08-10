num1=float(input("enter the frist number: "))
num2=float(input("enter the second number: "))
opp=input("enter the operation to perforn on these numbers: ")

if opp=="+":
    print(num1+num2)
elif opp=="-":
    print(num1-num2)
elif opp=="*":
    print(num1*num2)
else :
    if num2==0:
        print("num2 can't be zero")            
    else:
        print(num1/num2)
            