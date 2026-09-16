Poster=100
while True:
 A=float(input("Start attacking "))
 if  A== 0 : 
  print("you run away form the arena ")
  break
 Poster= Poster - A
 if Poster <50:
  print(f"come on we are just getting started|{round(Poster,2)}")
 elif Poster> 0:
  print(f"come on this is the final strech Now {round(Poster,2)}")
 else :
   print("we won | legend fall ")
   break 
print("-"*20)

 
 


