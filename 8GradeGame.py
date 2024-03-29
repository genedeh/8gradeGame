import random
import string


class MathsGame:
    """ This is  a maths game that lets the user to check his or her skills in
       addition, subtraction, division, multiplication and addition plus subtraction
       :parameter: profile_name: str, name: str, seconds: int
       SAMPLE:

       Correct answer SAMPLE:

       >>> maths_game = MathsGame("testing", "test")
       >>> print(maths_game.addition_subtraction())
       >>> '7 + 1 - 1 + 3 = ?'
       >>>  'Enter answer: 10'
       >>>  'CORRECT ANSWER'

       Wrong answer SAMPLE':

       >>> maths_game = MathsGame("testing", "test")
       >>> print(maths_game.addition_subtraction())
       >>> '1 + 2 - 9 + 6 = ?'
       >>>  'Enter answer: 3'
       >>>   'WRONG ANSWER'

       # :exception: ValueError

        Excepiton answer SAMPLE:

        >>> maths_game = MathsGame("testing", "test")
        >>> print(maths_game.addition_subtraction())
        >>> '3 + 4 - 2 + 4 = ?'
        >>> 'Enter answer: nine'
        >>> '"nine" is not a valid number, only the string stop is allowed'

    """

    def __init__(self, profile_name: str, name: str, seconds: int = 20):
        self.profile_name = profile_name
        self.name = name
        self.seconds = seconds

    def __str__(self):
        return f"name: {self.name}, profile name: {self.profile_name}"

    def addition(self):
        """This method gives the user addition based questions"""
        global answer
        while True:
            try:
                easy_random1 = int(random.choice(string.digits))
                easy_random2 = int(random.choice(string.digits))
                easy_random3 = int(random.choice(string.digits))
                easy_random4 = int(random.choice(string.digits))
                print(f"{easy_random1} + {easy_random2} + {easy_random3} + {easy_random4} = ?")
                real_answer = easy_random1 + easy_random2 + easy_random3 + easy_random4
                answer = input("Enter answer: ")
                if answer.lower() == "stop":
                    print("okay")
                    break
                if int(answer) == real_answer:
                    print("CORRECT ANSWER")
                else:
                    print("WRONG ANSWER")
                    print(f"the answer is {real_answer} sorry! try again")
            except ValueError:
                return f'"{answer}" is not a valid number, only the string stop is allowed'

    def subtraction(self):
        """This method gives the user subtraction based questions"""
        global answer
        while True:
            try:
                easy_random1 = int(random.choice(string.digits))
                easy_random2 = int(random.choice(string.digits))
                easy_random3 = int(random.choice(string.digits))
                easy_random4 = int(random.choice(string.digits))
                print(f"{easy_random1} - {easy_random2} - {easy_random3} - {easy_random4} = ?")
                real_answer = easy_random1 - easy_random2 - easy_random3 - easy_random4
                answer = input("Enter answer: ")
                if answer.lower() == "stop":
                    print("okay")
                    break
                if int(answer) == real_answer:
                    print("CORRECT ANSWER")
                else:
                    print("WRONG ANSWER")
                    print(f"the answer is {real_answer} sorry! try again")
            except ValueError:
                return f'"{answer}" is not a valid number, only the string stop is allowed'

    def division(self):
        """This method gives the user division based questions"""
        global answer
        while True:
            try:
                easy_random1 = int(random.choice(string.digits))
                easy_random2 = int(random.choice(string.digits))
                easy_random3 = int(random.choice(string.digits))
                easy_random4 = int(random.choice(string.digits))
                print(f"{easy_random1} / {easy_random2} / {easy_random3} / {easy_random4} = ?")
                real_answer = easy_random1 / easy_random2 / easy_random3 / easy_random4
                answer = input("Enter answer: ")
                if answer.lower() == "stop":
                    print("okay")
                    break
                if float(answer) == real_answer:
                    print("CORRECT ANSWER")
                else:
                    print("WRONG ANSWER")
                    print(f"the answer is {real_answer} sorry! try again")
            except ValueError:
                return f'"{answer}" is not a valid number, only the string stop is allowed'

    def multiplication(self):
        """This method gives the user multiplication based questions"""
        global answer
        while True:
            try:
                easy_random1 = int(random.choice(string.digits))
                easy_random2 = int(random.choice(string.digits))
                easy_random3 = int(random.choice(string.digits))
                easy_random4 = int(random.choice(string.digits))
                print(f"{easy_random1} * {easy_random2} * {easy_random3} * {easy_random4} = ?")
                real_answer = easy_random1 * easy_random2 * easy_random3 * easy_random4
                answer = input("Enter answer: ")
                if answer.lower() == "stop":
                    print("okay")
                if int(answer) == real_answer:
                    print("CORRECT ANSWER")
                else:
                    print("WRONG ANSWER")
                    print(f"the answer is {real_answer} sorry! try again")
            except ValueError:
                return f'"{answer}" is not a valid number, only the string stop is allowed'

    def addition_subtraction(self):
        """This method gives the user addition with subtraction based questions"""
        global answer
        while True:
            try:
                easy_random1 = int(random.choice(string.digits))
                easy_random2 = int(random.choice(string.digits))
                easy_random3 = int(random.choice(string.digits))
                easy_random4 = int(random.choice(string.digits))
                print(f"{easy_random1} + {easy_random2} - {easy_random3} + {easy_random4} = ?")
                real_answer = easy_random1 + easy_random2 - easy_random3 + easy_random4
                answer = input("Enter answer: ")
                if answer.lower() == "stop":
                    print("okay")
                    break
                if int(answer) == real_answer:
                    print("CORRECT ANSWER")
                else:
                    print("WRONG ANSWER")
                    print(f"the answer is {real_answer} sorry! try again")
            except ValueError:
                return f'"{answer}" is not a valid number, only the string stop is allowed'


maths_game = MathsGame("testing", "test")
print(maths_game.addition_subtraction())
