print("Welcome to love calculator.... ")
name1= input("Enter your name \n")
name2= input("Enter your parterner name \n")
both_name = name1 + name2
combined_name= both_name.upper()
T= combined_name.count("T")
R= combined_name.count("R")
U=combined_name.count("U")
E= combined_name.count("E")
first_score= (T+R+U+E)
l=combined_name.count("L")
o=combined_name.count("O")
v=combined_name.count("V")
e=combined_name.count("E")
second_score= (l+o+v+e)
final_score= int(str(first_score)+str(second_score))
if final_score < 10 or final_score > 90:
    print(f"Your love score is {final_score},you go together like coke and memtos.")
elif final_score>40 and final_score<50:
    print(f"Your love score is {final_score},you are alright together.")
else:
    print(f"Your love score is {final_score}.")