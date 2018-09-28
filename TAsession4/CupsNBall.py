def cups_n_balls(cup_balls, position_of_balls):
    for i in position_of_balls:
        if i == "A":
          cup_balls[b], cup_balls[a] = cup_balls[a], cup_balls[b]  # swap the contents of first and second cup
        if i == "B":
          cup_balls[c], cup_balls[b] = cup_balls[b], cup_balls[c]  # swap the contents of second and third cup
        if i == "C":
          cup_balls[c], cup_balls[a] = cup_balls[a], cup_balls[c]  # swap the contents of first and third cup
    print(balls_in_cup.index("balls") + 1)  # outputs position of ball


balls_in_cup = ["balls", " ", " .2"]
a = balls_in_cup.index("balls")    # a, b and c stores the position of the contents
b = balls_in_cup.index(" ")
c = balls_in_cup.index(" .2")
movement = str(input("Please input ABC in any order"))
cups_n_balls(balls_in_cup, movement)