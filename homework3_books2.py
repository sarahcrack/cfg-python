year_written = int(input('When was the book written?'))


def century():
    if year_written >= 1900:
        century = 'Twentieth Century'
    else:
        century = 'Nineteenth Century'
    return century



print(century())