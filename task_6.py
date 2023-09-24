# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте 
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

def replenishment(real_status:int) -> int:
    rep_summ = int(input("Введите сумму пополнения кратную 50 у.е.: "))
    real_status += rep_summ
    return real_status 


def withdrawal(real_status: int) -> int:
    wit_summ = int(input("Введите сумму снятия кратную 50 у.е.: "))
    while wit_summ > real_status:
        wit_summ = int(input("Сумма снятия превышает остаток по счету, попробуйте еще раз: "))
    if wit_summ*0.015 < 30:
        real_status -= (wit_summ + 30)
    elif wit_summ*0.015 > 600:
        real_status -= (wit_summ + 600)
    else:
        real_status -= (wit_summ + wit_summ*0.015)
    
    return real_status

def bankomat():
    balance_status = 0
    i = 0
    while True:
        balance_status += (balance_status*0.03) if i%3 == 0 else 0
        balance_status -= (balance_status*0.1) if balance_status > 5_000_000 else 0
            
        print(f"-- На счете лежит {balance_status} у.е. --")
        print("Если вы хотите пополнить счет, наберите 1")
        print("Если вы хотите снять деньги со счета, наберите 2")
        print("Если вы хотите выйти, наберите 3")
        user_menu_choise = int(input("Введите ваш выбор: "))
        if user_menu_choise == 1:
            balance_status = replenishment(balance_status)
            i += 1
        if user_menu_choise == 2:
            balance_status = withdrawal(balance_status)
            i += 1
        if user_menu_choise == 3:
            print(f"Вы решили выйти, остаток на счете {balance_status}")
            return
        

bankomat()