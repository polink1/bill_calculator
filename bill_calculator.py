print("Welcome to the 'Split a bill' calculator!")
bill_total = input("How much is the bill? ")
tip = input("What percentage tip would you like to give? 10, 15, or 20? ")
people = input("How many people do you split it between? ")
tip_p = float(tip) / 100 + 1
each_pays = float(bill_total) * tip_p / int(people)
total_each = "%.2f" % float(each_pays)
print(f"Each person should pay ${total_each}")
