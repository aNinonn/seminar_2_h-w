# Напишите программу, которая получает целое число и возвращает его 
# шестнадцатеричное строковое представление. Функцию hex используйте 
# для проверки своего результата.

user_number = int(input("Введите число :"))
res = ""
print(hex(user_number))


while user_number:
   res = f"{user_number % 16}" + res 
   user_number //= 16
   
print(res)
