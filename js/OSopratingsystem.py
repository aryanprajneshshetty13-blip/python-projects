#A=current core temperature of the device in Celsius
A=float(input("enter current core temperature in celsius "))
if A<=40 :
    state="Optimal stander opration "     

elif A<=75:
     state="warning: activating thermoelectric cooling "
else :
     state="Critical: Throttling GPU to prevent hardware failure"
print(f"your temp is {A}| status {state}")
 