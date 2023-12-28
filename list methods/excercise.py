people = []

    
def main():
    try:
        while True:
            print('\nOptions')
            print('1.add name')
            print('2.remove name')
            print('3.append name')
            print('4.insert name')
            print('5.pop name')
            print('6.reverse order')
            print('7.extent list')
            print('8.get numbers and sort')
            print('0.Exit')
            
            choice = int(input('Enter your choice(0-8): '))
            
            if choice == 1:
                name = input('Enter name: ')
                people.append(name)
                print(people)
            elif choice == 2:
                name  = input('enter name to remove: ')
                people.remove(name)
                print(people)
            elif choice == 3:
                name_to_append = input('enter name: ')
                people.append(name_to_append)
                print(people)
            elif choice == 4:
                name_to_insert = input('enter name: ')
                position = int(input('enter index to add: '))
                people.insert(position,name_to_insert)
                print(people)
            elif choice == 5:
                index = int(input('enter index number to remove: '))
                people.pop(index)
                print(people)
            elif choice == 6:
                people.reverse()
                print(people)
                
            elif choice == 7:
               name = input('enter name to extent: ')
               people.extend([name])
               print(people)
            elif choice == 8:
               people.sort()
               print(people)  
            elif choice == 0:
                break
    except ValueError as e:
        print(f"error: {e}")
if __name__ == "__main__":
    main()                