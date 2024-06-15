#sueldo base mas comision del 10% por venta
#realizo 3 ventas
sueldo_base = float(input('Ingrese su sueldo base: '))
venta_1 = float(input('Ingrese el monto de su primera venta: '))
venta_2 = float(input('Ingrese el monto de su segunda venta: '))
venta_3 = float(input('Ingrese el monto de su tercera venta: '))
comision = (venta_1 + venta_2 + venta_3)*0.1
sueldo_total = sueldo_base + comision
print('Tu sueldo a recibir este mes es: ', sueldo_total)