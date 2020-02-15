from User import User
from Budget import Budget
from UserMenu import UserMenu
from Angel import Angel
from Troublemaker import Troublemaker
from Rebel import Rebel


class UserInit:
    def __init__(self):
        self._user = None
        self._budget = None

    def initialize(self):
        print("1. Register a user")
        print("2. Load a premade user")
        num = input("Select 1 or 2: ")
        if num == "1":
            self._user = self.create_user()
            self._budget = self.create_budget()
        elif num == "2":
            self._user = self.load_test_user()
            self._budget = self.load_test_budget()
        else:
            print("Please enter a valid value")
            print("--------------------------")
            self.initialize()
        print("--------------------------")

    def create_user(self):
        name = input("Enter user's name: ")
        age = input("Enter user age: ")
        bank_num = input("Enter bank account number: ")
        bank_name = input("Enter bank name: ")
        bank_bal = input("Enter bank balance: ")
        type = self.get_type()
        if type == "1":
            return Angel(name, age, bank_num, bank_name, bank_bal)
        elif type == "2":
            return Troublemaker(name, age, bank_num, bank_name, bank_bal)
        elif type == "3":
            return Rebel(name, age, bank_num, bank_name, bank_bal)

    def get_type(self):
        print("1. Angel")
        print("2. Troublemaker")
        print("3. Rebel")
        val = input("Select 1-3: ")

        if val == "1":
            return "1"
        elif val == "2":
            return "2"
        elif val == "3":
            return "3"
        else:
            print("INVALID INPUT")
            print("---------------------------")
        self.get_type()

    def create_budget(self):
        entertainment = input("Enter budget for games and entertainment: ")
        clothing = input("Enter budget for clothing and accessories: ")
        food = input("Enter budget for eating out: ")
        misc = input("Enter budget for miscellaneous needs: ")

        return Budget(self._user, entertainment, clothing, food, misc)

    def load_test_user(self):
        user = Angel("John", 17, 41, "Vancity", 700.00)
        return user

    def load_test_budget(self):
        budget = Budget(self._user, 50, 100, 200, 150)
        return budget

def main():
    user_init = UserInit()
    user_init.initialize()
    user = user_init._user
    budget = user_init._budget
    menu = UserMenu(user, budget)
    menu.display()

if __name__ == '__main__':
    main()