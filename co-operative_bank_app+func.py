print("CO-OPERATIVE BANK APP")
company_register = dict(())
each_user = 0
def increment():
    global each_user
    each_user += 1
    print(each_user)
    return each_user
increment()
def sign_up():
    first_name = input("\nEnter your first name : ")
    last_name = input("\nEnter your last name : ")
    phone_number = input('\nEnter your phone number : ')
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
    company_register.update({f"user {each_user}" : {"first name":first_name,"last name":last_name,"phone number":phone_number,"email address":email_address,"password": confirm_password,"savings":savings,"loan":loan}})
    print(company_register)

def sign_in() :
    sign_in_firstname = input("\nInput your fisrt name >> ")
    sign_in_password = input("\nInput your password >> ")
    if company_register[f"user {each_user+1}"]["first name"] == sign_in_firstname and company_register[f"user {each_user+1}"]["password"] == sign_in_password:
        print("\nWelcome  to the dashboard")
    else:
        print("\nAccount does not exist ? ")
        red_signin = input("\nSign in [1] | Sign up [2] : ")
        if red_signin == "1":
            print("Redirecting to sig in page...")
            sign_in()
        else:
            print("\nRedirecting to sign up page...")
            sign_up()

# sign_up()
# sign_in()

