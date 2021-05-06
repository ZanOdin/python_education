# --------------------------------------------------------1------------------------------------------------------
def int_func():
    """Выводит слова с заглавной буквы через пробел (лат)"""
    words = input("Введите слова через пробел: ")
    words = words.split(" ")
    new_words = []
    for word in words:
        new_word = ""
        for i in word:
            if 97 <= ord(i) <= 122:
                new_word += i
            else:
                new_word = ""
                break
        if new_word != "":
            new_words.append(new_word.capitalize())
    return ' '.join(new_words)


print(int_func())


# --------------------------------------------------------2------------------------------------------------------

def int_func_2():
    """Выводит слова с заглавной буквы через пробел (лат) - метод решения без создания списка"""
    words = input("Введите слова через пробел: ")
    new_word = ""
    new_words = ""
    err = 0
    for i in range(len(words)):
        if words[i] != " " and 97 <= ord(words[i]) <= 122 and err != 1:
            if words[i - 1] == " " or i == 0:
                new_word += words[i].capitalize()
            else:
                new_word += words[i]
                if i + 1 == len(words):
                    new_words += new_word
        elif words[i] == " ":
            err = 0
            if new_word != "":
                new_words += new_word + words[i]
            new_word = ""
        else:
            new_word = ""
            err = 1

    return new_words


print(int_func_2())
