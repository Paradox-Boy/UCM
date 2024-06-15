cm = float(input('Escriba la cantidad de cm: '))
shaku_med= 30.3
ken_med = 6
shaku_cant = cm / shaku_med
ken_cant = shaku_cant / ken_med
print(cm, 'cm es igual a: ', round(shaku_cant, 3), 'shaku(s), y: ', round(ken_cant, 3), 'ken(s)')