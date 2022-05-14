
#setting up the leap year logic

def is_leap_year(year):
    if(year % 100 != 0 and year % 4 ==0):
        return True
    elif(year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False

# user validation loop

while True:
    try:
        current_year = int(input("Please enter a year: "))
        if(is_leap_year(current_year)):
            print(current_year, "is a valid leap year!!")
        else:
            print(current_year, "is not a valid leap year!!")
    except:
        print("Please try again!!!")