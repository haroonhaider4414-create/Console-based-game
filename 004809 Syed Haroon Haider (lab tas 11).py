#Syed Haroon Haider


name_of_item = input("enter the name of item:")
price_of_item = int(input("enter the price of item:"))
weight_of_item = int(input("enter the weight of item:"))
total_cost = price_of_item * weight_of_item
print("Enter the name of item:" +name_of_item)
print("enter the price of item:" +str(price_of_item))
print("enter the weight of item:" +str(weight_of_item))

print(f"{name_of_item}: {price_of_item} KG per unit, weight: {weight_of_item} KG total cost:{total_cost}")


name_of_item = input("enter the name of item:")
weight_of_item = int(input("enter the weight of item:"))
price_of_item = int(input("enter the price of item:"))
Total_cost = weight_of_item * price_of_item
print("enter the name of item:" +name_of_item)
print("enter the price of item:" +str(price_of_item))
print("enter the weight of item:" +str(weight_of_item))
print(f"{name_of_item}: {price_of_item} litre per unit, weight:{weight_of_item} , total cost:{Total_cost}")



name_of_item = input("enter the name of item:")
weight_of_item = int(input("enter the weight of item:"))
price_of_item = int(input("enter the price of item:"))
total_cost2 = weight_of_item * price_of_item
print("enter the name of item" +name_of_item)
print("enter the weight of item" +str(weight_of_item))
print("enter the price of item" +str(price_of_item))
print(f"{name_of_item}: {price_of_item}, per unit, weight: {weight_of_item}, total cost:{total_cost2}")

print(f"Grand Total:{total_cost + Total_cost + total_cost2}")