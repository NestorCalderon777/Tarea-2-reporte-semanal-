
# Funcion que encuentra los minimos clicks para llegar de n --> m
def min_clicks(n, m):
    c = 0
    while n < m:
        if n * 2 <= m:
            n *= 2
        else:
            # Si n*2 > m, restamos de golpe hasta m
            c += m - n
            n = m
        c += 1  # Contamos el paso actual
    # Si n > m (caso muy raro), solo restamos
    if n > m:
        c += n - m
    return c
            
    

# Ejemplos del enunciado + casos que presentan mayor dificultad para el algoritmo
print(min_clicks(4, 6)) # Salida esperada 2
print(min_clicks(10, 10)) # Salida esperada 0
print(min_clicks(10000,1)) # Salida esperada 9999
print(min_clicks(2,16)) # Salida esperada 3






