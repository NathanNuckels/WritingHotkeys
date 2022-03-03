import time

try:
    import keyboard as k
except ModuleNotFoundError:
    print("Fatal: Kyboard not installed!!!")
    print("To install it, type")
    print("\tpip install keyboard")
    exit(1)

print("Press 0 to start.")
print("Hold Esc to stop.")
count=0
k.wait("0")
k.press_and_release("backspace")
while True:
    k.write(str(count))
    k.press_and_release("enter")
    time.sleep(1)
    count=count+1
    if k.is_pressed("9"):
        break
    print("----")

k.press_and_release("enter, enter")
k.write("`Finished`")
k.press_and_release("enter")
