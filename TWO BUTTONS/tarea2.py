
# Funcion que encuentra los minimos clicks para llegar de n --> m
def min_clicks(n, m):
    
    # Contador de clicks (o c como dice en el reporte)
    c = 0

    # Bucle que se mantiene si y solo si n es distinto de m 
    while n != m :
        # Caso 1: en este caso solo podemos restar hasta llegar al valor de m
        if n >= m:
            n -= 1

        # Caso 2: por otro lado en este duplicar el numero es los mas factible pero sin superar el valor de m
        elif n * 2 <= m :
            n *= 2

        # Caso 3: finalmente si ninguno de los dos casos anteriores son viables restaremos 1 para actualizar n
        else:
            n-= 1
            
    # Actualizamos los clicks y se retornan 
        c += 1
    return c
            
    

# Ejemplos del enunciado + casos que presentan mayor dificultad para el algoritmo
print(min_clicks(4, 6)) # Salida esperada 2
print(min_clicks(10, 1)) # Salida esperada 9
print(min_clicks(10000,1)) # Salida esperada 9999


