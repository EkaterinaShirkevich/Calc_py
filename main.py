import user_interface as console
import excep as ex
import model_div as div
import model_sub as sub
import model_sum as sum
import model_mult as mult
import compl


console.Interface("Welcome")
while(True):
    console.Interface("Menu")
    i = ex.digit()
    match i:
        case 1: 
            print('Калькулятор для работы с рациональными числами')
            console.Interface("Action")
            i = input('Введите знак: ')
            if i == "+": print("Результат: ", sum.get_sum(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
            elif i == "-": print("Результат: ",sub.get_sub(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
            elif i == "*": 
                console.Interface("Mult")
                i =int(input('Введите выбранный пункт:'))
                print("Результат: ",mult.get_mult(int(input("Введите первое число: ")), int(input("Введите второе число: ")),i))
            elif i == "/": 
                console.Interface("Div")
                i =int(input('Введите выбранный пункт:'))
                print("Результат: ",div.get_div(int(input("Введите первое число: ")), int(input("Введите второе число: ")),i))
            elif i == "5": 
                console.Interface("End")
                if(int(input('Введите выбранный пункт: ')) == 2): 
                    print("Программа завершила работу")
                    break
            
            else: 
                ex.mistake()
            
            
        case 2:
            print('Калькулятор для работы с комплексными числами')
            console.Interface("Action")
            i = ex.action(input('Введите знак: '))
            if not i ==  False:
                if i == '5': 
                    print("Программа завершила работу")
                    break
                print(compl.cal_compl(i))
            
            console.Interface("End")
            if(int(input('Введите выбранный пункт: ')) == 5): 
                print("Программа завершила работу")
                break
        case 3:
            print('Запущен выход из программы')
            break
        case _: print("Нет данных")