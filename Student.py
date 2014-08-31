__author__ = 'prateek'


class Student:
    def __init__(self, s_name="", s_gpa=None, s_age=0):
        self.name = s_name
        self.gpa = s_gpa
        self.age = s_age

    def __attrs(self):
        return self.name, self.gpa, self.age

    def __str__(self):
        return "(" + self.name + ',' + str(self.gpa) + ',' + str(self.age) + ")"

    def __lt__(self, other):
        return other < self

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        else:
            return self.__attrs() == other.__attrs()
            # self.name == other.name and self.gpa == other.gpa and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.gpa, self.age))


if __name__ == "__main__":
    print "Starting..."
    a1 = Student("aa"    , 3     , 10    )
    a2 = Student("aa"    , 3     , 11    )
    a3 = Student("A"     , 3     , 10    )
    a4 = Student("aa"    , 4     , 10    )
    a5 = Student("aa"    , 4     , 9     )
    a6 = Student("A"     , 3.2   , 20.2  )
    a7 = Student("john"  , 4.0   , 20    )
    a8 = Student("joh"   , 4.0   , 25    )
    a9 = Student("aa"    , 3.6   , 25    )
    b1 = Student("aa"    , 3.63  , 25    )
    b2 = Student("Carlos", 3.33  , 21.34 )
    b3 = Student("Carlos", 3.33  , 21.34 )

    ''' Personal testing code '''
    testDict = {hash(a1):a1, hash(a2):a2, hash(a3):a3,
                hash(a4):a1, hash(a5):a1, hash(a6):a6,
                hash(a7):a7, hash(a8):a8, hash(a9):a9,
                hash(b1):b1, hash(b2):b2, hash(b3):b3 }
    for key in sorted(testDict, key=lambda cha: testDict[cha].name):
        print "Sorting by name: key:" , key , "\t Val: " , testDict.get(key)
    print("")
    for key in sorted(testDict, key=lambda cha: testDict[cha].gpa):
        print "Sorting by gpa: key:" , key , "\t Val: " , testDict.get(key)
    print("")
    for key in sorted(testDict, key=lambda cha: testDict[cha].age):
        print "Sorting by age: key:" , key , "\t Val: " , testDict.get(key)



    '''Sorting by GPA and then breaking ties using name & then age within the lambda function'''
    arraySort = [("aa"    , 3     , 10    ), ("aa"    , 3     , 11    ), ("ab"     ,3     , 11    ),
                 ("aa"    , 4     , 10    ), ("aa"    , 4     , 9     ), ("A"     , 3.2   , 20.2  ),
                 ("john"  , 4.0   , 20    ), ("joh"   , 4.0   , 25    ), ("aa"    , 3.6   , 25    ),
                 ("aa"    , 3.63  , 25    ), ("Carlos", 3.33  , 21.34 ), ("Carlos", 3.33  , 21.34 )]

    for key in sorted(arraySort, key=lambda cha: (cha[1], cha[2], cha[0])):
        print "Sorting by gpa & then by age & then by name:" , key