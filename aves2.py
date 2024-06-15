def lectura_datos(nombre):
    datos = []
    with open(nombre, 'r') as ent:
        for linea in ent:
            linea = linea.rstrip('\n')
            lista = linea.split(",")
            datos.append(lista)
    return datos

def region(datos):
    aves_region = {}
    for lista in datos:
        region = lista[2]
        aves_muertas = int(lista[-1])
        
        if region in aves_region:
            aves_region[region] += aves_muertas
        else:
            aves_region[region] = aves_muertas
    
    return aves_region

# Ejemplo de uso
datos = lectura_datos('aves.txt')  # Reemplaza 'archivo.csv' por el nombre de tu archivo CSV
resultado = region(datos)
print(resultado)