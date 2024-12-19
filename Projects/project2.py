cupcake_points = 0
muffin_points = 0
answer = input("on a bad hair day would you rather A) wear a hat, or B) spend extra time fixing it?")
if answer == "A":
    cupcake_points += 1
elif answer == "B":
    muffin_points += 1
answer = input ("do you usualy, A) dress for comfort, or B) dress for the eye?")
if answer == "A":
    muffin_points += 1
elif answer == "B":
    cupcake_points += 1
answer = input("when you put on an outfit do you, A) add accessories, or B) just leave it as it is")
if answer == "A":
    cupcake_points += 1
elif answer == "B":
    muffin_points += 1
answer = input("when your at a social gathering are you, A) social and outgoing, or B)shy and kept to your self ")
if answer == "A":
    cupcake_points += 1
elif answer == "B":
    muffin_points += 1
answer = input("when you have a project due do you, A) do it in a timely maner with time too spare, or B) procrastinate till the very last minute")
if answer == "B":
    cupcake_points += 1
elif answer == "A":
    muffin_points += 1
if cupcake_points > muffin_points:
    print("your a Cupcake!")
if muffin_points > cupcake_points:
    print("your a Muffin!")