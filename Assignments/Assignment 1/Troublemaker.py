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
        pass
