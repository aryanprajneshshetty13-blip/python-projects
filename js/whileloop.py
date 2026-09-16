# The loop starts here. Everything indented under it will run forever.
# 1. Initialize the boss's health first!
Poster = 100.0

# 2. Capital 'T' in True
while True:
    
    # 3. The input must be INSIDE the loop so you can attack multiple times
    A = float(input("Start attacking: "))

    # 4. Lowercase 'i' in if, and indented the actions underneath it
    if A == 0:
        print("you run away form the arena ")
        break

    Poster = Poster - A

    # 5. Check 'Poster' (the boss health), not 'A' (your attack)
    if Poster > 50:
        print(f"come on we are just getting started | {round(Poster, 2)}")
        
    elif Poster > 0:
        print(f"come on this is the final strech Now | {round(Poster, 2)}")
        
    else:
        print("we won | legend fall ")
        break  # Added this so the loop actually stops when you win!
        
    # Indented this so it prints after every turn
    print("-" * 10)