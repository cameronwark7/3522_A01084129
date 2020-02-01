from RecordMenu import RecordMenu

class UserMenu:
    def __init__(self, user, budget):
        self._user = user
        self._budget = budget
        self._record_menu = RecordMenu(self._user, self._budget)

    def display(self):
        print("1. View Budgets")
        print("2. Record a Transaction")
        print("3. View Transactions by Budget")
        print("4. View Bank Account Details")
        val = input("Select 1-4")
        val = int(val)

        if val == 2:
            self._record_menu.choice_display()
