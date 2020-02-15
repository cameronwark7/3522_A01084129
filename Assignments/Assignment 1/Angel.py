from User import User


class Angel(User):
    def __init__(self, name, age, bank_num, bank_name, bank_bal):
        super().__init__(name, age, bank_num, bank_name, bank_bal)

    def lock_set(self, lock, type, status):
        return False

    def notify(self, price, e_lock, c_lock, f_lock, m_lock, entertainment, clothing, food, misc):
        if (entertainment < 0):
            print("WARNING: Entertainment Budget Exceeded")
        elif ((self._initial_e * 0.1) > (entertainment)):
            print("WARNING: Less than 10% of Entertainment Budget Left")
        if (clothing < 0):
            print("WARNING: Clothing Budget Exceeded")
        elif ((self._initial_c * 0.1) > (clothing)):
            print("WARNING: Less than 10% of Clothing Budget Left")
        if (food < 0):
            print("WARNING: Food Budget Exceeded")
        elif ((self._initial_f * 0.1) > (food)):
            print("WARNING: Less than 10% of Food Budget Left")
        if (misc < 0):
            print("WARNING: Misc Budget Exceeded")
        elif ((self._initial_m * 0.1) > (misc)):
            print("WARNING: Less than 10% of Misc Budget Left")

