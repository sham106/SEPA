import os
def product_menu():
    print("chose your operation")
    print("1 = product* ")
    print("2 = Readfile(to load data into array* ")
    print("3 = insert new product* ")
    print("4 = delete product* ")
    print("5 = update_customer* ")

    # options for the customer to choose
    option = int(input("Enter your choice: "))

    while True:
        if option == 1:
            product()
        elif option == 2:
            readfile()
        elif option == 3:
            insert_new_product()
        elif option == 4:
            delete_product()
        elif option == 5:
            update_product()
        else:
            print("Try another option!")
            return


def product():
    # Write product data into a file
    product_file = open("product.txt", "a")
    product_id = input("Enter id: ")
    product_name = input("enter product name: ")
    price = input("Enter price of the product: ")
    product_description = input("Enter the description of the product: ")
    product_quantity = input("Enter the quantity: ")
    total = float(price) * int(product_quantity)
    print(total)
    product_file.write(product_id+"~"+product_name+"~"+price+"~"+product_description+"~"+product_quantity+"\n")
    product_file.close()


# Loading product data into array
def readfile():
    product_file = open("product.txt", "r")
    words = product_file.read().splitlines()  # puts the file into array
    product_file.close()
    return words


# Inserting new product
def insert_new_product():
    print("enter the details of new product")
    product()


# deleting a product
def delete_product():
    lines = []
    # read file
    with open("product.txt", "r") as fp:
        lines = fp.readlines()
        # write file
        with open("product.txt",  "w") as fp:
            # Iterate each line
            for number, line in enumerate(lines):
                if number not in[0]:
                    fp.write(line)


# Updating a product
def update_product():
    fh_r = open("product.txt", "r")
    fh_w = open("product.txt", "w")
    product_id = int(input("Enter the ID number to search: "))
    s = " "
    while s:
        s = fh_r.readlines()
        l = s.split("~")
        if len(s) > 0:
            if int(l[0]) == product_id:
                product_id = input("Enter id: ")
                product_name = input("enter product name: ")
                price = input("Enter price of the product: ")
                product_description = input("Enter the description of the product: ")
                product_quantity = input("Enter the quantity: ")
                total = float(price) * int(product_quantity)
                print(total)
                fh_w.write(product_id + "~" + product_name + "~" + price + "~" + product_description + "~" + product_quantity + "\n")
            else:
                fh_w.write(s)

    fh_w.close()
    fh_r.close()
    os.rename(product.txt, product.txt)


update_product()




