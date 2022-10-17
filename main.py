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
            i = ex.action()
            if i == "+": print("Результат: ", sum.get_sum(ex.digit_number(), ex.digit_number()))
            elif i == "-": print("Результат: ",sub.get_sub(ex.digit_number(), ex.digit_number()))
            elif i == "*": 
                console.Interface("Mult")
                i =int(input('Введите выбранный пункт:'))
                print("Результат: ",mult.get_mult(ex.digit_number(), ex.digit_number(),i))
            elif i == "/": 
                console.Interface("Div")
                i =int(input('Введите выбранный пункт:'))
                print("Результат: ",div.get_div(ex.digit_number(), ex.zero_number(),i))
            elif i == "5": 
                print('---------------------------------------------')
                print("Программа завершила работу")
                print('---------------------------------------------')
                break
            
            else: 
                ex.mistake()
            
            console.Interface("End")
            if(ex.digit() == 2): 
                print('---------------------------------------------')
                print("Программа завершила работу")
                print('---------------------------------------------')
                break
            
            
        case 2:
            print('Калькулятор для работы с комплексными числами')
            console.Interface("Action")
            i = ex.action()
            if i == '5': 
                print('---------------------------------------------')
                print("Программа завершила работу")
                print('---------------------------------------------')
                break
            print(compl.cal_compl(i))
            
            console.Interface("End")
            if(ex.digit() == 2): 
                print('---------------------------------------------')
                print("Программа завершила работу")
                print('---------------------------------------------')
                break
        case 3:
            print('---------------------------------------------')
            print("Программа завершила работу")
            print('---------------------------------------------')
            break
        case _: print("Нет данных")