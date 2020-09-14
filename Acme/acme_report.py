from acme import Product
from random import randint, sample, uniform

adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''
    Function to randomly generate a given number of products
    '''
    products = []
    for _ in range(num_products):
        name = f'{sample(adjective, 1)[0]} {sample(noun,1)[0]}'
        price = randint(5,100)
        weight = randint(5,100)
        flammability = uniform(0.0, 2.5)
        prod = Product(name=name, price=price, weight=weight, flammability=flammability)
        prod_list = []
        for title in [prod.identifier, prod.name, prod.price, prod.weight, prod.flammability]:
            prod_list.append(title)
        products.append(prod_list)
    return products

def inventory_report(products):
    names = []
    prices = []
    weights = []
    flams = []
    for name in products: 
        names.append(name[1])
        prices.append(name[2])
        weights.append(name[3])
        flams.append(name[4])
    
    set_names = set(names)
    unique_names = len(set_names)
    
    average_price = sum(prices) / len(prices)
    average_weight = sum(weights) / len(weights)
    average_flammability = sum(flams) / len(flams)
    print('ACME Inventory Report')
    print(f'There are {unique_names} unique products at Acme!')
    print(f'The average price of our products is {average_price}')
    print(f'The average weight of our products is {average_weight}')
    print(f'The average flammability score for our products is {average_flammability}')


if __name__ == '__main__':
    
    #Simple test for product generator
    '''
    #print(generate_products())
    '''
    
    #Simple test for inventory report
    '''
    #inventory_report(generate_products(50))
    '''