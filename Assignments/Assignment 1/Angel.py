from User import User


class Angel(User):
    def __init__(self, name, age, bank_num, bank_name, bank_bal):
        super().__init__(name, age, bank_num, bank_name, bank_bal)

    def lock_set(self, lock, type, status):
        return False

    def notify(self, price, e_lock, c_lock, f_lock, m_lock, entertainment, clothing, food, misc):
        if (entertainment < 0):
            print("WARNING: Entertainment Budget Exceeded")
        elif ((entertainment * 0.1) < (self._initial_e - entertainment)):
            print("WARNING: Less than 10% of Entertainment Budget Left")
        if (clothing < 0):
            print("WARNING: Clothing Budget Exceeded")
        elif ((clothing * 0.1) < (self._initial_c - clothing)):
            print("WARNING: Less than 10% of Clothing Budget Left")
        if (food < 0):
            print("WARNING: Food Budget Exceeded")
        elif ((food * 0.1) < (self._initial_f - food)):
            print("WARNING: Less than 10% of Food Budget Left")
        if (misc < 0):
            print("WARNING: Misc Budget Exceeded")
        elif ((misc * 0.1) < (self._initial_m - misc)):
            print("WARNING: Less than 10% of Misc Budget Left")

