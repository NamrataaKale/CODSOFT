first=input("Enter first number:")
operator=input("Enter an operator : +,-,*,/,% ")
second=input("Enter second number:")

first=int(first)
second=int(second)


if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
else:
    print("Invalid operator") 
    
    

