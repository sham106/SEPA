import os


def customer_menu():
    print("chose your operation")
    print("1 = customer* ")
    print("2 = delete_customer_features* ")
    print("3 = update_customer* ")

    # options for the customer to choose
    option = int(input("Enter your choice: "))

    while True:
        if option == 1:
            customer()
        elif option == 2:
            delete_customer_features()
        elif option == 3:
            update_customer()
        else:
            print("Try another option!")
            return


def customer():
    # Loading customer data into the file
    outfile = open("customer.txt", "a")
    customer_id = input("Enter  the customer id: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter your e-mail address: ")
    city = input("Name of your city: ")

    outfile.write(customer_id+"~"+first_name+"~"+last_name+"~"+phone+"~"+email+"~"+city+"\n")

    outfile.close()


# Deleting customer features
def delete_customer_features():
    lines = []
    # read file
    with open("customer.txt", "r") as fp:
        lines = fp.readlines()
    # write file
    with open("customer.txt",  "w") as fp:
        # Iterate each line
        for number, line in enumerate(lines):
            if number not in[0]:
                fp.write(line)


def update_customer():
    fh_r = open("customer.txt", "r")
    fh_w = open("customer.txt", "w")
    customer_id = int(input("Enter the ID number to search: "))
    s = " "
    while s:
        s = fh_r.readlines()
        l = s.split("~")
        if len(s) > 0:
            if int(l[0]) == customer_id:
                customer_id = input("Enter  the customer id: ")
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                phone = input("Enter phone number: ")
                email = input("Enter your e-mail address: ")
                city = input("Name of your city: ")

                fh_w.write(customer_id + "~" + first_name + "~" + last_name + "~" + phone + "~" + email + "~" + city + "\n")
    fh_w.close()
    fh_r.close()
    os.rename("customer.txt", "customer.txt")

customer_menu()