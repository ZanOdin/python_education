def update_txt(txt_file):
    change_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    new_text = open("task_4_new.txt", "w", encoding='utf-8')
    new_text.close()
    with open(txt_file, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for key in change_dict.keys():
                if words[0] == key:
                    with open("task_4_new.txt", "a", encoding="utf-8") as new_text:
                        new_text.write(f"{change_dict[key]} - {words[2]}\n")
        with open("task_4_new.txt", "r", encoding="utf-8") as new_text:
            print(new_text.read())


update_txt("text_4.txt")
