# Print the numbers that are divisible by 7 but not 3
for counter in range(100):
    if (counter % 7 == 0) and (counter % 3!=0):
        print(counter)
