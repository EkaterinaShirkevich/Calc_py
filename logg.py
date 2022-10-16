from datetime import datetime as dt

def actions_logger(data):
    '''
    Функция, логирует ошибки программы
    :param data: наименование ошибки
    '''
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{data}, {time} \n')


# def actions_calculator(a,b,data):
#     time = dt.now().strftime('%D %H:%M')
#     with open('log.csv', 'a', encoding='utf-8') as file:
#         file.write(f'"Пользователь ввел"{data}, {time} \n')