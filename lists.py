import random;
import json;
# friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']


# print(random.choice(friends))

# class User:
#     def __init__(self, name, lastname):
#         self.name = name;
#         self.lastname = lastname
#     def get_username(self):
#         return self.name + " " + self.lastname
#     pass

# user1 = User(lastname='lasia', name='kasiek')

# print('----')
# print(user1.get_username())
# print('----')

# class Question:
#     def __init__(self, text, answer):
#         self.text = text
#         self.answer = answer
#     def get_it(self):
#         return self.text +": " + self.answer

question_data = [
    {'text': 'asdf', 'id': '1'},
    {'text': 'fsdf', 'id': '2'},
    {'text': 'asgdfdf', 'id': '3'},
    {'text': 'asgdfgdf', 'id': '4'},
    {'text': 'gsdf', 'id': '5'},
]


with open('question.json') as file:
    # json.dump(question_data,file)
    d= json.load(file)
    print(d)


# data = [Question(a['text'], a['id']) for a in question_data]

# li = list(d.get_it()+ "\n" for d in data)

# print(*(d for d in data))