import turtle


class Animal:
    # function for creation of eye
    def face(self):
        # define pen size
        turtle.pensize(10)

        # define pen color
        turtle.pencolor("brown")

        # for outer bigger circle
        turtle.fillcolor("yellow")
        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()
        turtle.circle(200)

        # for eyes
        turtle.penup()
        turtle.goto(-100, 50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10.5)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(100, 50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10.5)
        turtle.end_fill()

        # for nose
        turtle.penup()
        turtle.goto(0, 50)
        turtle.pendown()
        turtle.circle(-70, steps=2)

        # for smile
        turtle.penup()
        turtle.goto(-100, -70)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(100, 360)
        turtle.mainloop()


class Mammal(Animal):
    mammal_name = ""
    mammal_age = ""
    mammal_gender = ""
    DictionaryMammal = ""
    mammal_attribute = ""

    def MammalFile(self):
        mammal_file_name = input("Enter folder name:  ")
        mammal_name = input("Enter the animal name: ")
        mammal_age = input("Enter the animals age: ")
        mammal_gender = input("Enter the gender of the animal:  ")
        while mammal_gender.lower() == "male" or mammal_gender.lower() == "female":
            if 1 < 10:
                print(f"the animal is called a {mammal_name}")
                print(f"the animals is {mammal_age} years old")
                print(f"the animal is a {mammal_gender}")
            mammal_attribute = input(f"Chose {mammal_file_name} attributes: ")
            if mammal_attribute.lower() == "name":
                print(f"name : {mammal_name}")
            if mammal_attribute.lower() == "age":
                print(f"name : {mammal_age}")
            if mammal_attribute.lower() == "gender":
                print(f"name : {mammal_gender}")
            break


class NonMammal(Animal):
    non_mammal_name = ""
    non_mammal_age = ""
    non_mammal_gender = ""
    DictionaryNonMammal = ""
    mammal_non_attribute = ""

    def NonMammalFile(self):
        non_mammal_file_name = input("Enter file name:  ")
        non_mammal_name = input("Enter the animal name: ")
        non_mammal_age = input("Enter the animals age: ")
        non_mammal_gender = input("Enter the gender of the animal:  ")
        while non_mammal_gender.lower() == "male" or non_mammal_gender.lower() == "female":
            if 1 < 10:
                print(f"the animal is called a {non_mammal_name}")
                print(f"the animals is {non_mammal_age} years old")
                print(f"the animal is a {non_mammal_gender}")
            mammal_attribute = input(f"Chose {non_mammal_file_name} attributes: ")
            if mammal_attribute.lower() == "name":
                print(f"name : {non_mammal_name}")
            if mammal_attribute.lower() == "age":
                print(f"age : {non_mammal_age}")
            if mammal_attribute.lower() == "gender":
                print(f"gender : {non_mammal_gender}")
            break


animal = Animal()
mammal = Mammal()
non_mammal = NonMammal()
print(id(Mammal))
