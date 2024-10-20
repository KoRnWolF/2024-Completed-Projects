import math

print("Welcome to the tip calculator:")
total_bill = float(input("Please enter the total bill?\n"))
tip_percent = int(input("How much would you like to tip in %?\n"))
people_split = int(input("How many people will split the bill?\n"))

print("")
print("Total Bill : R",total_bill)
print("Tip %:",tip_percent,"%")
print("Split between: ",people_split,"people")

total_tip = total_bill * tip_percent / 100
total_bill_plus_tip = total_bill + total_tip

print("Total Tip: R",total_tip)
print("Grand Total: R",total_bill_plus_tip)

individual_amount = total_bill_plus_tip / people_split
print("Each persons amoutn: ",individual_amount)
individual_amount_rounded = math.ceil(individual_amount)
print("Each person should pay: R",individual_amount_rounded)