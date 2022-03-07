#Faulty Calculator

n1 = int(input("Enter first number: "))
op = input("Enter Operation: ")
n2 = int(input("Enter second number: "))

if(n1 == 45 and op == '*' and n2 == 3):
    print("45*3 = 555")
elif(n1 == 56 and op == '+' and n2 == 9):
    print("56+9 = 77")
elif(n1 == 56 and op == '/' and n2 == 6):
    print("56/6 = 4")
    

#Working Calculator

else:
    if(op == '+'):
        n3 = n1+n2
        print("%d%c%d = %d" %(n1, op, n2, n3))
    
    if(op == '-'):
        n3 = n1-n2
        print("%d%c%d = %d" %(n1, op, n2, n3))

    
    if(op == '*'):
        n3 = n1*n2
        print("%d%c%d = %d" %(n1, op, n2, n3))

    
    if(op == '/'):
        n3 = n1/n2
        print("%d%c%d = %d" %(n1, op, n2, n3))

    if(op == '%'):
        n3 = n1%n2
        print("%d%c%d = %d" %(n1, op, n2, n3))
