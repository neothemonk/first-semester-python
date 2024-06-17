def loves_me(n):
    templist = []
    output_string = ""
    for i in range(1,n+1):
        if i == n:
            if i % 2 == 0:
                templist.append("LOVES ME NOT")
            else:
                templist.append("LOVES ME")
        elif i % 2 != 0:
            templist.append("Loves me")
        else:
            templist.append("Loves me not")
    for i in templist:
        output_string+=f"{i},"
    return output_string


def main():
    print(loves_me(5))

if __name__=="__main__":
    main()
