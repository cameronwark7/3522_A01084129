from item import item

class Journal(item):
    def __init__(self, name, issue_no, pub, call_num, title, num_copies):
        self._name = name
        self._issue_no = issue_no
        self._publisher = pub
        super().__init__(call_num, title, num_copies)

    def __str__(self):
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Publisher: {self._publisher}\n" \
               f"Name: {self._name}\n" \
                f"Issue No.: {self._issue_no}"
