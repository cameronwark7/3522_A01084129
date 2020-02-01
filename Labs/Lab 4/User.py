class User:
    def __init__(self, name, age, user_type, bank_num, bank_name, bank_bal):
        self._name = name
        self._age = age
        self._user_type = user_type
        self._bank_num = bank_num
        self._bank_name = bank_name
        self._bank_bal = bank_bal
        self._is_locked = False

