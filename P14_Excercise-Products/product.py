import csv

from tabulate import tabulate


class Product:
    def __init__(self, article_number, name, description, price, stock):
        self.__article_number = article_number
        self.__name = name
        self.__description = description
        self.__price = price
        self.__stock = stock
    
    @property
    def article_number(self):
        return self.__article_number
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def price(self):
        return self.__price
    
    @property
    def stock(self):
        return self.__stock
    
    def total_value(self):
        return self.__price * self.__stock


def read_products():
    products = []
    with open('product.csv', encoding='utf-8-sig', newline='') as csvfile:
        for rij in csv.DictReader(csvfile):
            product = Product(rij['article_number'], rij['name'], rij['description'], float(rij['price']), int(rij['stock']))
            products.append(product)
        return products
    
def show_products(products):
    product_table = []
    for product in products:
        product_table.append([product.article_number, product.name, product.price, product.total_value()])
    
    print(tabulate(product_table, headers=['Article number', 'Name', 'Price', 'Total value']))

products = read_products()
show_products(products)