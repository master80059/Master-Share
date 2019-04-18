import hashlib
import secrets


    
def dollar(ammount): # used in print command to format floats to us currency format for easy read.
    return("${0:,.2f}".format(amount))
    
def Crypto(ammount): # used in print command to format floats to us currency format for easy read.
    return("Crypto{0:,.24f}".format(amount))



def get_bool(prompt): #used to get a bool input and add different entries or answers not case sensitive 
    while True:
        try:
            return {"true":True,"t":True,"yes":True,"y":True,"false":False,"f":False,"no":False,"n":False}[input(prompt).lower()]
        except KeyError:
            print ("Invalid input: please enter true, t, yes, y or false, f, no, n. not case sensitive")
    
def get_int(prompt): # used to get a int input
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print ("invalid input must be in 000 format!")
    

def get_word(prompt):
    while True:
        try:
            return str(input(prompt).upper()) 
        except KeyError:     
            print("letter only!")


def get_float(prompt): #used to get a float input
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print ("invalid input must be in 000.00 format!")

def get_hash(data):
    h = hashlib.sha3_512()
    h.update(
    str(data)
    )
    return h.hexdigest()
        
def get_random_hex(size):
    return secrets.token_hex(size)

