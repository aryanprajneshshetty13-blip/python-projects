def calculate_damage(base_attack,enemy_defence):
    final_damage=base_attack -enemy_defence
    if final_damage < 0:
        final_damage = 0
    return final_damage 
    
strick=calculate_damage(50, 20)
print(strick) 