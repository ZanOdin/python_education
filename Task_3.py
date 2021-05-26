class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


number_list = []
while True:
    try:
        number = str(input("Enter a new number to add to the list: "))
        if number.isdigit():
            number = int(number)
        elif number.lower() == "q" or number.lower() == "stop":
            print(number_list)
            break
        else:
            raise MyException("Enter the number or 'q'/'stop'...")
    except (ValueError, MyException) as err:
        print(err)
    else:
        number_list.append(number)
        print(number_list)
