class Person:
    pick_walk = ""
    pick_talk = ""
    pick_fight = ""
    __walk = {'run': 200, 'sprint': 500, 'marathon': 50000}
    pick_walk = input("Chose either run or sprint or marathon:  ")
    if pick_walk.lower() == "run":
        print(__walk['run'])
    elif pick_walk.lower() == "sprint":
        print(__walk['sprint'])
    elif pick_walk.lower() == "marathon":
        print(__walk['marathon'])
    else:
        raise ValueError("INVALID INPUT")
    __talk = {'quiet': -0, 'speak': 10, 'shout': 1000}
    pick_talk = input("Chose either quiet or speak or shout:  ")
    if pick_talk.lower() == "quiet":
        print(__talk['quiet'])
    elif pick_talk.lower() == "speak":
        print(__talk['speak'])
    elif pick_talk.lower() == "shout":
        print(__talk['shout'])
    else:
        raise ValueError("INVALID INPUT")
    __fight = {'blows': 100, 'kicks': 200, 'upper_court': 1000000}
    pick_fight = input("Chose either blows or kicks or upper_court:  ")
    if pick_fight.lower() == "blows":
        print(__fight['blows'])
    elif pick_fight.lower() == "kicks":
        print(__fight['kicks'])
    elif pick_fight.lower() == "upper_court":
        print(__fight['upper_court'])
    else:
        raise ValueError("INVALID INPUT")

    def __init__(self, __walk, __talk, __fight):
        self.pick_walk = __walk
        self.pick_talk = __talk
        self.pick_fight = __fight


person = Person
print(person.pick_walk)
