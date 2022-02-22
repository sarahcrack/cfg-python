meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount code? y/n ')
discount_applicable = discount_choice == 'y'

if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')

print('Total cost: {:.2f}'.format(meal_price))