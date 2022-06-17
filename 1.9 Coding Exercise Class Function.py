class clubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("name", self.name)
        print("birthday", self.birthday)
        print("age", self.age)
        print('favorite_food', self.favorite_food)
        print("goal", self.goal)

class clubofficers(clubMembers):
    #__init__ method of admin sublcass overides __init__methods of user subs class

    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        clubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display2(self):
        print("name", self.name)
        print("birthday", self.birthday)
        print("age", self.age)
        print("goa", self.goal)
        print("position", self.position)

m_1 = clubMembers("tom", "january 16", "14", "ice cream", "to be happy")
o_4 = clubofficers("vera", "june 22", "16", "beef strogaooff", "to bbe the worlds greatest chef", "treasurer")

m_1.display1()
o_4.display2()