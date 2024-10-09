function suma_angulos = suma_angulos(n)
    if n < 3
        error('No es un polígono válido, intente nuevamente.');
    end
    suma_angulos = (n - 2) * 180;
end

n_lados = input('Por favor indique la cantidad de lados del polígono: ');
try
    resultado = suma_angulos(n_lados);
    fprintf('La suma total de los ángulos interiores es: %.1f grados\n', resultado);
catch error
    fprintf('Error: %s\n', error.message);
end
