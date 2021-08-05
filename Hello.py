def ask_yes_no(prompt):
    #using while loop to make sure type in yes or no. wrong answers will be prompted
     while True:
        answer = input(prompt)
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            continue
  
def main():
    CURRENT_YEAR = 2021
    METER_TO_FEET = 3.218

    #ask for details from users
    firstname = input("Your first name: ")
    lastname = input("Your last name: ")
    year_born = input("When you were born: ")
    height_meter = input("Your height (meter): ")
    is_male = ask_yes_no("Are you male (yes/no): ")
    is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no): ")

    
    #convert year born form string to integer then calculate
    year_born = int(year_born)
    age = CURRENT_YEAR - year_born

    #convert height from string to float then convert it from meter to feet and take 2 digits
    height_meter = float(height_meter)
    height_feet = height_meter * METER_TO_FEET
    height_feet = round(height_feet,1)

    print("\n---")
    print("Your name is " + firstname + " " + lastname)
    print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
    print("Your are " + str(height_feet) + " feet tall")

    if is_vietnamese: #bằng với if is_vietnamese == True 
        print("You are from Vietnam")
    else:
        print("You are not from Vietnam")

    #check height of the user based on their gender
    if is_male:
        if height_feet > 6.5:
            print("You are", end=" ");

            #print "very" 10 times using for
            for i in range(10):
                print("very", end=" ")
            print("tall as a man")
        elif height_feet > 6.0:
            print("You are tall as a man")
        else:
            print("You are short as a man")
    else:
        if height_feet > 5.7:
            print("You are tall as a girl")
        elif height_feet < 5.0:
            print("You are", end=" ");

            #print "very" 10 times using while
            i = 0
            while 1 < 10:
                print("very", end=" ")
                i+=1
            print("short as a girl")
        else:
            print("You are short as a girl")
    print("---")

main()