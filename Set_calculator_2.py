print("SET CALCULATOR 2.0")
user_set = int(input("How many sets do you want to operate with? >> "))
main_set = list(())
set_number = 0
for each_set in range(user_set) :
    sub_set = set(())
    number_of_set_characters = int(input(f"\nHow many values does set {each_set+1} have >> "))
    for character_index in range(number_of_set_characters):
        values = input(f"\nInput your {character_index+1} value >> ")
        sub_set.add(values)
    set_number += 1
    if set_number == 1:
        first_set = sub_set
        print(first_set)
        main_set.append(first_set)
    elif set_number == 2:
        second_set = sub_set
        print(second_set)
        main_set.append(second_set)
    elif set_number == 3:
        third_set = sub_set
        print(third_set)
        main_set.append(third_set)
    if set_number == 2:
        third_set = set(())
for i in range(10):
    operations = input("\nWhich of the operations will you like to perform on these set: Differnce [D], Intersection [I], Union [U] >> ")
    if operations.upper() == "D":
        diff_set = first_set.difference(second_set, third_set)
        print("\n")
        print(f"The DIFFERENCE of the sets is {diff_set}\n")
    elif operations.upper() == "I":
        inter_set = first_set.intersection(second_set, third_set)
        print("\n")
        print(f"The INTERSECTION of the sets is {inter_set}")
    elif operations.upper() == "U":
        union_set = first_set.union(second_set,third_set)
        print("\n")
        print(f"The UNION of the sets is {union_set}")
    else:
        print("\nInvalid operation selected. Please choose from [D], [I], or [U].")