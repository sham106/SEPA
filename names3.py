def searchname():
    infile = open("names.txt", "r")
    user = input("Enter your first letter: ").upper()
    for s in infile:
        s = s.strip()
        if s.startswith(user):
            print(s)


searchname()