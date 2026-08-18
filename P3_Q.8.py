purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount >= 2000:
    discount = purchase_amount * 0.20
elif purchase_amount >= 1000:
    discount = purchase_amount * 0.10
else:
    discount = 0

final_amount = purchase_amount - discount
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")
