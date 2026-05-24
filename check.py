from solution import FileReader

print(FileReader("not_exist_file.txt").read())  # должно быть: пустая строка

with open("some_file.txt", "w") as f:
    f.write("some text")

print(FileReader("some_file.txt").read())  # должно быть: some text