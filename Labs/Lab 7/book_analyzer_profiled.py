"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":","(", "[", "]", ")"]

    def __init__(self):
        self.text = None
        self.unique_words = []

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        #strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words += line.split()
        self.text = words

        # remove common punctuation from words
        temp_text = []
        for word in self.text:
            temp_word = word
            for punctuation in self.COMMON_PUNCTUATION:
                temp_word = temp_word.replace(punctuation, '')
                temp_word.lower()
            temp_text.append(temp_word)
        self.text = temp_text

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        temp_text = self.text

        while temp_text:
            word = temp_text.pop()
            for a_word in temp_text:
                if word == a_word:
                    continue
            self.unique_words.append(word)



def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    book_analyzer.find_unique_words()
    print("-"*50)
    print(f"List of unique words (Count: {len(book_analyzer.unique_words)})")
    print("-"*50)
    for word in book_analyzer.unique_words:
        print(word)
    print("-"*50)


if __name__ == '__main__':
    main()