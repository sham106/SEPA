#   Print the numbers that are divisible by the sum of its digits
for count in range(1, 101):

    # Finding the sum of the digits of each number
    sum_of_count = 0
    string_number = str(count)
    for i in string_number:
        sum_of_count += int(i)

# Determining if the sum of the  digits divides the number wholly
    if i == sum_of_count:
        print(count)