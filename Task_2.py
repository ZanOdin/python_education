class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

divident = input("Enter the devidend: ")
divider = input("Enter the divider: ")
try:
    divident = int(divident)
    divider = int(divider)
    if divider == 0:
        raise MyException("Can't be divided by zero...")
    result = round(float(divident / divider), 2)
except(ValueError, MyException) as err:
    print(err)
else:
    print(result)
finally:
    print("It was a pleasure doing business with you.")
