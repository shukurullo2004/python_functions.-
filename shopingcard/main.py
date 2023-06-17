#shopping card
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food that you want to buy (to exit click q )")
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input(f'Enter price of {food.capitalize()} '))
        prices.append(price)

print("You entered: ")
for food in foods:
    print(food)

for price in prices:
    total += price
print(f"total prices of food {total}")

