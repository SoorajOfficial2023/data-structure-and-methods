def main():
    while True:
        f_string = input('Enter a string: ')
        capitalize = f_string.upper()
        print(capitalize)

        width_for_str = int(input('enter width for centering: '))
        result = f_string.center(width_for_str)
        print(f"centered string: {result}")

        sub_string = input('enter a substring to count: ')
        count_result = f_string.count(sub_string)
        print(count_result)

        suffix_string = input('enter a suffix to check at the end: ')
        suffix_end = f_string.endswith(sub_string)
        print(f"ends with {sub_string} : {suffix_end}")

        sub_str = input('enter a sub string to find: ')
        result_count = f_string.find(sub_string)
        print(f"index of {sub_str} : {result_count}")

        name = input('enter your name: ')
        age = input('enter your age: ')
        formated_data = "My name is {},I'm {} years old".format(name,age)
        print(formated_data)
        
    
if __name__ == "__main__":
    main()





