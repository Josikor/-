import csv
import os
import json

from openpyxl import Workbook
from prettytable import PrettyTable
import matplotlib.pyplot as plt    

def prettytable_from_csv(csv_file):
    with open(csv_file, encoding='utf-8') as csvf:
        data = []
        for line in csvf.readlines():
            if line.endswith('\n'):
                line = line[0:-1]

            data.append(line.split(sep=','))

    pt = PrettyTable()

    pt.field_names = data[0]
    pt.add_rows([
        *data[1:]
        ])
    return pt

def write_prettytable(pt):
    # saving table in .txt file
    with open('out.txt', 'wt', encoding='utf-8') as fout:
        fout.write(str(pt))

def write_json_from_csv(csv_file, json_file):
    json_array = []

    with open(csv_file, encoding='utf-8') as csvfin:

        csv_reader = csv.DictReader(csvfin)
        
        for row in csv_reader:
            json_array.append(row)
    
    with open(json_file, 'w', encoding='utf-8') as jsonfout:
        json_string = json.dumps(json_array, indent=4)
        jsonfout.write(json_string)

def write_excel_from_csv(csv_file, excel_file):
    wb = Workbook()

    ws = wb.active

    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.reader(csvf)
        for row in csv_reader:
            ws.append(row)

    wb.save(filename = excel_file)

def graph_on_screen(csv_file, x_field, y_field):
    x_list = []
    y_list = []
    with open(csv_file, encoding='utf-8') as csvfin:

        csv_reader = csv.DictReader(csvfin)
        
        for row in csv_reader:
            x_list.append(row[x_field])
            y_list.append(row[y_field])

    plt.plot(x_list, y_list)
    plt.xlabel(x_field)
    plt.ylabel(y_field)
    plt.show()


def loop():
    
    pt = prettytable_from_csv('in.txt')
    while True:
        print(pt, sep='\n\n')
        print(
        """
1 - Вивести таблицю у текстовий файл.
2 - Вивести таблицю у файл json.
3 - Вивести таблицю у файл Microsoft Excel.
4 - Вивести таблицю у графік на екран.
5 - Відібрати записи за критерієм.

        """)
        try:
            a = input("Ваш вибір: ")
            a = int(a)
        except ValueError:
            print("Неправильні вхідні дані. Спробуйте ще раз.")
            continue
        else:
            print('\n')
            if a == 1:
                write_prettytable(pt)
            elif a == 2:
                write_json_from_csv('in.txt', 'out.json')
            elif a == 3:
                write_excel_from_csv('in.txt', 'out.xlsx')
            elif a == 4:
                print("Дві назви критерій для створення графіку.")
                print("""
Доступні критерії:
* код ринку
* найменування ринку 
* дата
* ціна
* середня ціна
                    """)
                try:
                    x_field = input("Напишіть назву критерію (1): ").capitalize()
                    y_field = input("Напишіть назву критерію (2): ").capitalize()
                except AttributeError:
                    print("Неправильні вхідні дані. Спробуйте ще раз.")
                    continue
                else:
                    graph_on_screen('in.txt', x_field, y_field)
                    input("Нажміть Enter щоб продовжити. ")

            elif a == 5:
                # за критерієм
                print("""
Доступні критерії:
* код ринку
* найменування ринку 
* дата
* ціна
* середня ціна
                    """)
                try:
                    b = input("Напишіть назву критерію: ").capitalize()
                except AttributeError:
                    print("Неправильні вхідні дані. Спробуйте ще раз.")
                    continue
                else:
                    print(pt.get_string(fields=[b])) 
                    input("Нажміть Enter щоб продовжити. ")
        os.system('cls')

if __name__ == '__main__':
    loop()
