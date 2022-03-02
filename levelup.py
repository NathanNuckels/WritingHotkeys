import sys
try:
    import keyboard as k
except ModuleNotFoundError:
    print("Fatal: Kyboard not installed!!!")
    print("To install it, type")
    print("\tpip install keyboard")
    exit(1)
delete=False
messages=0
delay=1
if len(sys.argv)>1:
    if sys.argv[1].lower=="-help" or sys.argv[2].lower=="--help":
        print("Syntax: python levelup.py [bool: DELETE] [int: MESSAGES] [float: DELAY]")
        print("\tDelete: delete messages?")
        print("\tMessages: Number if messages. Set to 0 for infinite.")
        print("\tDelay: The delay in seconds between messages. Must be greater than 1")
        exit(0)
    if sys.argv[1].lower=="true":
        delete=True
    elif sys.argv[1].lower=="false":
        delete=False
    else:
        print("Error: DELETE must be true or false.")
        exit(1)
    if len(sys.argv)>2:
        try:
            messages=int(sys.argv[2])
        except ValueError:
            print("Error: MESSAGES must be a number")
            exit(1)
        if messages<=0:
            print("Error: MESSAGES must not be negitive.")
            exit(1)
        if len(sys.argv)>3:
            try:
                delay=int(sys.argv[3])
            except ValueError:
                print("Error: DELAY must be a number")
                exit(1)
            if delay<1:
                print("Error: DELAY must be greater than 1")
                exit(1)
print([delete,messages,delay])
