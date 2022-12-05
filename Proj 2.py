
#############################################################
#  Computer Project #2
#
#    Objective is to make calculations to find amount due
#
#    amount due is based on customer code, number of rental\
#    days, the odometer at the start, and the odometer at \
#    the end.
#
#    Program uses integers, condtions, input/outputs,\
#    and iterations
#
#    Finds the final amount due based on the input given
#
#    The first section of code is where the program gives\
#    the user a list of inputs that need to put in
#
#    The next section of code asked the user if they would\
#    like to continue 
#
#    If the user chose A the program would run through a\
#    series of calculations and inputs based on the\
#    customer code
#
#    If the program reviews an invalid customer code, an\
#    error message will print as well as another prompt
#
#    The program will run until the user does not want to\
#    continue
#
#    Program will print "Thank you for your loyalty!" at\
#    the end
#############################################################

import math
print("\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)") 

answer = input("\nWould you like to continue (A/B)? \n")

while answer == "A":

    customer_code = ("BD", "D", "W")
    answer1 = input("\nCustomer code (BD, D, W): \n")

    while answer1 != "BD" and answer1 != "D" and answer1 != "W":
        print("\n\t*** Invalid customer code. Try again. ***")
        customer_code = ("BD", "D", "W")
        answer1 = input("\nCustomer code (BD, D, W): \n")

    num_rental_days = int(input("\nNumber of days: \n"))
    odometer_start = int(input("Odometer reading at the start: \n"))
    odometer_end = int(input("Odometer reading at the end:   \n"))    
        

    print("\nCustomer summary:")
    print("\tclassification code:", answer1)
    print("\trental period (days):", num_rental_days)
    print("\todometer reading at start:", odometer_start)
    print("\todometer reading at end:  ", odometer_end)

    
    if odometer_start <= odometer_end:
        num_miles_driven = (odometer_end - odometer_start) / 10

    else:
        num_miles_driven = ((odometer_end + 1000000) - odometer_start) / 10

    amount_due = float(60)
    amount_dueBD = float(40)
    amount_dueW = float(190)


    print("\tnumber of miles driven: ", num_miles_driven)


    if answer1 == "W":
        weeks = math.ceil(num_rental_days / 7)
        if (num_miles_driven/weeks) <= 900:
            finalW = amount_dueW * weeks
            print("\tamount due: $",finalW )

        if ((num_miles_driven/weeks) > 900) and ((num_miles_driven/weeks) < 1500):
            finalW = (amount_dueW + 100) * weeks 
            print("\tamount due: $",finalW )
            
        if (num_miles_driven/weeks) > 1500:
            over_lim = num_miles_driven - (weeks*1500) 
            finalW = (amount_dueW * weeks)+ (200 * weeks) + (over_lim * 0.25)

    
            
            print("\tamount due: $",finalW )
        
        answer = input("\nWould you like to continue (A/B)? \n")



    if answer1 == "BD":

        final_BD = amount_dueBD * num_rental_days + (num_miles_driven * 0.25)
        print("\tamount due: $",final_BD)
        
        answer = input("\nWould you like to continue (A/B)? \n")

    if answer1 == "D":
        if num_miles_driven <= 100:
            print("\tamount due: $", amount_due * num_rental_days)    

        elif num_miles_driven > 100:
            amount1 = amount_due * num_rental_days 
        
            amount0 = (num_miles_driven - (100 * num_rental_days)) * 0.25
            print("\tamount due: $",amount1 + amount0)

        answer = input("\nWould you like to continue (A/B)? \n")
    
    

print("Thank you for your loyalty.")



"\n\t*** Invalid customer code. Try again. ***"
"\nCustomer summary:"
"\tclassification code:"
"\trental period (days):"
"\todometer reading at start:"
"\todometer reading at end:  "
"\tnumber of miles driven: "
"\tamount due: $"
"Thank you for your loyalty."
