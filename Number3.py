# Print the ODD numbers divisible by 7 but not 3
for counter in range(1, 101):
    if counter % 2 != 0:

        if counter % 3 != 0 and counter % 7 == 0:

            print(counter)




