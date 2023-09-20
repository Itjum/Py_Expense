from PyInquirer import prompt

import csv

user_questions = [
    {
        "type":"input",
        "name":"user",
        "message":"New User - Name:",
    }
]

def add_user():
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\n', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos['user']])
    print("User added")
    return