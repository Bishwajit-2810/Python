products = {
 "Rice": [45, 42, 41, 40],
 "Salt": [34, 35, 36, 36],
 "Fish": [200, 202, 201, 205],
 "Orange": [100, 99, 101, 102]
}

product=input().capitalize()
min_price=min(products[product])
place_of_min=products[product].index(min_price)+1
print(f"{product}-> market {place_of_min} = {min_price}")
