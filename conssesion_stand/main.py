cart =[]
prices = 0
orderNum = 0
menu = {'pizza':12500,
        'shovla': 11000,
        'osh': 14000,
        'hamburger':7500,
        'shorva': 11500,
        'manti': 10400}
print(f"\n---------Our today's menu--------")
for food, price in menu.items():
        print(f'{food:10}: {price:.2f}$')
while True:
        order = input("Enter your order(q to stop programm):")
        if order.lower() == 'q':
                break
        elif order in menu:
                cart.append(order)
                prices += menu.get(order)
                orderNum += 1
        else:
                print("there is not such food in menu, please enter another one")

print(f'----------Total prices of your order---------\n{prices}')
print(f'----------your ordered foods:-----------')
for order in cart:
       print(order)
