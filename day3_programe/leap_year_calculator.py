print("Welcone to the leap year calculator...\n")
year = int(input("Enter the year here.. "))
if year%4==0:
    if year %400==0:
        print(f"{year},is a leap year")
    else:
        if year %100:
            print(f"{year}, is a leap year.")
        else:
            print(f"{year}, is not a leap year")
else:
    print(f"{year}, is not a leap year.")