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
            elif (type == "c"):
                if (0 > status):
                    return True
            elif (type == "f"):
                if (0 > status):
                    return True
            elif (type == "m"):
                if (0 > status):
                    return True
            else:
                return False

    def notify(self, price, e_lock, c_lock, f_lock, m_lock, entertainment, clothing, food, misc):
        pass
