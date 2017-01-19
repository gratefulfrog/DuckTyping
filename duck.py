#!/usr/local/bin/python3
"""
Python Duck Typing example:
- The idea is that if it can Quack, it's a Duck, otherwise it's not a duck.

Running the program from the command line
$ chmod a+x duck.py
$ ./duck.py 
or
$ ./duck.py 23

running the program from with python3
$ python3
>>> import duck
>>> duck.main()
Not a Duck... 	a Cat
Quack!
A Duck!
Quack!
A Duck!
Not a Duck... 	a Dog
Not a Duck... 	a Cat
Not a Duck... 	a Dog
Not a Duck... 	a Cat
Not a Duck... 	a Dog
Not a Duck... 	a Dog
Quack!
A Duck!
>>> duck.main(41)
...


What it does:
- create a list of animals of various kinds,
- ask each one to quack,
- if it quacks, it's a duck,
- if not, it's not a duck!
"""

class Named:
    """ 
    class's string representation is its name,
    all the animal classes inherit from this class so that their name is properly displayed!
    """
    def __repr__(self):
        return self.__class__.__name__
    
class Duck(Named):
    """ a Duck quacks
    """
    def quack(self):
        print("Quack!")

class Dog(Named):
    """ a Dog barks
    """
    def bark(self):
        print("Woof!")

class Cat(Named):
    """ a Cat meows
    """
    def meow(self):
        print("Meow!")

class Cow(Named):
    """ a Cow moos
    """
    def moo(self):
        print("Mooo!")

class Donkey(Named):
    """ a Donkey honks
    """
    def honk(self):
        print("HeeHoo!")
        
def main(nbAnimals = 10):
    """
    * we first get a list of all the classes defined in the current module
    * then seed the random number generator,
    * then make an empty list which will contain animal instances
    * then iterate over the nbAnimals, randomly appending an animal instance to the 
      animalInstanceList,
      Note how we use macro evaluation to create a string which when evaluated will
        produce an instace of an animal class, eg. the string 'Duck' is concatenated
        with the string '()' to produce 'Duck()' which is then passed to eval to 
        create an instance of the Duck class!
    * then we iterate over all the animal instances, asking each to quack,
      if it can quack without an error, it's a duck!
      if an exception was raised, then it's not a duck! In that case, just to prove
        to the user that it was not a duck, we extract the class name from the type 
        information and print to stdout.  This last part is only for demonstrative
        purpose, and is not needed in real life applications.
    """
    import random,inspect,sys
    classStringLis = [c[0]  for c in inspect.getmembers(sys.modules[__name__], inspect.isclass) if c[0] !='Named']

    random.seed()
    animalInstanceList = []
    for i in range(nbAnimals):
        animalInstanceList += [eval(random.choice(classStringLis)+'()')]
    
    for animal in animalInstanceList:
        try:
            animal.quack()
            print('A ',animal,'!')
            #print('A Duck!')
        except:
            print('Not a Duck... \ta', animal) 
    
if __name__ == "__main__":
    # execute only if run as a script
    # first check for a command line argument, i.e. the number of animals
    # if provided, use it,
    # otherwise accept the default...
    import sys
    if len(sys.argv)>1:
        main(int(sys.argv[1]))
    else:
        main()

