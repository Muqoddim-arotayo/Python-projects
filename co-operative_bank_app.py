print('\nSIGN UP PAGE')
company_register = dict(())
for each_user in range(4):
    first_name = input('\nEnter your first name >>> ')
    last_name = input('\nEnter your last name >>> ')
    phone_number = input('\nEnter your phone number >>> ')
    if not first_name or not last_name or not phone_number :
        print('do not leave any input blank')
    elif len(phone_number) < 11 or phone_number[0] != '0' and phone_number[0] != '+':
        print('input a valid phone number')
    else :
        email_address = input('\nEnter your email address >>> ')
        if '@gmail.com' in email_address :
            old_password = input('\nInput a password >>> ')
            confirm_password = input('\nconfirm your password >>> ')
            if old_password != confirm_password :
                print("password doesn't match")
            else :
                print('\nAccount creation successful')
                print(f'\nwelcome, {first_name}')
        else :  
            print('input a valid email address')
    savings = 50000
    loan = 25000
    company_register.update({f"user {each_user+1}" : {"first name":first_name,"last name":last_name,"phone number":phone_number,"email address":email_address,"password": confirm_password,"savings":savings,"loan":loan}})
    print(company_register)
    multiple_signup = input("Sign up [1], Sign in [2] >> ")
    if multiple_signup == "2":
        break
    else :
        print("Redirecting to Sign up page... ")

print("\nSIGN IN")
for itiration in range(50):
    sign_in_firstname = input("\nInput your fisrt name >> ")
    sign_in_password = input("\nInput your password >> ")
    for each_user_name, each_user_details in company_register.items():
        print(each_user_name)
        print(each_user_details)
        if sign_in_firstname == each_user_details["first name"] and sign_in_password == each_user_details["password"]:
            print(f"\nWelcome {sign_in_firstname}")
            for i in range(5):
                print("\n<< DASHBOARD >>")
                operation = input("\nSavings [1] \nloan application [2] \nloan repayment[3] ")
                if operation == '1':
                    print("\nRedirecting to savings...")
                    saving_operation = input("\nWhat savings operation do you want to perform? \nAdd [1] \nWithdraw [2] \nView [3] >> ")
                    if saving_operation == '1':
                        savings_amount = int(input("\nEnter the amount you want to save: "))
                        if savings_amount <= 0:
                            print("\nInvalid savings amount. Please enter a positive number.")
                        else:
                            print(f"\nSavings of {savings_amount} naira added successfully.")
                            each_user_details["savings"] += savings_amount
                            print(f"\nUpdated savings balance: {each_user_details["savings"]} naira")
                    elif saving_operation == '2':
                        withdrawal_amount = int(input("\nEnter the amount you want to withdraw: "))
                        if withdrawal_amount <= 0:
                            print("\nInvalid savings amount. Please enter a positive number.")
                        else:
                            print(f"\nWithdrwal of {withdrawal_amount} naira done successfully.")
                            each_user_details["savings"] -= withdrawal_amount
                            print(f"\nUpdated savings balance: {each_user_details["savings"]} naira")
                    elif saving_operation == '3':
                        print(f"\nCurrent savings balance: {each_user_details["savings"]} naira")
                elif operation == '2':
                    print("\nRedirecting to loan application...")
                    print(f"\nCurrent loan balance: {each_user_details["loan"]} naira")
                    application_operation = input("\nWhat Loan application operation do you want to perform? \nApply for loan [1] \nInterest rate calculator [2] \nView loan balance [3] >> ")
                    if application_operation == "1":
                        loan_amount = int(input("\nEnter the amount you want to apply for: "))
                        if loan_amount <= 0:
                            print("Invalid loan amount. Please enter a positive number.")
                        else:
                            loan_loan = loan_amount+each_user_details["loan"]
                            loan_not = each_user_details["savings"]*2
                            if loan_loan > loan_not :
                                print(f"\nYou have exceeded your loan threshold, you can only collect {each_user_details["savings"]*2 - each_user_details["loan"]}")
                            else :
                                print(f"\nLoan application for {loan_amount} naira submitted successfully.")
                                interest = loan_amount*0.1
                                print(f"\nInterest on loan is {interest}, You are to pay {loan_amount + interest}")
                                each_user_details["loan"] += loan_amount + interest
                                print(f"\nUpdated loan balance: {each_user_details["loan"]} naira")
                    elif application_operation == "2":
                        amount_calc = int(input("\nEnter the amount you want to calculate: "))
                        duration_calc = int(input("\nHow many month: "))
                        repay_amount_calc = amount_calc + amount_calc * 0.1
                        print("\nLoan interest rate = 10%")
                        print(f"\nTotal interest = {amount_calc*0.1}")
                        print(f"\nMonthly repayment = {amount_calc/duration_calc}")
                        print(f"\nTotal repayment = {amount_calc}")
                    elif application_operation == "3":
                        print(f"Current Loan outstanding balance: {each_user_details["loan"]} naira")
                elif operation == '3':
                    print("\nRedirecting to loan repayment...")
                    amount_repay = int(input("\nHow much do you want to pay ? "))
                    each_user_details["loan"] -= amount_repay
                    print(f"\nUpdated loan outstanding is {each_user_details["loan"]} naira")
                else:
                    print("Invalid operation selected.")
        else:
            print("\nAccount does not exit !!! ")
    exit_option = input("Log out [1], Go to Sign In [2] >> ")
    if exit_option == "1":
        break
    else :
        print("Redirecting to Sign in page... ")