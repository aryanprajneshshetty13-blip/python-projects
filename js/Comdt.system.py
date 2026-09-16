Curse_energy=100
curse_health=100

while True:
 F=input("enter you move:")
 if F=="c" or F=="c":
    print("Smart choice | Reterning to arena.... ")
    break
 elif F=="A" or F=="a":
      Curse_energy= Curse_energy-20
      curse_health= curse_health-20
      print(f"try harder lil bro|your curse enegry left {Curse_energy}|curse health left{curse_health} ")

 elif F=="B" or F=="b":
    Curse_energy= Curse_energy-80
    curse_health= curse_health-80
    print(f"I got carless |your curse enegry left {Curse_energy}|curse health left{curse_health}")
 else :
    print("invalid move | chose move A,B,C")
 if curse_health<=0:
    print("we won")
    break
