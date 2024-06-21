print(""" __      __       .__                 
/  \    /  \ ____ |  |   ____  ____   _____   ____    
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >    
       \/       \/          \/            \/     \/  """)
print("Life in Weeks Calculator....\n")
expected_age = int(input("How many age do you want to live \n"))
current_age = int(input("Enter your current age \n"))
remain_weeks = (expected_age-current_age) * 52
print(f"You have {remain_weeks} weeks in your life.")