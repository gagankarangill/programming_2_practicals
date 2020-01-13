total_items = int(input("Number of items :"))
total_price = 0
for i in range(1, total_items+1):
    price = int(input("Price of item:"))
    total_price = total_price + price
if total_price > 100:
    discount = 0.10 * total_price
    discounted_price = total_price-discount
    print("Total discounted price is $", discounted_price)
else:
    print("Total price for", total_items, "items is $", total_price)

