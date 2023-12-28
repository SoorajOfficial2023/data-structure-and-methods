text = 'hello'
result = text.center(20)
print(result)
#center method

text = "apple,orange,grape,apple"
result = text.count('apple')
print(result)
#count method

file_name = 'document.txt'
result = file_name.endswith('.txt')
print(result)
#endswith method

file_name = 'document.txt'
result = file_name.startswith('document')
print(result)
#startswith method

word = 'artificial inteligence'
result = word.find('inteligence')
print(result)
#find method ; return -1 if not found

text = "this is {} and {}"
formatted_text = text.format('one','two')
print(formatted_text)
#1

text = "My name is {name}, I'm {age} years old"
formatted_text = text.format(name='jhone',age=30)
print(formatted_text)
#2

name = 'jhone'
age = 25
city = 'newyork'
formated_text = "My name is {},I'm {} years old,my city is {}".format(name,age,city)
print(formated_text)
#3
#format methods

sentance = 'Hello, world!'
position = sentance.index('world')
print(f"The word 'world' is found at position: ",position)
#index method

alphanumeric_string = "abc123@"
print(alphanumeric_string.isalnum())

non_alphanumeric_string = "abc123"
print(non_alphanumeric_string.isalnum())
#alphanumeric method

ascii_letters = 'hello'
print(ascii_letters.isascii())

non_ascii_letters = '你好'
print(non_ascii_letters.isascii())
#ascii method

numeric_str = '123'
print(numeric_str.isdigit())

non_numeric_str = 'abc123'
print(non_numeric_str.isdigit())
#isdigit method

title = "  "
print(title.isspace())

non_space = 'hello'
print(non_space.isspace())
#isspace method

title_word = 'Hello, Welcome'
x = title_word.istitle()
print(x)

non_title = 'the market'
y = non_title.istitle()
print(non_title.istitle())
#istitle method

seperator = ' '
words = ['this','is','an','apple']
joined_string = seperator.join(words)
print(joined_string)
#join() method

text = "apple,orange,grape"
fruits = text.split(",")
print(fruits)
#split method

text = "apple,orange,grape,pinapple"
fruits = text.split(",",maxsplit=1)
print(fruits)
#maxsplit= method