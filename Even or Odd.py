def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
print ("This program will take a number input from the user and provide whether the number is even or odd.")
print ("The user can run this program as much as they want to.") 
while True:
    a=int(input("Enter a number - "))
    if a%2==1:
        print ("This number is an odd number.")
    else:
        print ("This number is an even number.")
    if not Continue():
        break
