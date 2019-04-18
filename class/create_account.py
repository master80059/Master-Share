import datetime
import hashlib
import csv
import os
import time
import resource
accounts = os.path.abspath('accounts\accounts.cvs')
def get_account_information():
    #First_Name = resource.get_word("What is your First Name?")
    #print(First_Name) #debug
    #Middle_Name = resource.get_word("What is your Middle Name?")
    #print(Middle_Name) # debug
    #Last_Name = resource.get_word("What is your Last Name?")
    #print(Last_Name) # debug
    #print(str(" Full Name Entered:" + " " + First_Name + " " + Middle_Name + " " + Last_Name))
    account_ID = resource.get_random_hex(15)
    resource.print_random_hex(account_ID) # debug
    time.sleep(10)


get_account_information()
