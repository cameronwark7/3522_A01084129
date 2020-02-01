class RecordMenu:
    def __init__(self, user, budget):
        self._user = user
        self._budget = budget

    def choice_display(self):
        print("What type of transaction?")
        print("1. Games and Entertainment")
        print("2. Clothing and Accessories")
        print("3. Eating Out")
        print("4. Miscellaneous")
        val = input("Choose 1 - 4: ")
        choice = int(val)
        price = self.get_price()
        repeat = None

        if choice == 1:
            self._budget.entertainment_record(price)
            repeat = self.success()
        elif choice == 2:
            self._budget.clothing_record(price)
            repeat = self.success()
        elif choice == 3:
            self._budget.food_record(price)
            repeat = self.success()
        elif choice == 4:
            self._budget.misc_record(price)
            repeat = self.success()
        else:
            print("Please enter a valid number: ")
            print("---------------------------")
            self.choice_display()

        if repeat == "y":
            self.choice_display()

    def success(self):
        while 1:
            response = input("Another transaction? (y/n): ")
            if response != "y":
                if response != "n":
                    print("INVALID INPUT")
            if response == "y":
                break
            if response == "n":
                break
        print("--------------------")
        return response

    def get_price(self):
        price = input("Enter cost of purchase: ")
        return price
