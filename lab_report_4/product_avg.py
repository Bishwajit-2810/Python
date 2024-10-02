product_prices = {
    'Apples': [1.5, 1.7, 1.6, 1.8],
    'Bananas': [0.5, 0.6, 0.55, 0.65],
    'Oranges': [2.0, 2.1, 2.05, 2.2]
    }
new_dict={}
for key in product_prices.keys():
    new_dict[key] = sum(product_prices[key])/len(product_prices[key])

print(new_dict)