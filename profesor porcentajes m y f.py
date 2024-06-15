#profesor conoce la cantidad total de alumnos hombres y mujeres
#profesor quiere saber el porcentaje de cada uno
cantidad_hombres = int(input('Por favor indique la cantidad de estudiantes hombres: '))
cantidad_mujeres = int(input('Por favor indique la cantidad de estudiantes mujeres: '))
total_estudiantes = cantidad_hombres + cantidad_mujeres
porcentaje_hombres = cantidad_hombres * 100 / total_estudiantes
porcentaje_mujeres = cantidad_mujeres * 100 / total_estudiantes
print('El porcentaje de estudiantes hombres es: ', porcentaje_hombres)
print('El porcentaje de estudiantes mujeres es: ', porcentaje_mujeres)
