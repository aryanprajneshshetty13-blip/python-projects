rate=float(input("enter your rate of Interest :"))
yr=int(input("enter your years"))
p=float(input("enter you principal "))
Si=rate*yr*p/100
Ma=p+Si
print(f"interest earnd {Si}")
print(f"total maturity amount is {Ma}")