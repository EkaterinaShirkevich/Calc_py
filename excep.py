from cgitb import text
import user_interface as console
import logg 

def mistake():
    console.Interface("Mistake")
    

def action():
    ls =['+','-','*','/','5']
    while(True):
        i = input('Введите знак: ') 
        if i in ls: return i
        console.Interface("Mistake")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)


def digit():
    while(True):
        i = input("Введите выбраный пункт: ")
        if i.isdigit(): return int(i)
        console.Interface("Mistake")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)

def digit_number():
    while(True):
        i = input("Введите число: ")
        if i.isdigit(): return int(i)
        console.Interface("Mistake")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)





