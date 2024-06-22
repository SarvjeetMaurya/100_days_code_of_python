print("Welcome to the rollercoster...")
height =float(input("What is your height in cm ? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoster.\n")
    age = int(input("Enter your age here... "))
    if  age<12:
        print("Child Ticktes are 5$ .")
        bill=5
    elif age <=18:
        print("Youths tickets are 7$ .")
        bill=7
    else:
        print("Adults ticktes are 12$ .")
        bill = 12
    want_pic = input("Do you wants take the picture? Y or N  ")
    if want_pic == "Y" or want_pic == "y":
        bill = bill+3
        print(f"please pay {bill}$")
    else:
        print(f"please pay {bill}$")
else:
    print("Sorry, you have to grow taller before you can ride.")