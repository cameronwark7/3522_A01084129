from item import item

class DVD(item):
    def __init__(self, relDate, regCode, call_num, title, num_copies):
        self._releaseDate = relDate
        self._regionCode = regCode
        super().__init__(call_num, title, num_copies)

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._releaseDate}\n" \
                f"Region Code: {self._regionCode}"