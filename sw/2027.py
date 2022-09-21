"""
#++++
+#+++
++#++
+++#+
++++#"""
for i in range(5):
    for z in range(5):
        if i == z:
            print("#", end="")
        else:
            print("+", end="")
    print()
