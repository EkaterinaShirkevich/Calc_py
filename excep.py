import user_interface as console

def mistake():
    console.Interface("Mistake")
    

def action(i):
    ls =['+','-','*','/','5']
    if not i in ls:
        console.Interface("Mistake")
        return False
    return i

def digit():
    while(True):
        i = input("Введите выбраный пункт: ")
        if i.isdigit(): return int(i)
        console.Interface("Mistake")