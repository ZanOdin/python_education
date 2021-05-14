with open("task_2.txt", "r", encoding="utf-8") as file:
    line_count = 0
    word_count = 0
    words = []
    for line in file:
        line_count += 1
        words = line.split()
        word_count = len(words)
        print(f"В {line_count} строке количество слов: {word_count}")
