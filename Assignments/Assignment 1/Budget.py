from datetime import datetime
from Rebel import Rebel


class Budget:
    def __init__(self, user, entertainment, clothing, food, misc):
        self._user = user
        self._entertainment = float(entertainment)
        self._clothing = float(clothing)
        self._food = float(food)
        self._misc = float(misc)
        self._user._initial_e = float(entertainment)
        self._user._initial_c = float(clothing)
        self._user._initial_f = float(food)
        self._user._initial_m = float(misc)
        self._entertainment_lock = False
        self._clothing_lock = False
        self._food_lock = False
        self._misc_lock = False
        self._transactions = []

    def get_food_lock(self):
        return self._food_lock

    def get_entertainment_lock(self):
        return self._entertainment_lock

    def get_clothing_lock(self):
        return self._clothing_lock

    def get_misc_lock(self):
        return self._misc_lock

    def return_transactions(self, t_type):
        if t_type == "entertainment":
            for x in self._transactions:
                if x[2] == "Entertainment":
                    print(x[0] + " | $" + str(x[1]) + " | "
                          + x[2] + " | " + x[3])
        elif t_type == "clothing":
            for x in self._transactions:
                if x[2] == "Clothing":
                    print(x[0] + " | $" + str(x[1]) + " | "
                          + x[2] + " | " + x[3])
        elif t_type == "food":
            for x in self._transactions:
                if x[2] == "Food":
                    print(x[0] + " | $" + str(x[1]) + " | "
                          + x[2] + " | " + x[3])
        elif t_type == "misc":
            for x in self._transactions:
                if x[2] == "Misc":
                    print(x[0] + " | $" + str(x[1]) + " | "
                          + x[2] + " | " + x[3])
        else:
            pass
        print("--------------------")

    def general_record(self, price, type):
        price = float(price)

        if type == "Entertainment":
            self._entertainment -= price
            self._user.bank_bal -= price
        elif type == "Clothing":
            self._clothing -= price
            self._user.bank_bal -= price
        elif type == "Food":
            self._food -= price
            self._user.bank_bal -= price
        elif type == "Misc":
            self._misc -= price
            self._user.bank_bal -= price

        store = input("Where did this purchase take place? ")
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        transaction = (date_time, price, type, store)
        self._transactions.append(transaction)

        print("TRANSACTION RECORDED")
        print(transaction[0] + " | $" + str(transaction[1]) + " | "
              + transaction[2] + " | " + transaction[3])
        print("--------------------")

    def entertainment_record(self, price):
        result = False
        result = self._full_lockout()
        if (self._entertainment_lock == False):
            self.general_record(price, "Entertainment")
        else:
            if result == False:
                print("Locked out of this budget category")

        lock_result = self._user.lock_set(self._entertainment_lock, "e", self._entertainment)
        self._entertainment_lock = lock_result

        self._user.notify(price, self._entertainment_lock, self._clothing_lock, self._food_lock, self._misc_lock,
                          self._entertainment, self._clothing, self._food, self._misc)

    def clothing_record(self, price):
        result = False
        result = self._full_lockout()
        if (self._clothing_lock == False):
            self.general_record(price, "Clothing")
        else:
            if result == False:
                print("Locked out of this budget category")

        lock_result = self._user.lock_set(self._clothing_lock, "c", self._clothing)
        self._clothing_lock = lock_result

        self._user.notify(price, self._entertainment_lock, self._clothing_lock, self._food_lock, self._misc_lock,
                          self._entertainment, self._clothing, self._food, self._misc)

    def food_record(self, price):
        result = False
        result = self._full_lockout()
        if (self._food_lock == False):
            self.general_record(price, "Food")
        else:
            if result == False:
                print("Locked out of this budget category")

        lock_result = self._user.lock_set(self._food_lock, "f", self._food)
        self._food_lock = lock_result

        self._user.notify(price, self._entertainment_lock, self._clothing_lock, self._food_lock, self._misc_lock,
                          self._entertainment, self._clothing, self._food, self._misc)

    def misc_record(self, price):
        result = False
        result = self._full_lockout()
        if (self._misc_lock == False):
            self.general_record(price, "Misc")
        else:
            if result == False:
                print("Locked out of this budget category")

        lock_result = self._user.lock_set(self._misc_lock, "m", self._misc)
        self._misc_lock = lock_result


        self._user.notify(price, self._entertainment_lock, self._clothing_lock, self._food_lock, self._misc_lock,
                          self._entertainment, self._clothing, self._food, self._misc)

    def _full_lockout(self):
        if (type(self._user) == Rebel):
            i = 0
            if (self._entertainment_lock == True):
                i = i + 1
            if (self._clothing_lock == True):
                i = i + 1
            if (self._food_lock == True):
                i = i + 1
            if (self._misc_lock == True):
                i = i + 1
            if (i >= 2):
                self._entertainment_lock = True
                self._clothing_lock = True
                self._food_lock = True
                self._misc_lock = True
                print("LOCKED OUT OF ACCOUNT")
        return True