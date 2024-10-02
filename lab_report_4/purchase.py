book_name = ['A', 'B', 'C', 'D', 'E']
book_price = [200, 100, 300, 500, 250]

book_list=input().split()

price=0
for i in range(len(book_list)):
    if book_list[i] in book_name:
        index=book_name.index(book_list[i])
        price=price+book_price[index]
    else:
        print("book not found")
print(book_list)
print(price)