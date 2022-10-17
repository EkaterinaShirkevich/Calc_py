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
        i = input("Введите выбранный пункт: ")
        if i.isdigit(): return float(i)
        console.Interface("Mistake")
        print("Вам надо ввести число")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)

def zero_number():
    while(True):
        i = digit_number()
        if i !=0 : return i
        console.Interface("Mistake")
        print("На ноль делить нельзя")
        text = "Пользователь ввел: 0. Это некорректный ввод"
        logg.actions_logger(text)


def digit_number():
    while(True):
        i = input("Введите число: ")
        if i.isdigit(): return float(i)
        console.Interface("Mistake")
        print("Вам надо ввести число")
        text = "Пользователь ввел: " + i + ". Это некорректный ввод"
        logg.actions_logger(text)




