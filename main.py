# ДЗ Вебинар №8

old_file = 'phonebook_old.txt'
new_file = 'phonebook_new.txt'
record_number = int(input('Введите номер строки: '))

def copy_record(old_file, new_file, record_number):
    with open(old_file, 'r') as file:
        lines = file.readlines()
    with open(new_file, 'w') as file:
        file.write(lines[record_number - 1])
    for i in range(len(lines)):
        if i != record_number - 1:
            file.write(lines[i])

copy_record(old_file, new_file, record_number)
