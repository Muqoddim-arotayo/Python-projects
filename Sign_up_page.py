print('SIGN UP PAGE')
first_name = input('Enter your first name >>> ')
last_name = input('Enter your last name >>> ')
phone_number = input('enter your phone number >>> ')
if not first_name or not last_name or not phone_number :
    print('do not leave any input blank')
elif len(phone_number) < 11 or phone_number[0] != '0' and phone_number[0] != '+':
    print('input a valid phone number')
else :
    email_address = input('enter your email address >>> ')
    if '@gmail.com' in email_address :
        old_password = input('Input a password >>> ')
        confirm_password = input('\nconfirm your password >>> ')
        if old_password != confirm_password :
            print("password doesn't match")
        else :
            print('Account creation successful')
            print(f'welcome, {first_name}')
            password_change_option = input('Change passowrd [1] | Forget Password [2] >>>')
            if password_change_option == '1' :
                if old_password != confirm_password :
                    print("\npassword doesn't match")
                else :
                    print('\nAccount creation successful')
                    print(f'Your password is {confirm_password}\t')
                    change_password = input('\nInput your new password >>> ')
                    confirm_password.replace(confirm_password,change_password)
                    print(f'\nYour new password is {change_password}')
            else :
                print('forgot password in development')
    else :  
        print('input a valid email address')