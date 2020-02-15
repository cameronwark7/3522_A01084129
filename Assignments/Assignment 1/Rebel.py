from User import User


class Rebel(User):
    def __init__(self, name, age, bank_num, bank_name, bank_bal):
        super().__init__(name, age, bank_num, bank_name, bank_bal)

    def lock_set(self, lock, type, status):
        if (lock == True): # if they are already locked out then keep them locked out
            return True
        elif (lock == False):
            if (type == "e"):
                if (0 > status):
                    return True
                else:
                    return False
            elif (type == "c"):
                if (0 > status):
                    return True
                else:
                    return False
            elif (type == "f"):
                if (0 > status):
                    return True
                else:
                    return False
            elif (type == "m"):
                if (0 > status):
                    return True
                else:
                    return False
            else:
                return False

    def notify(self, price, e_lock, c_lock, f_lock, m_lock, entertainment, clothing, food, misc):
        if (entertainment < 0):
            print("WARNING: Entertainment Budget Exceeded; LOCKED OUT")
        elif ((self._initial_e * 0.5) > (entertainment)):
            print("WARNING: Less than 50% of Entertainment Budget Left")
        if (clothing < 0):
            print("WARNING: Clothing Budget Exceeded; LOCKED OUT")
        elif ((self._initial_c * 0.5) > (clothing)):
            print("WARNING: Less than 50% of Clothing Budget Left")
        if (food < 0):
            print("WARNING: Food Budget Exceeded; LOCKED OUT")
        elif ((self._initial_f * 0.5) > (food)):
            print("WARNING: Less than 50% of Food Budget Left")
        if (misc < 0):
            print("WARNING: Misc Budget Exceeded; LOCKED OUT")
        elif ((self._initial_m * 0.5) > (misc)):
            print("WARNING: Less than 50% of Misc Budget Left")
