# tip calculator and bil splitter app

print("Welcome to the tip calculator!")
pre_tax_bill = input("What was the total bill?\n>> ")
if pre_tax_bill.isnumeric():
    pre_tax_bill = int(pre_tax_bill)
else:
    print("total error")
    exit()

tip_percent = input("How much tip would you like to give? 10, 12 or 15 percent\n>> ")
if tip_percent.isnumeric():
    tip_percent =int(tip_percent)
else:
    print("tip error")
    exit()

if int(tip_percent) not in [10, 12, 15]:
    print("tip error")
    exit()

bill_split = input("How many people to split the bill?\n>> ")
if bill_split.isnumeric():
    bill_split = int(bill_split)
else:
    print("split error")
    exit()

print(f"Each person should pay: ${round((pre_tax_bill * (tip_percent + 100)/100)/bill_split, 2)}")