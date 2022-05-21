# using main function to call other functions
def searchage():
    user_age = input("enter your age to search:")
    infile = open("names.txt", "r")
    for i in infile:
        if str(user_age) in i:
            print(i)
        else:

            print("age not there")


def searchname():
    infile = open("names.txt", "r")
    user = input("Enter your first letter: ").upper()
    for s in infile:
        s = s.strip()
        if s.startswith(user):
            print(s)

def  main():
    users_choice = int(input("chose 1 to search with name or 2 to search with age: "))
    if users_choice == 1:
        searchname()
    elif users_choice == 2:
        searchage()
    else:
        print("wrong choice!!!")


main()