import numpy as np
import matplotlib.pyplot as plt

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
    # Si n > m solo restamos
    if n > m:
        c += n - m
    return c
            
    

# Ejemplos del enunciado + casos que presentan mayor dificultad para el algoritmo (pueden agregar y testaer)
print(min_clicks(10, 10)) # Salida esperada 0
print(min_clicks(10000,1)) # Salida esperada 9999
print(min_clicks(2,16)) # Salida esperada 3

# ---- Valores simulados ----
tamanos = [0, 500, 1000, 1500, 2000, 2500, 3000]
tiempos_medios = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
tiempos_std = [0, 0.02, 0.03, 0.04, 0.05, 0.07, 0.1]  # errores simulados

# ---- Ajuste cuadrático ----
coef = np.polyfit(tamanos, tiempos_medios, 2)  # polinomio grado 2
ajuste = np.polyval(coef, tamanos)

# ---- Gráfico ----
plt.errorbar(
    tamanos, tiempos_medios, yerr=tiempos_std,
    fmt='-o', color='blue', ecolor='black', capsize=5, label='Tiempo medio'
)
plt.plot(tamanos, ajuste, 'r--', label='Ajuste cuadrático')

plt.title("Tiempo de ejecución del algoritmo min_clicks")
plt.xlabel("Tamaño del problema (m)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.show()
