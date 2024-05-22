import csv

class Product:
    def __init__(self,article_number, name, description, price, stock):
        self.article_number = article_number
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

products =[]

with open('product.csv', encoding='utf-8-sig', newline='') as csvfile:
    for row in csv.DictReader(csvfile):
        product = Product(row['article_number'], row['name'], row['description'], float(row['price']), int(row['stock']))
        products.append(product)

for product in products:
    print(product.article_number, product.name, product.price, "value:", product.price * product.stock)