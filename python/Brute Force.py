import time
pin=int(input("enter your pin "))
B=0
while True:
  start_time = time.time() 
  B=B+1
  print(f"Trying: {B}")
  print(start_time)

  if B==pin:
        print(f"ACCESS GRANTED! The PIN is {B}")
        break
