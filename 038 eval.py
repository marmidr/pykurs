import math

while True:
    print("Enter formula for variable x: (eg. x * 10)")

    try:
        line = input()
    except KeyboardInterrupt as e: # ^C
        break

    if len(line) == 0:
        break

    print("You entered: ", line)
    args = list(range(10))

    try:
        for x in args:
            print(x, "->", eval(line))
    except SyntaxError as e:
        print(e)

