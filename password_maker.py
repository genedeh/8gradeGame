import random
import string


class PasswordMaker:
    def __init__(self, key_words, code_name="Code Name", key=6):
        self.__key_words = key_words
        self.__code_name = code_name
        self.__key = key

    def DigitPassword(self):
        return "".join(random.choices(string.digits, k=self.__key))

    def WordPassword(self):
        return "".join(random.choices(self.__key_words + string.ascii_letters, k=self.__key))

    def CodePassword(self):
        return "".join(random.choices(self.__code_name + string.digits + string.ascii_letters, k=self.__key))

    def RandomPassword(self):
        return "".join(
            random.choices(self.__key_words + self.__code_name + string.digits + string.ascii_letters, k=self.__key))


passcode_bot = PasswordMaker("Genesis", code_name="bro force one", key=8)
print(passcode_bot.CodePassword())
