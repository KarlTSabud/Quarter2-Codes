def compute_delivery_fee(distance, rate):
    return distance * rate

distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

total = compute_delivery_fee(distance, rate)

print(f"Total Delivery Fee: ₱{total:.2f}")
