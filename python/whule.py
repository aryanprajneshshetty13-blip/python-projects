A=0
max_A=3
while A <max_A:
    G=input("enter your pass : ")
    if G=="secure123":
        print("Access Granted")
        break
    else:
        A=A+1
        print("Acces denied ")
if A==max_A:
    print("Account block ")
        