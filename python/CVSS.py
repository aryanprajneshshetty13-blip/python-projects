T=int(input("Enter your CVSS score"))
if T>=9:
    print('Patch within 24 hours  ')
elif T>=7:
    print(" patch within 7 Days ")
elif T>=4:
    print(" patch within 30 Days ")
else:
    print("patch in next cycle ")