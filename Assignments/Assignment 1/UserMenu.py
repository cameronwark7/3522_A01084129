from RecordMenu import RecordMenu
from ViewTransactions import ViewTransactions

class UserMenu:
    def __init__(self, user, budget):
        self._user = user
        self._budget = budget
        self._record_menu = RecordMenu(self._user, self._budget)
        self._view_transactions_menu = ViewTransactions(self._budget)

    def view_budgets(self):
        #Selecting this option should show the user the current status of their budgets
        #(locked or not) in addition to the amount spent, amount left, and the total
        #amount allocated to the budget
        status = "Locked"
        if not self._budget.get_entertainment_lock():
            status = "Unlocked"
        print("Games and Entertainment: " + status)
        print("Amount spent: " + str(self._user._initial_e - self._budget._entertainment))
        print("Amount left: " + str(self._budget._entertainment))
        print("Total amount allocated: " + str(self._user._initial_e))
        print("")
        if not self._budget.get_clothing_lock():
            status = "Unlocked"
        else:
            status = "Locked"
        print("Clothing and Accessories: " + status)
        print("Amount spent: " + str(self._user._initial_c - self._budget._clothing))
        print("Amount left: " + str(self._budget._clothing))
        print("Total amount allocated: " + str(self._user._initial_c))
        print("")
        if not self._budget.get_food_lock():
            status = "Unlocked"
        else:
            status = "Locked"
        print("Eating Out: " + status)
        print("Amount spent: " + str(self._user._initial_f - self._budget._food))
        print("Amount left: " + str(self._budget._food))
        print("Total amount allocated: " + str(self._user._initial_f))
        print("")
        if not self._budget.get_misc_lock():
            status = "Unlocked"
        else:
            status = "Locked"
        print("Miscellaneous: " + status)
        print("Amount spent: " + str(self._user._initial_m - self._budget._misc))
        print("Amount left: " + str(self._budget._misc))
        print("Total amount allocated: " + str(self._user._initial_m))
        print("")

    def view_acc_details(self):
        print("---------------------------")
        print("Bank Account Number: " + str(self._user.get_bank_num()))
        print("Bank Account Name: " + self._user.get_bank_name())
        self._budget.print_all_transactions()

        print("Closing Balance: $" + str(self._user.get_bank_bal()))
        print("---------------------------")

    def display(self):
        print("1. View Budgets")
        print("2. Record a Transaction")
        print("3. View Transactions by Budget")
        print("4. View Bank Account Details")
        val = input("Select 1-4: ")

        if val == "1":
            print("---------------------------")
            self.view_budgets()
        elif val == "2":
            self._record_menu.choice_display()
        elif val == "3":
            self._view_transactions_menu.choice_display()
        elif val == "4":
            self.view_acc_details()
        else:
            print("INVALID INPUT")
            print("---------------------------")
        self.display()
