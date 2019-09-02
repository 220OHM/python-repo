x = open("cybernetics.txt", "r+")
fu = open("21.txt", "r+")
y = list(x.read())
z = 0
z1 = False
lit = False
x1 = ""
x2 = 0
print(fu.read().format())
aba = input("Take input literal? (Y/N):")
if aba == "Y":
    lit = False
else:
    lit = True
while True:
    x2 = 0
    z1 = False
    hh = False
    z = 0
    y1 = str(input("Search:"))
    z2 = list(y1)
    z2[0] = str(list(z2)[0]).upper()
    z2 = str(z2).replace("[", "").replace("'", "").replace(",", "").replace("]", "").replace(" ", "")
    while z < len(y):
        if y[z] == "\n":
            if lit is True:
                hh = False
                if y1.lower() in x1:
                    x2 += 1
                    z1 = True
                    hh = True
                    print(x1)
                    print()
                    x1 = ""
                    z += 1
                if hh is False:
                    if z2 in x1:
                        x2 += 1
                        z1 = True
                        print(x1)
                        print()
                        x1 = ""
                        z += 1
            if y1 in x1:
                x2 += 1
                z1 = True
                print(x1)
                print()
                x1 = ""
                z += 1
            else:
                x1 = ""
                z += 1
        z -= 1
        x1 += y[z]
        z += 2
    if z1 is False:
        print("no Results found.")
    else:
        if x2 < 2:
            print(x2, "Result found.")
        else:
            print(x2, "Results found.")
