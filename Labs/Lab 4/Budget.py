from datetime import datetime

class Budget:
    def __init__(self, entertainment, clothing, food, misc):
        self._entertainment = float(entertainment)
        self._clothing = float(clothing)
        self._food = float(food)
        self._misc = float(misc)
        self._transactions = []

    def general_record(self, price, type):
        price = float(price)

        if type == "Entertainment":
            self._entertainment -= price
        elif type == "Clothing":
            self._clothing -= price
        elif type == "Food":
            self._food -= price
        elif type == "Misc":
            self._misc -= price

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
        self.general_record(price, "Entertainment")

    def clothing_record(self, price):
        self.general_record(price, "Clothing")

    def food_record(self, price):
        self.general_record(price, "Food")

    def misc_record(self, price):
        self.general_record(price, "Misc")
