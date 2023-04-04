my_number = 6

user_value = int((input("Please guess a number: ")))

while user_value != my_number:
   if user_value > my_number:
    print("too high")
    if user_value < my_number:
      print("too low")

    user_value = int(input("Sorry, wrong! Try again: "))

    print("You got it!")