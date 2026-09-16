import random
B=random.randint(1,101)
live=10
while live >0:
 guess=int(input(" enter your guess in number "))
 guess_hint=abs(B-guess)
 if guess==B:
    print(f" congrats you guessed it| {B} ")
    break
 elif guess_hint<20:
    print("warm")
    print(B)
    live=live-1
    print(guess_hint)
 elif guess_hint>20:
    print("cold")
    print(B)
    print(guess_hint)
    live=live-1
else:
    print("try again")
    print(B)
