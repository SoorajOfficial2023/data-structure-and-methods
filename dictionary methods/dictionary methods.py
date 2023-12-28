student_data = {'appu':12,'athira':14}
student_data.clear()
print(student_data)
#clear method

student_data = {'appu':12,'athira':14}
copied_data=student_data.copy()
print(copied_data)
#copy method

topics = ['ML','NLP','CV']
value = 'AI'
ai_dict = dict.fromkeys(topics,value)
print(ai_dict)
#fromkeys method

topics = {'ML': 'AI', 'NLP': 'AI', 'CV': 'AI'}
ML_value = topics.get('ML','Not found')
print(ML_value)
#get method

topics = {'ML': 'AI', 'NLP': 'AI', 'CV': 'AI'}
items_list = topics.items()
print(items_list)
#items method

topics = {'ML': 'AI', 'NLP': 'AI', 'CV': 'AI'}
topics.pop('ML')
print(topics)
#pop method

content = {'name':'jhone','age':25,'city':'newyork'}
content.popitem()
print(content)
#popitem method

student_score = {'alice':85,'bob':90,'charlie':65}
alice_score = student_score.setdefault('alice',0)
print(f"Alice's score: {alice_score}")

david_score = student_score.setdefault('david',0)
print(f"david's score :{david_score}")

print('Modified dictionary: ',student_score)
#setdefault method

my_dict = {}
content = {'name':'jhone','age':25,'city':'newyork'}
my_dict.update(content)
print(my_dict)
#update method

student_score = {'alice':85,'bob':90,'charlie':65}
score_list = student_score.values()
print(f'all scores: ,{score_list}')
#values method






