# 1. Set up your starting variables
attempts = 0
max_attempts = 3

# 2. The while loop runs AS LONG AS attempts is less than 3
while attempts < max_attempts:
    guess = input("Enter password: ")
    
    # 3. Check if they got it right
    if guess == "Secure@123":
        print("Access Granted")
        break  # This smashes us out of the loop early!
    
    # 4. If they got it wrong, add 1 to the attempt counter
    else:
        attempts = attempts + 1
        print("Access Denied")

# 5. Outside the loop, check if they maxed out their tries
if attempts == max_attempts:
    print("Account Locked")