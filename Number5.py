#  Print the numbers that are equal to the square of the sum of its digits
for count in range(1, 101):

    # Finding the sum of the digits of each number
    sum_of_count = 0
    string_number = str(count)
    for i in string_number:
        sum_of_count += int(i)

# Determining if the square  of the sum of the  digits is equal to the number
    if  sum_of_count**2 == count:
        print(count)