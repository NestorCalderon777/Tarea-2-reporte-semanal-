
# Funcion que encuentra los minimos clicks para llegar de n --> m
def min_clicks(n, m):
    # Contador de clicks (o c como dice en el reporte)
    c = 0
    # Bucle que se mantiene si y solo si n es distinto de m 
    while n != m :
        # Caso 1 
        if n >= m:
            n -= 1

        elif n * 2 <= m :
            n *= 2

        else:
            n-= 1

        c += 1
    return c
            
    

# Ejemplos del enunciado
print(min_clicks(4, 6))   
print(min_clicks(10, 1))  
print(min_clicks(10000,1))
