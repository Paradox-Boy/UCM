def angulo_interior(lados):
    if lados < 3:
        return "No es un polígono válido, intente nuevamente."
    angulo = (lados - 2) * 180 / lados
    return angulo

def main():
    lados = input('Por favor indique la cantidad de lados del polígono: ')
    if lados.isdigit():
        lados = int(lados)
        angulo = angulo_interior(lados)
        if isinstance(angulo, str):
            print(angulo)  
        else:
            print(f"El ángulo interior de un polígono con {lados} lados es: {angulo:.0f} grados.")
            print(f"La suma total de los ángulos interiores es: {angulo * lados:.2f} grados.")
    else:
        print("Por favor, debe indicar un número entero válido, intente nuevamente.")

if __name__ == "__main__":
    main()
