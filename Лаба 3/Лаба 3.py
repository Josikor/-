import csv
import sys
grp=int(input("Виберіть групу студентів: 1-Комп.науки, 2-Менеджмент"))
if grp==1:
    oper=int(input("Виберіть дію:1 - Прочитати файл, 2 - Перезаписати файл, 3 - Добавити в файл, 4 - Найти дані в файлі, 5 - Відсортувати за середнім балом "))
    if oper==1:
        file=open('students.txt', 'r', encoding='utf-8')
        print(file.read())
        file.close()
    elif oper==2:
        newstud=(input("Введіть ПІБ студентів та їх бал"))
        file=open('students.txt','w',encoding ='utf-8')
        file.write(newstud)
        file.close()
    elif oper == 3:
        grade=input("Введіть бал ЗНО ")
        addstud=input("ПІБ кого додати ")
        file=open('students.txt','a', encoding ='utf-8')
        file.write ('\n' +grade+ " " +addstud)
        file.close()
    elif oper == 4:
        file=open ('students.txt', 'r', encoding ='utf-8')
        search=input('ПІБ кого знайти')
        read=file.read()
        file.close()
        if search in read :
            print("Знайдено")
        else :
            print("Не знайдено")
    elif oper == 5 :
        file = open('students.txt', encoding ='utf-8')
        for i in sorted(file) :
            print(i, end= ' ')
else : 
    oper=int(input("Выберите дію:1 - Прочитати файл, 2 - Перезаписати файл, 3 - Добавити в файл, 4 - Найти дані в файлі, 5 - Відсортувати за середнім балом "))
    if  oper == 1 :
        file = open('students2.txt', encoding ='utf-8')
        print(file.read())
        file.close()
    elif oper == 2 :
        newstud=(input("Введіть ПІБ студентів та їх бал"))
        file = open('students2.txt','w', encoding ='utf-8')
        file.write(newstud)
        file.close()
    elif oper == 3 :
        grade = input("Введіть бал ЗНО ")
        addstud = input("ПІБ кого додати ")
        file = open('students2.txt','a', encoding ='utf-8')
        file.write ('\n' +grade+ " " +addstud)
        file.close()
    elif oper == 4 :
        file = open ('students2.txt', 'r', encoding = 'utf-8')
        search = input('ПІБ кого знайти')
        read= file.read()
        file.close()
        if search in read :
            print("Знайдено")
        else :
            print("Не знайдено")
    elif oper == 5 :
        file = open('students2.txt', encoding ='utf-8')
        for i in sorted(file) :
            print(i, end= ' ')
            