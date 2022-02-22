import random

random_lottery_number = random.randint(1, 59)
print(random_lottery_number)


def random_numbers(n):
    num = range(1, 59)
    lotto_numbers = random.sample(num, n)
    print(lotto_numbers)


# random_numbers(7)
lotto = random_numbers(7)
print(lotto)

lottery_ticket = [1, 2, 11, 22, 33, 44, 55]

count = 0
for a in lotto:
    if a in lottery_ticket:
        count += 1
print(count)

if lottery_ticket == lotto:
    print("Congratulations, you win £1000000 for seven matching numbers!!")
else:
    print("Better luck next time!")
