price = input('What is the price of the burger? ')
within_budget = float(price) <= 10

veggie = input('Are there any vegetarian options? y/n ')
veggie_option = veggie == 'y'

is_good_choice = within_budget and veggie_option

if is_good_choice:
    print('This restaurant is a great choice!')

if not is_good_choice:
    print('Probably not a good idea')