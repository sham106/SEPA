from customer import*
from product import*


def menu():
    while True:
        print("@@@@ welcome to the best online store @@@")
        print("chose your operation")
        print("1 = customer* ")
        print("2 = purchase* ")
        print("3 = product* ")

        # options for the customer to choose
        option = int(input("Enter your choice: "))
        while option != 0:
            if option == 1:
                customer()
            elif option == 2:
                purchase()
            elif option == 3:
                product()
            else:
                print("Try another option!")
                return


def purchase():
    return True


if __name__ == '__main__':
    menu()
