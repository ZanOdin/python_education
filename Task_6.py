def int_func(text):
    """Выводит слово с заглавной буквы (лат)"""
    for i in text:
        if 97 <= ord(i) <= 122:
            continue
        else:
            return None
    return text.capitalize()


print(int_func("yeap"))
