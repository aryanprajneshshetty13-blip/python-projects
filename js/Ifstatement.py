A=float(input("enter your annual revenue"))
if A<=300000:
  tax_rat=0.00

elif A<=600000:
  tax_rat=0.05
else:
   tax_rat=0.10
tax_Amo=tax_rat*A
C=A-tax_Amo
print(f"you revenue {A} | your tax amount  is {tax_Amo} your net revenue{C} ")