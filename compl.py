import excep as ex
import logg

def cal_compl(i):
	in_real_1 = ex.digit_number('Введите действительное число 1 части: ')
	in_imag_1 = ex.digit_number('Введите мнимое число 1 части: ')
	a = complex(in_real_1, in_imag_1)
	
	in_real_2 = ex.digit_number('Введите действительное число 2 части: ' )
	in_imag_2 = ex.digit_number('Введите мнимое число 2 части: ' )
	b = complex(in_real_2, in_imag_2)
	
	if i == "+":
		logg.result_logger(a + b)
		return a + b
	elif i == "-":
		logg.result_logger(a - b)
		return a - b
	elif i == "*":
		logg.result_logger(a * b)
		return a * b
	elif i == "/":
		logg.result_logger(a / b)
		return a / b
	elif i == "^":
		logg.result_logger(a ** b)
		return a ** b
