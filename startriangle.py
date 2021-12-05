def triangle(nLines):
    for i in range(1, nLines + 1):
        print("")
        for p in range(i):
            print("*", end="")


def treeTriangle(nLines, upright=True):
    for i in range(nLines):
        spaces = nLines - i
        if upright == False:
            spaces = i
        for p in range(spaces):
            print(" ", end="")
            stars = 1 + 2 * i
            if upright == False:
                stars = nLines - 2*i
        for j in range(stars):
            print("*", end="")
        print("")


def square(n):
    for i in range(n):
        for p in range(0, n):
            character = "x "
            if(i == 0 or i == n - 1):
                character = "x "
            else:
                if(p == 0 or p == n):
                    character = "x "
                else:
                    character = " "
            print(character, end="")
        print("")


square(4)
