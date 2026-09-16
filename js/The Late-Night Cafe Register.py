#A=customer's available budget
A=float(input("enter your budget"))
while True:
    # Everything indented under here will run forever!
    print("The cafe is open.")
    
    # We need a way to stop it, otherwise it's an infinite loop
    command = input("Type 'exit' to close the shop: ")
    
    if command == 'exit':
        print("Shutting down the register...")
        break  # This command instantly smashes you out of the loop
if A>=120.50:
    item_name="chessy maggi"
    changes=A-120.50
    print(f"you budget is {A}|and you changes {round(changes,2)}|you {item_name} will be ready in 5 mint")

elif A>=60:
    item_name="std maggi"
    changes=A-60
    print(f"your budget is {A}|your change is {round(changes,2) }|you {item_name} will be ready in 5 mint")

else: 
    print(f"budget is to low {A}| go home twin  " )