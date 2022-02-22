when_book_written = int(input('When was the book written?'))

if when_book_written < 1809:
    print('Nineteenth, century, Tens')
elif when_book_written < 1819:
    print('Nineteenth, Teens')
elif when_book_written < 1829:
    print('Nineteenth, Twenties')
elif when_book_written < 1839:
    print('Nineteenth, Thirties')
elif when_book_written < 1849:
    print('Nineteenth, Forties')
elif when_book_written < 1859:
    print('Nineteenth, Fifties')
elif when_book_written < 1869:
    print('Nineteenth, Sixties')
elif when_book_written < 1879:
    print('Nineteenth, Seventies')
elif when_book_written < 1889:
    print('Nineteenth, Eighties')
elif when_book_written < 1899:
    print('Nineteenth, Nineties')
elif when_book_written < 1909:
    print('Twentieth, Tens')
elif when_book_written < 1919:
    print('Twentieth, Teens')
elif when_book_written < 1929:
    print('Twentieth, Twenties')
elif when_book_written < 1939:
    print('Twentieth, Thirties')
elif when_book_written < 1949:
    print('Twentieth, Forties')
elif when_book_written == 1950:
    print('Twentieth, Fifties')
else:
    print("We only sell books written between 1800 and 1950")


