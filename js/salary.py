# Take the current health as an integer
health = int(input('Enter boss health percentage (0-100): '))

# Check the conditions to figure out the game state
if health > 50:
    combat_status = "Phase 1: Standard attack patterns."
elif health > 0:
    combat_status = "Phase 2: Aggressive mode activated. Watch your posture!"
else:
    combat_status = "Execution successful. Good ending unlocked."

# Print the result using an f-string
print(f"System Update | Boss Health: {health}% | {combat_status}")