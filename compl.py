
def cal_compl(i):
    a =complex(int(input("1 real part: ")),int(input("1 imaginary number: ")))
    b =complex(int(input("2 real part: ")),int(input("2 imaginary number: ")))
    
    match i:
        case "+": return a+b
        case "-": return  a-b
        case "*": return  a*b
        case "/": return  a/b
        case "^": return  a**b