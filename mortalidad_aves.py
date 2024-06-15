#cantidad de aves por región
#cantidad de aves enero 2023
#cantidad de especie “Tagua” en Cartagena
#cantidad de especie “Piquero” el 12 de febrero 2023
#grafique cantidad de las siguientes especies: Gaviota garuma, Piquero, Gaviota de Franklin, Pelicano y Guanay (gráfico de barras)


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
    aves_enero2023 = {}
    for lista in datos:
        fecha = lista[0].split("-")
        mes = fecha[1]
        anio = fecha[2]
        aves_muertas = int(lista[7])
        if mes == '01'and anio == '2023':
            return 'Enero 2023'
        if mes and anio in fecha:
            aves_enero2023[mes and anio] += aves_muertas        
    return aves_enero2023

def funcion_c(datos):
    pass

def funcion_d(datos):
    pass

def funcion_e(especies):
    pass

def salida(region, enero_2023, tagua, piquero):
    pass

if __name__ == '__main__':
    datos = lectura_datos('aves.txt')
    muertes_region = funcion_a(datos)
    enero = funcion_b(datos)
    tagua = funcion_c
    piquero = funcion_d
    grafique = funcion_e
print(muertes_region)
print(enero)