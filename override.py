class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('vat mangsho polau korma')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)

    # override
    def eat(self):
        print('vegitables')

    def exercise(self):
        print('gym e poisa diya hudai gham jorai')

#  + sign oparator overload
    def __add__(self, other):
        return self.age + other.age
    
#  * sign oparator overload
    def __mul__(self, other):
        return self.weight * other.weight

#  len overload
    def __len__(self):
        return self.height
    
#  > operator overload
    def __gt__(self, other):
        return sakib.age > other.age

sakib = Cricketer('sakib', 38, 68, 91, 'BD')
mushi = Cricketer('mushi', 36, 65, 78, 'BD')
# sakib.eat()
# sakib.exercise()

# plus sign overload
print(45+ 63)
print('sakib' + 'rakib')
print([12, 98] + [5, 6 , 7, 2])

print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)