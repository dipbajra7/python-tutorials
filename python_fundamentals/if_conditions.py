temp = int(input("Enter temperature "))
while(temp != 1000):
    
    if(temp > 76):
        print("it's a hot day")
    elif (temp < 60):
        print("it's a cold day")
    else:
        print("it's a lovely day")

    temp = int(input("Enter temperature "))



house_price = 1000000
high_income = False
good_credit = False
criminal_record = True
credit_score = int(input("enter credit score "))
income = int(input("enter income "))
if(income > 100000):
    high_income = True
if(credit_score >= 800):
    good_credit = True

if(good_credit and high_income and not criminal_record):
    print("down payment is " + str(1/100 * house_price))
elif(good_credit or high_income):
    print("down payment is " + str(10/100 * house_price))
else:
    print("down payment is " + str(20/100 * house_price))