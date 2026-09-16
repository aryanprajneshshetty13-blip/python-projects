# 1. Starting stats and attack damage
# 1. Starting stats and attack values
cursed_energy = 100
curse_health = 100
A = 20  # Light attack damage & energy cost
B = 80  # Heavy attack damage & energy cost

while True:
    # 2. Take the player's move (A, B, or C to retreat)
    choise = input("Enter your move (A, B, C): ")

    # 3. Option C: Retreat from the Domain
    if choise == "C" or choise == "c":
        print("Smart choice. Retreating from the arena...")
        break

    # 4. Option A: Light Attack (Black Flash)
    elif choise == "A" or choise == "a":
        cursed_energy = cursed_energy - 20
        curse_health = curse_health - A
        print(
            f"Try harder lil bro | Curse health left: {curse_health} | Your energy left: {cursed_energy}"
        )

    # 5. Option B: Heavy Attack (Domain Expansion)
    elif choise == "B" or choise == "b":
        cursed_energy = cursed_energy - 80
        curse_health = curse_health - B
        print(
            f"Try harder lil bro | Curse health left: {curse_health} | Your energy left: {cursed_energy}"
        )

    # 6. Handle typos so the game doesn't crash
    else:
        print("Invalid move! Type A, B, or C.")

    # 7. Win Condition: Only check AFTER the attack hits!
    if curse_health <= 0:
        print("I got careless | We won! The curse is exorcised.")
        break

    # 8. Clean visual separator between turns
    print("-" * 45)