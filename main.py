#модуль для работы с регулярными выражениями и математикой
import re
import math

#функция, решающая квадратные уравнения
def quadratic_equation(expr):
    try:
        #разделяем уравнение на части по знакам: +, -, =
        expr = expr.replace('+', ' +')
        expr = expr.replace('-', ' -')
        expr = re.split('\s|\=', expr)

        #записываем значения частей уравнения в переменные
        a = expr[0]
        b = expr[1]
        c = expr[2]
        r = expr[3]

        #форматируем части уравнений
        a = float(eval(a.replace('x^2', '')))
        b = float(eval(b.replace('x', '')))
        c = float(eval(c))
        r = float(eval(r))

        #находим дискриминант
        D = b**2-(4*a*c)

        #проверяем сколько корней и возвращаем их значения
        if(D>0):
            result_1 = (-b+math.sqrt(D))/2*a
            result_2 = (-b-math.sqrt(D))/2*a

            return 'D = ' + str(D) + '\n' + 'result_1 = ' + str(result_1) + '\n' + 'result_2 = ' + str(result_2)
        elif(D==0):
            return 'D = ' + str(D) + '\n' + 'result = ' + str(-b/2*a)
        else:
            return 'D = ' + str(D) + '\n' + 'no results'
    except:
        return 'You wrote something wrong'

while(True):
    expr = input('Input quadratic equation (ax^2+bx+c=0): \n- ')
    print(quadratic_equation(expr))
    print('\n')
