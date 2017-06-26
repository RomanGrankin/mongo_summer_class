import pymongo, random
from loremipsum import get_sentences

#{"_id": 234234, "sku": 1513243, "price": 144, "description": "Some text",
#"category": 'PC', "brand": "apple", "reviews": ['author': 'Pete']}

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.store
products = db.products

categories = ['tablet', 'PC', 'cellphone']
brand = ['hp', 'apple', 'samsung', 'toshiba']
names = ['Pete', 'John', 'Roman', 'Sam', 'Kate', 'Salomon']

for sku in range(100000):
    price = (random.randrange(0, sku+1))*2393
    descr = get_sentences(random.randrange(3))
    categ = categories[random.randrange(3)]
    br = brand[random.randrange(4)]
    nm = names[random.randrange(6)]
    entry = {'sku': sku, 'price': price, 'description': descr, 'category': categ, 'brand': br, 'reviews':{'author': nm}}
    try:
        products.insert_one(entry)
    except Exception as e:
        print "unexp. err:", type(e), e
