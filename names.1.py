# In this function, open the file “names.txt” and print its contents using a loop.
def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        s = s.strip()
        print(s)


searchname()