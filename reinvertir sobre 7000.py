#un hombre desea saber cuanto será su interes de ganancia
#si es sobre 7000 desea reinvertir
#finalmente desea saber el saldo total en su cuenta
cap_inv = int(input('Por favor indique el monto a invertir: '))
interes = float(input('por favor indique el porcentaje de interes: '))
monto_interes = interes * cap_inv / 100
if monto_interes  > 7000:
    print('Su saldo final es: ', monto_interes + cap_inv)
else:
    print('El interés generado no es mayor que $7000')


