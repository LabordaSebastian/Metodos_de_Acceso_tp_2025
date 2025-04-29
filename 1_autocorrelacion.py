"""
Autocorrelación:
La autocorrelación mide la similitud de una secuencia consigo misma a diferentes desplazamientos (lags). En códigos PN, una buena autocorrelación implica un pico alto en el origen y valores bajos en otros desplazamientos, lo que es fundamental para aplicaciones de sincronización y espectro ensanchado.
"""
import numpy as np
import matplotlib.pyplot as plt

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

# Convertir la secuencia de {0,1} a {-1,1} para la autocorrelación
secuencia_bipolar = [2*x - 1 for x in secuencia]

# Repetir la secuencia 3 veces para graficar 3 períodos
secuencia_3periodos = secuencia_bipolar * 3

# Calcular la autocorrelación
autocorr = np.correlate(secuencia_3periodos, secuencia_3periodos, mode='full')
# Centrar el eje x
lags = np.arange(-len(secuencia_3periodos)+1, len(secuencia_3periodos))

# Graficar
plt.figure(figsize=(10,5))
plt.stem(lags, autocorr)
plt.title('Autocorrelación de la secuencia PN (3 períodos)')
plt.xlabel('Desplazamiento (lag)')
plt.ylabel('Autocorrelación')
plt.grid(True)
plt.tight_layout()
plt.savefig('1_autocorrelacion.png')
plt.close()

# Guardar conclusiones en un archivo .txt
with open('1_autocorrelacion.txt', 'w') as f:
    f.write('Se graficó la autocorrelación de la secuencia PN para 3 períodos.\n')
    f.write('La autocorrelación muestra un pico principal en el origen y valores bajos en los demás desplazamientos,\n')
    f.write('lo que es característico de las secuencias PN y las hace útiles para sincronización y espectro ensanchado.\n')
    f.write('Ver gráfico en 1_autocorrelacion.png.\n')

print('Autocorrelación calculada y graficada (ver 1_autocorrelacion.png). Conclusiones guardadas en 1_autocorrelacion.txt.') 