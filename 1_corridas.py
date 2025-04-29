"""
Propiedad de Corridas:
En una secuencia PN de longitud máxima (m-secuencia), la propiedad de corridas establece que:
- Aproximadamente la mitad de las corridas son de longitud 1, un cuarto de longitud 2, un octavo de longitud 3, etc.
- El número de corridas de unos y ceros es casi igual.
Una corrida es una secuencia continua de unos o ceros. Esta propiedad contribuye a la apariencia aleatoria de la secuencia.
"""

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

# Función para contar corridas
def contar_corridas(seq):
    if not seq:
        return []
    corridas = []
    actual = seq[0]
    longitud = 1
    for bit in seq[1:]:
        if bit == actual:
            longitud += 1
        else:
            corridas.append((actual, longitud))
            actual = bit
            longitud = 1
    corridas.append((actual, longitud))
    return corridas

corridas = contar_corridas(secuencia)

# Contar corridas por valor y longitud
from collections import Counter, defaultdict
corridas_por_longitud = defaultdict(lambda: {'unos':0, 'ceros':0})
for valor, longitud in corridas:
    if valor == 1:
        corridas_por_longitud[longitud]['unos'] += 1
    else:
        corridas_por_longitud[longitud]['ceros'] += 1

# Guardar el análisis en un archivo .txt
with open('1_corridas.txt', 'w') as f:
    f.write('Propiedad de Corridas en la secuencia PN:\n')
    f.write('Longitud | Corridas de unos | Corridas de ceros\n')
    for longitud in sorted(corridas_por_longitud):
        f.write(f'{longitud:8} | {corridas_por_longitud[longitud]["unos"]:16} | {corridas_por_longitud[longitud]["ceros"]:17}\n')
    f.write('\nSegún la teoría, la cantidad de corridas de longitud n debería ser aproximadamente la mitad de las de longitud n-1.\n')
    f.write('El número de corridas de unos y ceros debe ser casi igual.\n')

# Graficar histograma de corridas por longitud
import matplotlib.pyplot as plt
import numpy as np

longitudes = sorted(corridas_por_longitud)
unos = [corridas_por_longitud[l]['unos'] for l in longitudes]
ceros = [corridas_por_longitud[l]['ceros'] for l in longitudes]

x = np.arange(len(longitudes))
plt.figure(figsize=(8,5))
plt.bar(x - 0.2, ceros, width=0.4, label='Ceros', color='blue')
plt.bar(x + 0.2, unos, width=0.4, label='Unos', color='orange')
plt.xticks(x, longitudes)
plt.xlabel('Longitud de corrida')
plt.ylabel('Cantidad de corridas')
plt.title('Histograma de corridas por longitud en la secuencia PN')
plt.legend()
plt.tight_layout()
plt.savefig('1_corridas_histograma.png')
plt.close()

print('Propiedad de corridas analizada. Resultado guardado en 1_corridas.txt.') 