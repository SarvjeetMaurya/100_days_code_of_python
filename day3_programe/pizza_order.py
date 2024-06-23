print("Thank you for choosing python pizza Deliveries!\n")
print("their are some pizza and their size...")
print("Small size pizza-$15.\nMedium size pizza -$20.\nLarge size pizza-$25.")
pizza_size = input("What size pizza would you want? 'S', 'M' or 'L' ")
bill= 0
if pizza_size == "s" or pizza_size=="S":
    bill+= 15
elif pizza_size=="m" or pizza_size=="M":
    bill+= 20
elif pizza_size=="l" or pizza_size=="L":
    bill+= 25
else:
    print(f"{pizza_size}, is an invalide input.")
pepperoni = input("Do you want pepperoni?Small size :$2,size M or L:$3 'Y' or 'N'\n")
if pepperoni == "y" or pepperoni=="Y":
    if pizza_size== "S" or pizza_size=="s":
        bill+=2
    else:
        bill+=3
elif pepperoni== "n" or pepperoni=="N":
    bill
else:
    print(f"{pepperoni}, is a invailed input. ")
cheese = input("Do you want extra cheese for $1 ?'Y' or 'N'")
if cheese == "Y" or cheese=="y":
    bill += 1
    print(f"your final bill is ${bill}")
else:
    print(f" your final bill is ${bill}")    