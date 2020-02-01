from User import User
from Budget import Budget
from UserMenu import UserMenu

class UserInit:
    def __init__(self):
        self._user = None
        self._budget = None

    def initialize(self):
        print("1. Create new user")
        print("2. Load premade user")
        num = input("Select 1 or 2:")
        if num == "1":
            self._user = User
        elif num == "2":
            self._user = self.load_test_user()
            self._budget = self.load_test_budget()
        else:
            print("Please enter a valid value")
            print("--------------------------")
            self.initialize()


    def load_test_user(self):
        user = User("John", 17, "Angel", 41, "Vancity", 200.00)
        return user

    def load_test_budget(self):
        budget = Budget(50, 100, 200, 150)
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