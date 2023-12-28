name = ['sooraj','arya','abhijith']
program = ['python','css']
name.extend(program)
print(name)
#extend method

languages = ['python','css','c++','java']
index_of_java = languages.index('java')
print(index_of_java)
#index method

languages = ['python','css','c++']
removed_language = languages.pop(1)
print(removed_language)
print(languages)
#pop method

languages = ['python','css','c++','java']
languages.remove('python')
print(languages)
#remove method

numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)
#reverse method

numbers = [2,4,5,1,6,3,2,0,3,4,3]
numbers.sort()
print(numbers)
#sort method