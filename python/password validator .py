
while True:
 B=input(" Enter your pasward ")
 if len(B) >= 8:
        has_upper = False
        has_lower = False
        
        for char in B:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
                
        if has_upper == True and has_lower == True:
            print(f"your password is created | {len(B)}")
            break
        else:
            print("Password needs both uppercase and lowercase!")
 else:
  print(f"password too short | {len(B)}")
 
