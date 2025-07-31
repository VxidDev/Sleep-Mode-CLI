import os
from time import sleep

action = None
actions = ["s" , "r"]
action_defined = False

Time = None
Time_defined = False

while action_defined != True:   
    action = input("\nSelect the mode. (Reboot(R) or Shutdown(S)): ".lower())
    if action not in actions:
        print("\nUnknown mode! Select S or R.")
    else:
        action_defined = True

while Time_defined == False:
    try:
        Time = int(input("\nHow much time before the action?(in minutes): "))
        Time_defined = True
    except ValueError:
        print("Please input a number!")

Time = Time * 60

while Time > 0:
    Time -= 1
    os.system("cls")
    print(f"Time left before action... {Time} seconds.")
    sleep(1)

if action == "s":
    os.system("shutdown /s /f /t 0")
else:
    os.system("shutdown /r /f /t 0")