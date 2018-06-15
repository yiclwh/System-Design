"""
Factory is a design pattern in common usage. Please implement a ToyFactory 
which can generate proper toy based on the given type.

Example
    ToyFactory tf = ToyFactory();
    Toy toy = tf.getToy('Dog');
    toy.talk(); 
    >> Wow

    toy = tf.getToy('Cat');
    toy.talk();
    >> Meow
"""

"""
Your object will be instantiated and called as such:
ty = ToyFactory()
toy = ty.getToy(type)
toy.talk()
"""
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    # Write your code here
    def talk(self):
        print("Wow")

class Cat(Toy):
    # Write your code here
    def talk(self):
        print("Meow")

class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        # Write your code here
        if type == 'Dog':
            return Dog()
        elif type == 'Cat':
            return Cat()
        return None