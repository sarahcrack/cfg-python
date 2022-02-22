# Exercise 1
chairs = 15
nails = 4
total_chairs = chairs*nails
message = 'I need to buy {} nails'.format(total_chairs)
print(message)
print('You need to buy {} nails'.format(total_chairs))
# problem was that 15 was written as a string '15'

#Exercise 2
my_name = 'Penelope'
my_age = 29
message2 = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message2)
# problem was that Penelope was not written as a string 'Penelope'

#Exercise 3
number_egg_boxes = 10
number_eggs_in_box = 6
number_eggs_omelette = 4
total_number_eggs = number_egg_boxes * number_eggs_in_box
number_omelettes = total_number_eggs / number_eggs_omelette
total_omelettes = 'You can make {} omelettes with {} boxes of eggs'.format(int(number_omelettes), number_egg_boxes)
print(total_omelettes)

# you can use int() to get rid of decimal point

