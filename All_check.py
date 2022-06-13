import re

email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
master_card = '^5[1-4][0-9]{12}(?:[0-9]{3})?$'
visa_card = '^4[0-9]{12}(?:[0-9]{3})?$'
number = '[+-]?[0-9]+\.[0-9]+$'

def check_email(s):

    if(re.search(email,s)):
        print("Valid Email\n")
    else:
        print("Invalid Email\n")

def check_card(c):

    if(re.search(master_card,c)):
        print("Mastercard.\n")
    elif(re.search(visa_card, c)):
        print("VISA Card.\n")
    else:
        print("Invalid Card Number.\n")

def check_number(n):
    if(re.search(number,n)):
        print("Floating Number.\n")
    else:
        print("Not floating number.\n")

while(True):
    print("Menu:\n\t1. Card\n\t2. Number\n\t3. Email\n\t4. Exit")
    command = input(">> ")

    if command=='1':
        c = input("\nEnter card number to check : ")
        check_card(c)
    elif command=='2':
        n = input("\nEnter number to check : ")
        check_number(n)
    elif command=='3':
        s = input("\nEnter mail to check : ")
        check_email(s)
    elif command=='4':
        break
    else:
        print("Error occured. Try again.")
