# ===============================================1================================================
def num_dec(var_1, var_2):
    try:
        print(var_1 / var_2)
    except ZeroDivisionError:
        print("Нельзя делить на ноль")


num_dec(int(input("Делимое: ")), int(input("Делитель: ")))

# =================================================2==============================================

my_func = lambda var_1, var_2: var_1 / var_2

try:
    print(num_dec(5, 0))
except ZeroDivisionError:
    print("Нельзя делить на ноль")
