rate_first_1000 = 0.07633
rate_after_1000 = 0.09259

kw_hours_used = int(input("Enter the number of Kilowatt hours used: "))

if kw_hours_used <= 1000:
    amount_owed = rate_first_1000 * kw_hours_used
else:
    amount_owed = (rate_first_1000 * 1000) + (rate_after_1000 * (kw_hours_used - 1000))

print("Amount owed is: $%.2f" % amount_owed)