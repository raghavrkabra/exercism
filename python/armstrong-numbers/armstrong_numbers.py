def is_armstrong_number(number):
    number_length = len(str(number))
    check_number = 0
    working_number = number # to keep the original number intect in while loop

    while working_number > 0:
        working_number, digit = divmod(working_number, 10)
        check_number += pow(digit, number_length)

    return number == check_number
