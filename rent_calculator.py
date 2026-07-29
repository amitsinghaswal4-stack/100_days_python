##Inputs we need from user
#Total rent
#Total food ordered for snacking
#Electricity units spend
#Charge per unit
#Persons living in room/flat


##Expected output
#total amount you have to pay 

rent = int(input("Enter your PG/Room rent = "))
food = int(input("Enter the amount of food ordered =  "))
electricity_spend = int(input("Enter the total of electricity spend'(in units)' = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Number of persons living in room = "))

total_bill = electricity_spend * charge_per_unit

output = (food+rent+total_bill)//persons

print("Each person will pay = " , output )
