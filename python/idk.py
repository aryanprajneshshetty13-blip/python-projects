B=int(input(" Enter your num: "))
for i  in range(1,11):
    print(i*B)

A=int(input(" Enter your num "))
if A%2==0:
    print(f"{A} is even number: ")
else:
    print("Odd num")
    while A in range(1,11):
        print(A)