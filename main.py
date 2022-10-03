salary = float(input("Salary: "))
if salary <= 0:  # handles salary range
    print("Salary must be positive")
else:
    hours = float(input("Hours: "))
    if hours < 0:  # handles hours range
        print("Hours cannot be negative")
    else:
        paycheck = 0.0
        if hours > 40:  # handles overtime pay
            paycheck = 40 * salary + (hours-40) * salary*1.5
        else:
            paycheck = salary * hours
        print("Paycheck: " + str(paycheck))



