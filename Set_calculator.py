print("SET CALCULATOR")
user_operation = input("Which of the operations will you like to perform: Differnce [D], Intersection [I], Union [U] >> ").upper()
if user_operation == "D":
    print("DIFFERENCE")
    main_set = list(())
    number_of_set = int(input("\nHow many sets do you want to operate with >> "))
    set_number = 0
    for set_index in range(number_of_set):
        set_number += 1
        sub_set = set(())
        number_of_set_characters = int(input(f"\nHow many values does set {set_number} have >> "))
        for character_index in range(number_of_set_characters):
            values = input(f"\nInput your {character_index+1} value >> ")
            sub_set.add(values)
        if set_index+1 == 1 :
            first_set = sub_set
            print(first_set)
            main_set.append(first_set)
        elif set_index+1 == 2 :
            second_set = sub_set
            print(second_set)
            main_set.append(second_set)
        elif set_index+1 == 3 :
            third_set = sub_set
            print(third_set)
            main_set.append(third_set)
    if set_number == 2:
        third_set = set(())
    diff_set = first_set.difference(second_set, third_set)
    print("\n")
    print(f"The DIFFERENCE of the sets is {diff_set}\n")
elif user_operation == "I":
    print("INTERSECTION\n")
    main_set = list(())
    number_of_set = int(input("\nHow many sets do you want to operate with >> "))
    set_number = 0
    for set_index in range(number_of_set):
        set_number += 1
        sub_set = set(())
        number_of_set_characters = int(input("\nHow many values does this set have >> "))
        for character_index in range(number_of_set_characters):
            values = input(f"\nInput your {character_index+1} value >> ")
            sub_set.add(values)
        if set_index+1 == 1 :
            first_set = sub_set
            print(first_set)
            main_set.append(first_set)
        elif set_index+1 == 2 :
            second_set = sub_set
            print(second_set)
            main_set.append(second_set)
        elif set_index+1 == 3 :
            third_set = sub_set
            print(third_set)
            main_set.append(third_set)
    if set_number == 2:
        third_set = set(())
    inter_set = first_set.intersection(second_set, third_set)
    print("\n")
    print(f"The INTERSECTION of the sets is {inter_set}\n")
elif user_operation == "U":
    print("UNION\n")
    main_set = list(())
    number_of_set = int(input("\nHow many sets do you want to operate with >> "))
    set_number = 0
    for set_index in range(number_of_set):
        set_number += 1
        sub_set = set(())
        number_of_set_characters = int(input("\nHow many values does this set have >> "))
        for character_index in range(number_of_set_characters):
            values = input(f"\nInput your {character_index+1} value >> ")
            sub_set.add(values)
        if set_index+1 == 1 :
            first_set = sub_set
            print(first_set)
            main_set.append(first_set)
        elif set_index+1 == 2 :
            second_set = sub_set
            print(second_set)
            main_set.append(second_set)
        elif set_index+1 == 3 :
            third_set = sub_set
            print(third_set)
            main_set.append(third_set)
    if set_number == 2:
        third_set = set(())
    union_set = first_set.union(second_set, third_set)
    print("\n")
    print(f"The UNION of the sets is {union_set}\n")
else :
    print("Input a valid option")
            