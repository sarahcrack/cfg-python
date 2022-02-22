chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

chocolate_type = input('What type of chocolate would you like to buy: white, milk, dark or vegan?')

if chocolate_type == 'white':
    print(chocolates['white'])
elif chocolate_type == 'milk':
    print(chocolates['milk'])
elif chocolate_type == 'dark':
    print(chocolates['dark'])
elif chocolate_type == 'vegan':
    print(chocolates['vegan'])
else:
    print("Sorry we don't have that type of chocolate")