class Player:

    def __init__(self, fname, lname, college, draft_year, hometown, position):
        self.fname = fname
        self.lname = lname
        self.college = college
        self.draft_year = draft_year
        self.hometown = hometown
        self.position = position

    def __str__(self):
        return f"({self.fname} {self.lname} from {self.hometown})"


p1 = Player('Steph', 'Curry', 'Davidson', 2010, 'Akron, Ohio', 'Point Guard')
print(p1)




