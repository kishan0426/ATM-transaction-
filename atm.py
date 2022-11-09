#ATM transaction
#Declare the variables

denomination = [3000,6000,9000]
password = 'eXhydra@369'
amount = 100000

#Initialize the value of i

i = 0

#Ask the user to enter the password or pin for ATM 

while i < 3:
    usrpwd = input("Please enter the password : ")
    #If the password is correct, then ask the amount to be withdrawn otherwise prompt to reenter the password
    if usrpwd == password:
        withdraw = int(input("Enter transaction amount to be withdrawn : "))
        #Withdraw the correct amount as per the balance available
        if withdraw > 100000 and withdraw < 1:
            print("Enter an amount 'greater than 0' or 'less than or equal to balance'",amount)
            continue
        else:
            #Print the withdraw message and ask for repeat of transaction
            balance = amount - withdraw
            print("Transaction is successfully completed, account balance is :",balance)
            #If another transaction need to be performed, then enter the amount again
            rewithdraw = input("Do you need to perform another transaction? Yes or No: ")
            if rewithdraw == 'Yes' or rewithdraw == 'YES' or rewithdraw == 'yes':
                amount = balance
                continue
            #If the transaction need to be closed, print the thanks message
            elif rewithdraw == 'no' or rewithdraw == 'No' or rewithdraw == 'NO':
                print("Thanks for using XYZ bank. Please visit us next time")
                break
            #If any invalid input is provided, then break out of the loop
            else:
                print('*xxxxxxx* Invalid response! Transaction cancelled *xxxxxxx*')
                break
    #Three attempts are allowed for wrong password and post that transaction will be cancelled for security reasons
    else:
        print("Wrong password provided, enter the correct password again!")
        i += 1
        if i > 2:
            print('*' * 40)
            print("Password attempts exceeded closing the transaction...")
            print('*' * 40)
        
        