# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать 
# сумму и произведение* дробей. Для проверки своего кода 
# используйте модуль fractions.
import fractions


num_1, denum_1 = input("Введите дробь типа a/b :").split("/")
num_2, denum_2 = input("Введите вторую дробь типа a/b :").split("/")



def frac_sum (n1: int, d1: int, n2: int, d2: int) -> str:
    if d1 != d2:
        if ((n1*d2) + (n2*d1)) / (d1*d2) == 1:
            return "1"
        else:
            return f"{((n1*d2) + (n2*d1))}/{(d1*d2)}"
    else:
        if (n1+n2)/d1 == 1:
            return "1"
        else:
            return f"{(n1+n2)}/{d1}"

def frac_comp (n1: int, d1: int, n2: int, d2: int) -> str:
    if (n1*n2) / (d1*d2)== 1:
            return "1"
    else:
        return f"{(n1*n2)} / {(d1*d2)}"

print(f"Сумма равна: {frac_sum(int(num_1),int(denum_1),int(num_2),int(denum_2))}")
print(f"Произведение равно: {frac_comp(int(num_1),int(denum_1),int(num_2),int(denum_2))}")

frac1 = fractions.Fraction(int(num_1),int(denum_1))
frac2 = fractions.Fraction(int(num_2),int(denum_2))

print(f"Проверка: {frac1+frac2}, {frac1*frac2}")