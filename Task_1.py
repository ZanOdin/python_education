from sys import argv

name, hour_out, rph, prize = argv
print("Заработная плата равна (выработка в часах * ставка в час) + премия: ", end="")
print(int(hour_out) * int(rph) + int(prize))
