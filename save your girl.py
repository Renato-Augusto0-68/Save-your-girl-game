import random as r;
print("Welcome to : 'Save your girl'.")
print("coded by Rutheford")
import random as r
name=str(input("Write your name: ")).upper()
print(f"Hello {name}, Welcome to : 'Save your love'.")
print("Coded by Rutheford")
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
  print("Game over, you failed.")print("Your girlfriend/boyfriend was kidnapped by an zombie. You have to kill the zombie to save her/him. You only has 3 attempts")
print("The zombie's position is measured in a cartesian graphic")
if name != 'BIANCA':
 for g in range(1,4):
  x= float(input("x coordinate: "))
  y= float(input("y coordinate: "))
  if((x-k)+(y-p))==0.01:
    print(f"Congrats you nailed it, on the {g} attempt. Now she/he is safe. The coordinates were {k}, {p}.")
    break
  else:
   t=100*(x/k)
   v=100*(y/p)
   def percentage(t,v):
    if t>100:
     t=t-100
     return t
    if v>100:
     v=v-100
     return v
   print(f"You missed this time, try again. The precision is {t}% on the x coordinate and {v}% on the y coordinate. If the percentage is higher than 100, it means that the value is above the zombie's position.")
 if ((x-k)+(y-p))!=0.01 and g==3:
  print(f"Game over,{name}, you failed. The coordinates were {k}, {p}. ")
else:
 for g in range(1,7):
   x= float(input("x coordinate: "))
   y= float(input("y coordinate: "))
   if((x-k)+(y-p))==0.01:
    print(f"Congrats, {name}, nailed it, on the {g} attempt. Now she/he is safe. The coordinates were {k}, {p}")
    break
   else:
    t=100*(x/k)
    v=100*(y/p)
    def percentage(t,v):
      if t>100:
       t=t-100
       return t
      if v>100:
       v=v-100
       return v
    print(f"You missed this time, The precision is {t}% on the x coordinate and {v}% on the y coordinate. If the percentage is higher than 100, it means that the value is above the zombie's position.")
 if ((x-k)+(y-p))!=0.01 and g==7:
    print(f"Game over, {name}, you failed. The coordinates were {k}, {p}.")