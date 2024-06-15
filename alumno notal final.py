#alumno desea saber nota final
#la nota se compone por los siguientes porcentajes
#55% del promedio de las 3 notas parciales
#30% de la nota del examen final
#15 de la nota de trabajo final

parcial_1 = float(input('Por favor indique su primera nota parcial: '))
parcial_2 = float(input('Por favor indique su segunda nota parcial: '))
parcial_3 = float(input('Por favor indique su tercera nota parcial: '))
promedio_parcial = (parcial_1 + parcial_2 + parcial_3) / 3 
porcentaje_parciales = promedio_parcial * 0.55
examen_final = float(input('Por favor indique su nota del examen final: '))
porcentaje_examen = examen_final * 0.3
trabajo_final = float(input('Por favor indique su nota del trabajo final: '))
porcentaje_trabajo = trabajo_final * 0.15
print('Su nota final es:', porcentaje_parciales + porcentaje_examen + porcentaje_trabajo)
