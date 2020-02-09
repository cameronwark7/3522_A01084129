from RecordMenu import RecordMenu
from ViewTransactions import ViewTransactions

class UserMenu:
    def __init__(self, user, budget):
        self._user = user
        self._budget = budget
        self._record_menu = RecordMenu(self._user, self._budget)
        self._view_transactions_menu = ViewTransactions(self._budget)

    def display(self):
        print("1. View Budgets")
        print("2. Record a Transaction")
        print("3. View Transactions by Budget")
        print("4. View Bank Account Details")
        val = input("Select 1-4: ")

        if val == "1":
            pass
        elif val == "2":
            self._record_menu.choice_display()
        elif val == "3":
            self._view_transactions_menu.choice_display()
        elif val == "4":
            pass
        else:
            print("INVALID INPUT")
            print("---------------------------")
        self.display()
