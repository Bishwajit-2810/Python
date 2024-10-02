book_names = ['A', 'B', 'C', 'D']
book_prices = [250, 150, 300, 450]
new_dict={}

for i in range(len(book_prices)):
    if book_prices[i]>=500:
        discount_price = book_prices[i] - (book_prices[i] * 0.20)
    elif 300 <= book_prices[i] and book_prices[i] < 500:
        discount_price = book_prices[i] - (book_prices[i] * 0.15)
    elif 100 <= book_prices[i] and book_prices[i] < 300:
        discount_price = book_prices[i] - (book_prices[i] * 0.10)
    else:
        discount_price = book_prices[i] - (book_prices[i] * 0.05)
    new_dict[book_names[i]]=discount_price

i=0
for keys in new_dict.keys():
    print(f"book {new_dict[keys]}: Original price: {book_prices[i]}, Discounted price: {new_dict[keys]}")
    i+=1