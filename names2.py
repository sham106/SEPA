def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        s = s.strip()
        if s.startswith("A"):
            print(s)


searchname()