from itertools import count, cycle, takewhile

# --------------------------------------------count---------------------------------------------
try:
    numb = int(input("Введите целое число от 1 до 10: "))
    end = numb
    for elem in count(numb, 1):

        if end > 10:
            break
        print(elem, end=" ")
        end += 1
except ValueError:
    print("Error")

# ------------------------------------count with itertools.takewhile--------------------------------------
try:
    numb = int(input("\nВведите число: "))
    print([elem for elem in takewhile(lambda x: x <= 10, count(numb, 1))])
except ValueError:
    print("Error")
# --------------------------------------------cycle---------------------------------------------
print("\n\nCycle")
numb_list = [1, 5, 3, 4, 7, 9]
cycle_end = 0
for elem in cycle(numb_list):
    if cycle_end == len(numb_list) * 2:
        break
    print(elem, end=" ")
    cycle_end += 1
