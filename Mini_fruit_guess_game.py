import random

print("\nMINI GUESS GAME")
Fruits = [
    "Orange", "Apple", "Pineapple", "Guava", "Banana"
]
for Fruit in Fruits :
    user_fruit = input("\nInput a Fruit : ").capitalize()
    random_fruit = random.choice(Fruits)
    print("---------------------------------")
    print(f"Your choice : {user_fruit} \nComputer's choice : {random_fruit}")
    print("---------------------------------")
    if user_fruit.capitalize() == random_fruit:
        print("\nYou've won a lottery !!\n")
        retry_option = input("Do you wish to continue Y/N >> ")
        if retry_option.upper() != "Y":
            break
    elif user_fruit.capitalize() in Fruits : 
        print("\nTry again next time !!\n")
        print(Fruits)
        retry_option = input("Do you wish to continue Y/N >> ")
        if retry_option.upper() != "Y":
            break
    else:
        print("\nTry again next time !!\n")
        Fruits.append(user_fruit.capitalize())
        print(Fruits)
        retry_option = input("Do you wish to continue Y/N >> ")
        if retry_option.upper() != "Y":
            break