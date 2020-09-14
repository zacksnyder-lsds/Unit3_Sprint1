from random import randint

class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name 
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        steal = self.price/self.weight
        if steal < 0.5:
            return 'Not so stealable'
        elif steal >= 0.5 and steal < 1.0:
            return 'Kinda stealable'
        else: 
            return 'Very stealable!'

    def explode(self):
        boom = self.flammability * self.weight
        if boom < 10:
            return '...fizzle'
        if boom >= 10 and boom < 50:
            return '...Boom!'
        else:
            return '...BABOOM'
    

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, flammability)
        self.weight=weight
    
    def explode(self):
        return '...its a glove'

    def punch(self):
        if self.weight < 5:
            return 'That Tickles!'
        elif self.weight >=5 and self.weight < 15:
            return 'Hey That Hurt!'
        else:
            return 'Ouch!!!'


if __name__ == '__main__':

    #Simple Test for the Product class
    '''
    prod = Product('A cool toy')
    print(prod.name)
    print(prod.price)
    print(prod.weight)
    print(prod.flammability)
    print(prod.identifier)
    print(prod.stealability())
    print(prod.explode())
    '''

    #Simple test for the Boxing Gloves class
    ''' 
    prod2 = BoxingGlove('Boxing Gloves')
    print(prod2.name)
    print(prod2.price)
    print(prod2.flammability)
    print(prod2.identifier)
    print(prod2.weight)
    print(prod2.punch())
    print(prod2.explode())
    '''