import math

friends = input('How many friends are visiting?' )
pizzas = int(friends) * 0.5
message = 'You need {} pizzas for {} friends'.format(math.ceil(pizzas), friends)
print(message)