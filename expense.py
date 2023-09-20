from PyInquirer import prompt

import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]



def new_expense(*args):
    existing_users = []
    with open('users.csv', 'r') as userfile:
        reader = csv.reader(userfile)
        for row in reader:
            existing_users.append(row[0])

    user_question = {
        "type": "list",
        "name": "selected_user",
        "message": "Select a user:",
        "choices": existing_users
    }

    num_users_to_select = int(input("Enter the number of users to select (selecting 0 means all users paid): "))

    selected_users = []
    for i in range(num_users_to_select):
        user_question = {
            "type": "list",
            "name": "selected_user",
            "message": "Select a user:",
            "choices": existing_users
        }

        user_answer = prompt(user_question)
        selected_user = user_answer['selected_user']
        selected_users.append(selected_user)

    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        row_data = [infos['amount'], infos['label']] + selected_users 
        spamwriter.writerow(row_data)
    print("Expense Added !")
    return True


