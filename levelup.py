import sys
try:
    import keyboard as k
except ModuleNotFoundError:
    print("Fatal: Kyboard not installed!!!")
    print("To install it, type")
    print("\tpip install keyboard")
    exit(1)

def raiseError(_input):
    print("\nAn error has occured. View the last line of the Traceback for info.")
    print("\n")
    raise Exception(_input)

delete=False
messages=0
delay=1
args=sys.argv[1:]
if len(args)>0:
    #Get delete varible
    if args[0].lower()=="true":
        delete=True
    elif args[0].lower()=="false":
        delete=False
    else:
        raiseError("Varible DELETE must be a bool.")
if len(args)>1:
    try:
        messages=int(args[1])
    except ValueError:
        raiseError("Varible MESSAGES must be an int.")
if len(args)>2:
    try:
        delay=int(args[2])
    except ValueError:
        raiseError("Varible DELAY must be an int.")
    if delay<1:
        raiseError("Varible DELAY must be greater than or equal to 1")
if len(args)>3:
    raiseError("Too many arguments.")

print([delete,messages,delay])
