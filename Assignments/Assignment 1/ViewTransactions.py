class ViewTransactions:
    def __init__(self, budget):
        self._budget = budget

    def choice_display(self):
        print("--------------------")
        print("What type of transaction?")
        print("1. Games and Entertainment")
        print("2. Clothing and Accessories")
        print("3. Eating Out")
        print("4. Miscellaneous")
        print("5. Back")
        choice = input("Choose 1 - 5: ")

        if choice == "1":
            self._budget.return_transactions("entertainment")
        elif choice == "2":
            self._budget.return_transactions("clothing")
        elif choice == "3":
            self._budget.return_transactions("food")
        elif choice == "4":
            self._budget.return_transactions("misc")
        elif choice == "5":
            return
        else:
            print("INVALID INPUT")
            self.choice_display()
