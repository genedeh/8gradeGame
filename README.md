# 8gradeGame import random
import string


class MathsGame:
    def __init__(self, profile_name, name, seconds=20):
        self.profile_name = profile_name
        self.name = name
        self.seconds = seconds

    def __str__(self):
        return f"name: {self.name}, profile name: {self.profile_name}"

    def Addition(self):
        easy_random1 = int(random.choice(string.digits))
        easy_random2 = int(random.choice(string.digits))
        easy_random3 = int(random.choice(string.digits))
        easy_random4 = int(random.choice(string.digits))
        print(f"{easy_random1} + {easy_random2} + {easy_random3} + {easy_random4} = ?")
        real_answer = easy_random1 + easy_random2 + easy_random3 + easy_random4
        answer = input("Enter answer: ")
        if answer.lower() == "stop":
            return "okay"
        if int(answer) == real_answer:
            print("CORRECT ANSWER")
        else:
            print("WRONG ANSWER")
            print(f"the answer is {real_answer} sorry! try again")

    def Subtraction(self):
        easy_random1 = int(random.choice(string.digits))
        easy_random2 = int(random.choice(string.digits))
        easy_random3 = int(random.choice(string.digits))
        easy_random4 = int(random.choice(string.digits))
        print(f"{easy_random1} - {easy_random2} - {easy_random3} - {easy_random4} = ?")
        real_answer = easy_random1 - easy_random2 - easy_random3 - easy_random4
        answer = input("Enter answer: ")
        if answer.lower() == "stop":
            return "okay"
        if int(answer) == real_answer:
            print("CORRECT ANSWER")
        else:
            print("WRONG ANSWER")
            print(f"the answer is {real_answer} sorry! try again")

    def Division(self):
        easy_random1 = int(random.choice(string.digits))
        easy_random2 = int(random.choice(string.digits))
        easy_random3 = int(random.choice(string.digits))
        easy_random4 = int(random.choice(string.digits))
        print(f"{easy_random1} / {easy_random2} / {easy_random3} / {easy_random4} = ?")
        real_answer = easy_random1 / easy_random2 / easy_random3 / easy_random4
        answer = input("Enter answer: ")
        if answer.lower() == "stop":
            return "okay"
        if float(answer) == real_answer:
            print("CORRECT ANSWER")
        else:
            print("WRONG ANSWER")
            print(f"the answer is {real_answer} sorry! try again")

    def Multiplication(self):
        easy_random1 = int(random.choice(string.digits))
        easy_random2 = int(random.choice(string.digits))
        easy_random3 = int(random.choice(string.digits))
        easy_random4 = int(random.choice(string.digits))
        print(f"{easy_random1} * {easy_random2} * {easy_random3} * {easy_random4} = ?")
        real_answer = easy_random1 * easy_random2 * easy_random3 * easy_random4
        answer = input("Enter answer: ")
        if answer.lower() == "stop":
            return "okay"
        if int(answer) == real_answer:
            print("CORRECT ANSWER")
        else:
            print("WRONG ANSWER")
            print(f"the answer is {real_answer} sorry! try again")

    def Addition_Subtraction(self):
        easy_random1 = int(random.choice(string.digits))
        easy_random2 = int(random.choice(string.digits))
        easy_random3 = int(random.choice(string.digits))
        easy_random4 = int(random.choice(string.digits))
        print(f"{easy_random1} / {easy_random2} / {easy_random3} / {easy_random4} = ?")
        real_answer = easy_random1 + easy_random2 - easy_random3 + easy_random4
        answer = input("Enter answer: ")
        if answer.lower() == "stop":
            return "okay"
        if int(answer) == real_answer:
            print("CORRECT ANSWER")
        else:
            print("WRONG ANSWER")
            print(f"the answer is {real_answer} sorry! try again")


maths_game = MathsGame("ayo", "Hazzan")
print(maths_game.Division())
