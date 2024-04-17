#Exircise 1
# value1 = input("Введите первое значение: ")
# value2 = input("Введите второе значение: ")
# value3 = input("Введите третье значение: ")

# print(value1, value2, value3)  
# print(value1, ":", value2, ":", value3)  
# print("- " + value1, "\n- " + value2, "\n- " + value3) 

#Exircise 2
# value1 = int(input("Введите первое числа "))
# value2 = int(input("Введите второе числа "))

# print(value1**value2)

#Exercise 3
# purchase_price = float(input("Введите цену закупки телефона: "))

# sale_price = purchase_price * 1.3
# discount_5 = sale_price * 0.95
# discount_10 = sale_price * 0.90
# discount_15 = sale_price * 0.85

# print(f"Цена продажи: {sale_price}")
# print(f"Цена продажи со скидкой 5%: {discount_5}")
# print(f"Цена продажи со скидкой 10%: {discount_10}")
# print(f"Цена продажи со скидкой 15%: {discount_15}")

#Exircise 4
number = int(input("Введите число: "))

number_of_thousands = number // 1000
number_of_hundreds = (number % 1000) // 100
number_of_tens = (number % 100) // 10
number_of_units = number % 10

print(f"тысяч - {number_of_thousands}")
print(f"сотен - {number_of_hundreds}")
print(f"десятков - {number_of_tens}")
print(f"единиц - {number_of_units}")
