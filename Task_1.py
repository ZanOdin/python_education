# Creating new text file
text = open("task_1.txt", "w", encoding="utf-8")
text.close()
with open("task_1.txt", "a", encoding="utf-8") as text:
    string = input("Напишите что-нибудь: ")
    while string != "":
        text.writelines(f"{string}\n")
        string = input("Напишите что-нибудь еще: ")
