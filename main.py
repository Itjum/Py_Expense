from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions,new_expense
from user import add_user

import csv

def calculate_expense_summary():
    expenses = []
    with open('expense_report.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            expenses.append(row)

    total_expenses = {}
    for expense in expenses:
        amount = float(expense[0])
        users = expense[2:]  

        for user in users:
            total_expenses[user] = total_expenses.get(user, 0) + amount

    num_users = len(total_expenses)
    total_cost = sum(total_expenses.values())
    average_cost = total_cost / num_users

    reimbursements = {}
    for user, expense in total_expenses.items():
        reimbursements[user] = average_cost - expense

    return reimbursements

def ask_option():
    main_option = {
        "type":"list",
        "name":"main_options",
        "message":"Expense Tracker v0.1",
        "choices": ["New Expense","Show Status","New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()
    elif (option['main_options']) == "Show Status":
        reimbursements = calculate_expense_summary()

        print(f"Expense Summary: {len(reimbursements)} Users")

        owes = {user: {} for user in reimbursements.keys()}

        for user1, amount in reimbursements.items():
            if amount > 0:
                for user2, owed_amount in reimbursements.items():
                    if user1 != user2 and owed_amount < 0:
                        reimbursement_amount = min(amount, abs(owed_amount))
                        if reimbursement_amount > 0:
                            if user2 not in owes[user1]:
                                owes[user1][user2] = reimbursement_amount
                            else:
                                owes[user1][user2] += reimbursement_amount
                            amount -= reimbursement_amount

        for user1, user2_dict in owes.items():
            print(f"{user1} needs to reimburse:")
            if sum(user2_dict.values()) > 0: 
                for user2, amount in user2_dict.items():
                    print(f"- {amount:.2f}€ to {user2}")
            else:
                print("- nothing")

    elif (option['main_options']) == "New User":
        add_user()

def main():
    ask_option()

main()