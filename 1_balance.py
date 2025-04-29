"""
Propiedad de Balance:
En una secuencia PN de longitud máxima (m-secuencia), la propiedad de balance establece que, en un período completo, el número de unos es exactamente uno más que el número de ceros.
Esto significa que la secuencia es casi perfectamente equilibrada entre unos y ceros, lo que contribuye a su apariencia aleatoria y utilidad en comunicaciones.
"""

import matplotlib.pyplot as plt

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

num_unos = sum(secuencia)
num_ceros = len(secuencia) - num_unos

cumple_balance = (num_unos == num_ceros + 1)

# Guardar el análisis en un archivo .txt
with open('1_balance.txt', 'w') as f:
    f.write('Propiedad de Balance en la secuencia PN:\n')
    f.write(f'Cantidad de unos: {num_unos}\n')
    f.write(f'Cantidad de ceros: {num_ceros}\n')
    if cumple_balance:
        f.write('La secuencia CUMPLE la propiedad de balance: hay un uno más que ceros.\n')
    else:
        f.write('La secuencia NO cumple la propiedad de balance.\n')

# Graficar histograma de unos y ceros
plt.figure(figsize=(5,4))
plt.bar(['Ceros', 'Unos'], [num_ceros, num_unos], color=['blue', 'orange'])
plt.title('Histograma de unos y ceros en la secuencia PN')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.savefig('1_balance_histograma.png')
plt.close()

print('Propiedad de balance verificada. Resultado guardado en 1_balance.txt.') 