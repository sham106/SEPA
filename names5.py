#  such that it gets the search age from the user
def searchage():
    user_age = input("enter your age to search:")
    infile = open("names.txt", "r")
    for i in infile:
        if str(user_age) in i:
            print(i)
        else:

            print("age not there")


searchage()