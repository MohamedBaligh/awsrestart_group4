#!/usr/bin/env python3

###### For importing moudles from different directory ######
import sys
sys.path.append('/root/demos/modules/')
############################################################
import user_module

print("")
print("Welcome to User utility app")
print("")
print("Kindly select which action you need to do from the following options")

status=0
while status !=4:
    message="""
    1-User add
    2-Group add
    3-User remove
    4-exit
    """
    print(message)
    status=int(input("Please enter the number of action that you need to excute(i.e 1)"))
    if status == 1:
        user_module.new_user()
    elif status == 2:
        user_module.new_group()
    elif status ==3:
        user_module.remove_user()
    elif status ==4:
        pass
    else:
        print("your enterd option doesn't exist in app options,please try again.")
        status=0

