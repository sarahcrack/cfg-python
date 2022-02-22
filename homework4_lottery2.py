import random

# setup
lottery_ticket = [1, 2, 11, 22, 33, 44, 55]


# get winning lotto numbers
def get_winning_numbers(n):
    num = range(1, 59)
    lotto_numbers = random.sample(num, n)
    return lotto_numbers


# check how many numbers on ticket match winning numbers
def check_numbers(w):
    matches = 0  # initialise a count
    for number in w:  # iterate through every number in the list of winning numbers
        if number in lottery_ticket:  # if number also appears on lottery ticket, add +1 to matches
            matches += 1
    return matches


# Run programme

# Assign output of get_winning_numbers to a variable called winning_numbers
winning_numbers = get_winning_numbers(7)

# Assign output of check_numbers to a variable called correct_count
correct_count = check_numbers(winning_numbers)

print(
    f"""
    Ticket numbers: {lottery_ticket}
    Winning Numbers: {winning_numbers}
    Matches: {correct_count}
    """
)
# """triple quotes""" are so you can print text across multiple lines with one print statement

if correct_count == 7:
    print("Congratulations, you win £1,000,000 for seven matching numbers!!")
elif correct_count == 6:
    print("Congratulations, you win £10,0000 for six matching numbers!!")
elif correct_count == 5:
    print("Congratulations, you win £100 for five matching numbers!!")
elif correct_count == 4:
    print("Congratulations, you win £40 for four matching numbers!!")
elif correct_count == 3:
    print("Congratulations, you win £20 for three matching numbers!!")
elif correct_count == 2:
    print("Congratulations, you win £1 for two matching numbers!!")
elif correct_count == 1:
    print("Congratulations, you win 50p for one matching number!!")
else:
    print("Better luck next time!")
