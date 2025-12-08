def strlen(s):
    counter = 0
    for _ in s:
        counter += 1
    return counter


def strrev(s):
    rstr = ""
    l = strlen(s)
    while l > 0:
        rstr += s[l - 1]
        l -= 1
    return rstr


def strcat(st1, st2):
    return st1 + st2


def strcmp(st1, st2):
    if st1 == st2:
        print(st1 + " and " + st2 + " are same")
    elif st1 > st2:
        print(st1 + " comes after " + st2 + " in the Dictionary")
    else:
        print(st1 + " comes before " + st2 + " in the Dictionary")


print("String Functions:\n 1. String Length \n 2. String Reverse \n 3. String Concatenation\n 4. String Comparison\n 5. Exit")

while True:
    n = int(input("Enter your Choice: "))

    if n == 1:
        s = input("Enter a String: ")
        print("Length of the string is:", strlen(s))

    elif n == 2:
        s = input("Enter a String: ")
        print("Reversed String is:", strrev(s))

    elif n == 3:
        str1 = input("Enter the first String: ")
        str2 = input("Enter the second String: ")
        print("Concatenated string is:", strcat(str1, str2))

    elif n == 4:
        st1 = input("Enter the first String: ")
        st2 = input("Enter the second String: ")
        strcmp(st1, st2)

    elif n == 5:
        print("Exited")
        break

    else:
        print("Invalid choice")

