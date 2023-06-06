#Given the below class:
class Cats:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1=Cats("Kitty",5)
cat2=Cats("Tom",3)
cat3=Cats("Verity",7)
cat4=Cats("Falak",4)


# 2 Create a function that finds the oldest cat
def oldest(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest Cat is",oldest(cat1.age,cat2.age,cat3.age,cat4.age),"years old")   