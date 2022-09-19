t = int(input())

for i in range(1, t + 1):
    n = input()
    y = n[0:4]
    m = n[4:6]
    d = n[6:8]
    if (
        y != "0000"
        and (
            m == "01"
            or m == "03"
            or m == "05"
            or m == "07"
            or m == "08"
            or m == "10"
            or m == "12"
        )
        and int(d) <= 31
        and int(d) > 0
    ):
        print("#" + str(i), y + "/" + m + "/" + d)

    elif (
        y != "0000"
        and (m == "04" or m == "06" or m == "09" or m == "11")
        and int(d) <= 30
        and int(d) > 0
    ):
        print("#" + str(i), y + "/" + m + "/" + d)
    elif y != "0000" and m == "02" and int(d) <= 28 and int(d) > 0:
        print("#" + str(i), y + "/" + m + "/" + d)
    else:
        print("#" + str(i), "-1")
