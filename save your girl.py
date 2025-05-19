import random as r;
print("Welcome to : 'Save your girl'.")
print("coded by Rutheford")
k= r.uniform(0, 12)
p= r.uniform(0, 12)
print("Your girlfreind was kidnapped by an zombie. You have to kill the zombie to save her. Only has 3 attempts")
print("The zombie's posiction is measured in a cartesian graphic")
for g in range(1,4):
 x= int(input("x coordinate:  "))
 y=int(input("y coordinate:"))
 if x==k and y==p:
    print(f"Congrats you  nailed it, on the {g} attempt. Now she is safe.")
 else:
   print("You couldnt this time, try again")
if x!=k and y!=p and g==3:
  print("Game over, you failed.")