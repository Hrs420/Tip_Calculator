print("Welcome to the Tip Calculator")

bill = float(input("What was the total Bill? $"))

Tip = float(input("What percentage Tip would you like to give? 10, 12 or 15? "))

tip_percentage = float(bill*Tip/100)
total_bill = float(bill + tip_percentage)

split = float(input("How many people would to like to split you Bills? "))
split_bill = round(float(total_bill/split),2)

print("Each Person should Pay: "+str(split_bill))
