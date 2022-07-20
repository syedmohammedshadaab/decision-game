print("Welcome to my decision game!")
name = input("enter the name? ")
age = int(input("enter the age? "))
print("Hello",name,"ur age",age)

if age>=18:
  print("ur old enough to play")
  health=11
  print("ur starting",health,"health")
  wants=input("do u want to play? (yes/no) ").lower()
  if wants=="yes":
    print("Lets play")
    lf=(input("now ur in ryt track to go futher in the game plz select left or ryt (left/ryt)? ")).lower()
    if lf=="left":
      print("ur are in the car ")
      print("car meet with an accident due to it u lost 5 health")
      health -=5
      s=input("after car meet with an accident u have two choose to select car or bike(car/bike) ")
      if s=="car":
        print("u lost the game u meet with an accident again....")
      if health<=0:
          print ("game over")
      else:
          print ("u have taken the ryt decision.....U WON")
      
     
      
    elif lf=="ryt":
      print("ur are in the ship")
      
    else:
     print("u lost")
  else:
    print("u cant play")
else:
  print("ur are not old enough to play...")
