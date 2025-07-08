# day 2: tip calculator

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill (USD)?"))
tip_percent = int(input("What is the tip percentage you'd like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / people
print(f"Each person should pay {amount_per_person:.2f} USD.")