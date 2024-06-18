#cantidad de aves por región
#cantidad de aves enero 2023
#cantidad de especie “Tagua” en Cartagena
#cantidad de especie “Piquero” el 12 de febrero 2023
#grafique cantidad de las siguientes especies: Gaviota garuma, Piquero, Gaviota de Franklin, Pelicano y Guanay (gráfico de barras)


import matplotlib.pyplot as plt

def lectura_datos(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(",")
        datos.append(lista)
    return datos


def regiones_erroneas(region):
    if region == 'AricaParinacota':
        return 'Arica y Parinacota'
    if region == 'Tocopilla' or region == 'Taltal':
        return 'Antofagasta'
    if region == 'OÂ´Higgins':
        return 'O´Higgins'
    if region == 'nuble':
        return 'Ñuble'
    if region == 'Tarapaca' or region == 'Iquique':
        return 'Tarapacá'
    if region == 'Valparaiso':
        return 'Valparaíso'
    else:
        return region


def funcion_a(datos):
    aves_region = {}
    for lista in datos:
        region = regiones_erroneas(lista[2])
        aves_muertas = int(lista[7])        
        if region in aves_region:
            aves_region[region] += aves_muertas
        else:
            aves_region[region] = aves_muertas    
    return aves_region
     

def funcion_b(datos):
    aves_enero2023 = 0
    for lista in datos:
        fecha = lista[0].split("-")
        mes = fecha[1]
        anio = fecha[2]
        aves_muertas = int(lista[7])
        if mes == '01'and anio == '2023':
            aves_enero2023 += aves_muertas
        
    return aves_enero2023


def funcion_c(datos):
    taguas_muerte = 0
    for lista in datos:
        region = regiones_erroneas(lista[2])
        especie = lista[6].split(" - ")[0]
        comuna = lista[3]
        aves_muertas = int(lista[7])
        if especie.lower() == 'tagua' and comuna.lower() == 'cartagena':
            taguas_muerte += aves_muertas
    return taguas_muerte


def funcion_d(datos):
    piquero_muerte = 0
    for lista in datos:
        fecha = lista[0].split('-')
        dia = fecha[0]
        mes = fecha[1]
        year = fecha[2]
        aves_muertas = int(lista[7])
        especie = lista[6].split(" - ")[0]
        if dia == '12' and mes == '02' and year == '2023' and especie.lower() == 'piquero':
            piquero_muerte += aves_muertas
    return piquero_muerte

def aves_especie_grafica(datos):
    g_garuma = 0
    piquero = 0
    g_franklin = 0
    pelicano = 0
    guanay = 0
    for lista in datos:    
        aves_muertas = int(lista[7])
        especie = lista[6].split(" - ")[0]
        if especie.lower() == 'gaviota garuma':
            g_garuma += aves_muertas
        if especie.lower() == 'piquero':
            piquero += aves_muertas
        if especie.lower() == 'gaviota de franklin':
            g_franklin += aves_muertas
        if especie.lower() == 'pelicano':
            pelicano += aves_muertas
        if especie.lower() == 'guanay':
            guanay += aves_muertas          
        else:
            especie = aves_muertas    
    return g_garuma, piquero, g_franklin, pelicano, guanay

def funcion_e(valores):
    especies = ['Gaviota Garuma', 'Piquero', 'Gaviota de Franklin', 'Pelicano', 'Guanay']
    plt.figure(figsize=(10, 6))
    plt.bar(especies, valores, color= 'blue')
    plt.xlabel('Especies')
    plt.ylabel('Cantidad de Aves Muertas')
    plt.title('Cantidad de Aves Muertas por Especie')
    plt.xticks(rotation=360)
    plt.tight_layout()
    plt.show()


def salida(muertes_region, enero_2023, taguas_muerte, piquero_muerte):
     sal = open('resultado.txt', 'w', encoding='utf-8')
     sal.write('Autor(es): M. Ignacia Acevedo Apaz - L. Felipe Bahamondes Garrido \n\n')
     sal.write('Cantidad de aves muertas por región:\n\n')
     for region in muertes_region:
        cantidad = muertes_region[region]
        sal.write('\t'f'{region}: {cantidad}\n\n')
     sal.write(f'Casos aves muertas mes enero del año 2023: {enero_2023}\n\n')
     sal.write(f'En la comuna de Cartagena se detectaron {taguas_muerte} Taguas muertas.\n\n')
     sal.write(f'Las muertes detectadas para el 12 de febrero del 2023 de la especie Piquero (Sula variegata) son: {piquero_muerte}\n')
     sal.close()


if __name__ == '__main__':
    datos = lectura_datos('aves.txt')
    muertes_region = funcion_a(datos)
    enero_2023 = funcion_b(datos)
    taguas_muerte = funcion_c(datos)
    piquero_muerte = funcion_d(datos)
    valores = aves_especie_grafica(datos)
    funcion_e(valores)
    salida(muertes_region, enero_2023, taguas_muerte, piquero_muerte)