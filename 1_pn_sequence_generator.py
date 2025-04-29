"""
Características fundamentales de los códigos PN (Pseudo-Noise):
- Son secuencias binarias que aparentan ser aleatorias pero son generadas de manera determinística.
- Tienen un período largo antes de repetirse (máximo para m-secuencias: 2^n - 1).
- Presentan buena propiedad de balance: casi igual cantidad de unos y ceros.
- Poseen excelentes propiedades de autocorrelación: pico alto en el origen y valores bajos en otros desplazamientos.
- Distribución de corridas similar a la de una secuencia aleatoria.
- Su espectro es relativamente plano, similar al ruido blanco.
Estas características las hacen útiles en comunicaciones digitales, especialmente en sistemas de espectro ensanchado y CDMA.
"""
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del LFSR
n = 6  # Número de etapas
periodo = 2**n - 1  # Longitud máxima de la secuencia
# Polinomio: z^6 + z + 1 => realimentación entre la etapa 6 y la etapa 1

# Estado inicial (no puede ser todo ceros)
estado = [1, 0, 0, 0, 0, 0]  # Puede cambiarse si se desea otro estado inicial

secuencia = []

for _ in range(periodo):
    salida = estado[-1]
    secuencia.append(salida)
    # XOR entre la etapa 6 (estado[-1]) y la etapa 1 (estado[0])
    nuevo_bit = estado[-1] ^ estado[0]
    # Desplazar el registro
    estado = [nuevo_bit] + estado[:-1]

# Guardar la secuencia en un archivo .txt
with open('1_pn_sequence.txt', 'w') as f:
    f.write(' '.join(map(str, secuencia)))

# Graficar la secuencia generada
plt.figure(figsize=(12,2))
plt.stem(range(1, periodo+1), secuencia, basefmt=" ", use_line_collection=True)
plt.title('Secuencia PN generada (63 bits)')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.yticks([0,1])
plt.tight_layout()
plt.savefig('1_pn_sequence.png')
plt.close()

print(f"Secuencia PN generada y guardada en 1_pn_sequence.txt ({periodo} bits)")
print("Gráfico de la secuencia guardado en 1_pn_sequence.png") 