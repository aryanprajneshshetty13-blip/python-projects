timer = 5

# Keep looping as long as the timer is greater than 0
while timer > 0:
    print(timer)
    
    # Decrease the timer by 1 each loop (countdown!)
    timer -= 1 

print("Blast off!")

# 1. Create a counter variable and set it to 0
vowel_count = 0

# 2. Loop through each letter in the string
for letter in "python programming":
    
    # 3. Check if the current letter is inside our string of vowels
    if letter in "aeiou":
        # 4. If it is a vowel, add 1 to our counter
        vowel_count += 1

# 5. Print the final count outside the loop
print(vowel_count)















































for items in "apple", "banana", "STOP", "cherry", "date":
    if items =="STOP":
        break
    print(items)