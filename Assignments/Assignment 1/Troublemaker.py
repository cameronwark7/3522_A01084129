from User import User


class Troublemaker(User):
    def __init__(self, name, age, bank_num, bank_name, bank_bal):
        super().__init__(name, age, bank_num, bank_name, bank_bal)

    def lock_set(self, lock, type, status):
        if (lock == True):
            return True
        elif (lock == False):
            if (type == "e"):
                if (self._initial_e - (self._initial_e * 1.2) > status):
                    return True
                else:
                    return False
            elif (type == "c"):
                if (self._initial_c - (self._initial_c * 1.2) > status):
                    return True
                else:
                    return False
            elif (type == "f"):
                if (self._initial_f - (self._initial_f * 1.2) > status):
                    return True
                else:
                    return False
            elif (type == "m"):
                if (self._initial_m - (self._initial_m * 1.2) > status):
                    return True
                else:
                    return False
            else:
                return False

    def notify(self, price, e_lock, c_lock, f_lock, m_lock, entertainment, clothing, food, misc):
        if (entertainment < (0 - self._initial_e * 0.20)):
            print("WARNING: Entertainment Budget Exceeded; LOCKED OUT")
        elif ((self._initial_e * 0.75) > (entertainment)):
            print("WARNING: Less than 25% of Misc Budget Left")
        if (clothing < (0 - self._initial_c * 0.20)):
            print("WARNING: Clothing Budget Exceeded; LOCKED OUT")
        elif ((self._initial_c * 0.75) > (clothing)):
            print("WARNING: Less than 25% of Misc Budget Left")
        if (food < (0 - self._initial_f * 0.20)):
            print("WARNING: Food Budget Exceeded; LOCKED OUT")
        elif ((self._initial_f * 0.75) > (food)):
            print("WARNING: Less than 25% of Misc Budget Left")
        if (misc < (0 - self._initial_m * 0.20)):
            print("WARNING: Misc Budget Exceeded; LOCKED OUT")
        elif ((self._initial_m * 0.75) > (misc)):
            print("WARNING: Less than 25% of Misc Budget Left")
