#se debe determinar el nivel de hemoglobina según datos ingresados
#debe preguntar por edad
#debe preguntar por genero si es mayor de 15 años
#el nivel puede ser positivo, negativo (sobre) o negativo (bajo)

import os
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

mes_an = int(input('meses oprima 0 años oprima 1: '))
niv_hemo = float(input('indique el nivel de hemo: '))
if mes_an == 0:
    meses = int(input('indique los meses de edad: '))
    if meses <= 1:
        if niv_hemo < 13:
            print('nivel bajo rango')
        elif niv_hemo > 26:
            print('nivel sobre rango')
        else:
            print('nivel normal')
    elif meses > 1 and meses <= 6:
        if niv_hemo < 10:
            print('nivel bajo rango')
        elif niv_hemo > 18:
            print('nivel sobre rango')
        else:
            print('nivel normal')
    elif meses > 6 and meses <= 12:
        if niv_hemo < 11:
            print('nivel bajo rango')
        elif niv_hemo > 15:
            print('nivel sobre rango')
        else:
            print('nivel normal')
elif mes_an == 1:
    anios = int(input('indique los años de edad: '))
    if anios > 1 and anios <= 5:
        if niv_hemo < 11.5:
            print('nivel bajo rango')
        elif niv_hemo > 15:
            print('nivel sobre rango')
        else:
            print('nivel normal')
    elif anios > 5 and anios <= 10:
        if niv_hemo < 12.6:
            print('nivel bajo rango')
        elif niv_hemo > 15.5:
            print('nivel sobre rango')
        else:
            print('nivel normal')
    elif anios > 10 and anios <= 15:
        if niv_hemo < 13:
            print('nivel bajo rango')
        elif niv_hemo > 15.5:
            print('nivel sobre rango')
        else:
            print('nivel normal')
    elif anios > 15:
        m_f = int(input('si es hombre oprima 0, si es mujer oprima 1: '))
        if m_f == 0:
            if niv_hemo < 14:
                print('nivel bajo rango')
            elif niv_hemo > 18:
                print('nivel sobre rango')
            else:
                print('nivel normal')
        elif m_f == 1:
            if niv_hemo < 12:
                print('nivel bajo rango')
            elif niv_hemo > 16:
                print('nivel sobre rango')
            else:
                print('nivel normal')         
print('gracias')