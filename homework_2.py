# Переводчик секунд в часы:минуты:секунды

seconds = int(input("Введите количество секунд: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60

print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))
