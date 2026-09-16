# 1. Take the customer's available budget as a float
budget = float(input("Enter your budget: ₹"))

# 2 & 3. Use if/elif/else logic to check the budget top-down
if budget >= 120.50:
    B = "Premium Cheesy Maggi"
    change = budget - 120.50
    # 4. Print success with f-string and rounded change
    print(f"Order confirmed: {B}. Your change is ₹{round(change, 2)}.")

elif budget >= 60.00:
    B = "Standard Maggi"
    change = budget - 60.00
    # 4. Print success with f-string and rounded change
    print(f"Order confirmed: {B}. Your change is ₹{round(change, 2)}.")

else:
    # 4. Print the broke scenario
    print(f"Budget too low (₹{round(budget, 2)}). You should go home twin ")