class User:
    def __init__(self, name, age, bank_num, bank_name, bank_bal):
        self._name = name
        self._age = age
        self._bank_num = bank_num
        self._bank_name = bank_name
        self.bank_bal = bank_bal
        self._initial_e = 0
        self._initial_c = 0
        self._initial_f = 0
        self._initial_m = 0

    def get_bank_num(self):
        return self._bank_num

    def get_bank_name(self):
        return self._bank_name

    def get_bank_bal(self):
        return self.bank_bal
