# Below is a program that stores some gross salary variables and determines the montly contributions someone will pay
grossincome = float(input("Enter you gross income here:" ))
if grossincome > 0 and grossincome < 5999:
    print("Monthly contribution is: 150.00")
elif grossincome >= 6000 and grossincome < 7999:
    print("Monthly contribution is: 300.00")
elif grossincome >= 8000 and grossincome < 11999:
    print("Monthly contribution is: 400.00")
elif grossincome >= 12000 and grossincome < 14999:
    print("Monthly contribution is: 500.00")
elif grossincome >= 15000 and grossincome < 19999:
    print("Monthly contribution is: 600.00")
elif grossincome >= 20000 and grossincome < 24999:
    print("Monthly contribution is: 750.00")
elif grossincome >= 25000 and grossincome < 29999:
    print("Monthly contribution is: 850.00")
elif grossincome >= 30000 and grossincome < 49999:
    print("Monthly contribution is: 1000.00")
elif grossincome >= 50000 and grossincome < 99999:
    print("Monthly contribution is: 1500.00")
else:
    print("Monthly contribution is: 2000.00")