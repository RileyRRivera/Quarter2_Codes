def total_fee(dist, rate):
    total=dist*rate
    total=round(total, 2)
    return total

dist=float(input("Enter distance in kilometers:"))
rate=float(input("Enter rate per kilometers(₱):"))
total=total_fee(dist, rate)
print("Total delivery fee:", total)
