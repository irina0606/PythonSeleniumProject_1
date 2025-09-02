list1 = ["India", "USA", "Australia", "UK"]
list2 = ["Pune", "Washington", "Sidney", "London"]

result = zip(list1,list2)
print(list(result))

for x, y in zip(list1, list2):
    print(x, "-", y)

# zip function is good practice to use in calculations
# ex: count the profit

total_price = [45, 67, 65, 87]
sale_price = [55, 77, 89, 76]

for x, y in zip(total_price, sale_price):
    print(y-x)