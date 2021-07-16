import time
print ("This program will take a number input from the user and provide whether the number is even or odd.")
time.sleep(1.4)
print ("The user can run this program as much as they want to.") 
time.sleep(1.4)
a=int(input("Enter a number - "))
if a%2==1:
    print ("This number is an odd number.")
else:
    print ("This number is an even number.")
while True:
    Again=str(input("Do you want to enter another number? (Yes/No) "))
    if Again=="No":
        quit()
    if Again=="Yes":
        a=int(input("Enter a number - "))
        if a%2==1:
            print ("This number is an odd number.")
        else:
            print ("This number is an even number.")