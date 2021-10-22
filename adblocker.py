from begoneads.begoneads import install
from begoneads.begoneads import uninstall
from elevate import elevate

print("You Must Have Administrator or Root Access!")
elevate()
print("Block or Unblock?")
print("1. Block")
print("2. Unblock")
print("Enter Your Choice: ")
Choice = int(input())
if Choice == 1:
    install()
else:
    uninstall()