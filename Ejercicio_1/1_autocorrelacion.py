"""
Autocorrelación:
La autocorrelación periódica de una secuencia PN debe dar exactamente N cuando τ=0 y -1 para todo otro τ.
Referencia: MetAccesoCap3-2022.pdf, página 6, Fig 3.5
"""
import numpy as np
import matplotlib.pyplot as plt

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

# Convertir la secuencia de {0,1} a {-1,1} para la autocorrelación
secuencia_bipolar = np.array([2*x - 1 for x in secuencia])
N = len(secuencia_bipolar)

def autocorrelacion_periodica(x):
    """
    Calcula la autocorrelación periódica de la secuencia.
    Para una m-secuencia debe dar:
    R(0) = N
    R(τ) = -1 para τ ≠ 0
    """
    resultado = np.zeros(2*N + 7)  # De -N-3 a N+3
    for i, tau in enumerate(range(-N-3, N+4)):
        # Correlación periódica
        seq_rotada = np.roll(x, tau % N)  # Usamos módulo N para mantener la periodicidad
        resultado[i] = np.sum(x * seq_rotada)
    return resultado

# Calcular la autocorrelación periódica desde -N-3 hasta N+3
lags = np.arange(-N-3, N+4)  # Eje x extendido
autocorr = autocorrelacion_periodica(secuencia_bipolar)

# Graficar
plt.figure(figsize=(12,6))
plt.plot(lags, autocorr, '-', linewidth=2, color='blue')  # Línea continua
plt.title('Autocorrelación Periódica de la secuencia PN')
plt.xlabel('τ')
plt.ylabel('R(τ)')
plt.grid(True, alpha=0.3)  # Grid sutil
plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
plt.axhline(y=-1, color='g', linestyle='--', alpha=0.5, label='R(τ)=-1')
plt.axhline(y=N, color='g', linestyle='--', alpha=0.5, label=f'R(0)={N}')
plt.legend()
plt.tight_layout()
plt.savefig('1_autocorrelacion.png', dpi=300)  # Alta resolución
plt.close()

# Verificar los valores teóricos
indice_central = N + 3  # Ajustado al nuevo rango
valores_pico = autocorr[indice_central]  # Valor en τ=0
valores_resto = np.delete(autocorr, indice_central)  # Todos los demás valores
print(f"Valor en τ=0: {valores_pico} (debería ser {N})")
print(f"Valores para otros τ: media={np.mean(valores_resto):.2f}, std={np.std(valores_resto):.2f} (deberían ser -1)")

# Guardar conclusiones en un archivo .txt
with open('1_autocorrelacion.txt', 'w') as f:
    f.write('Autocorrelación Periódica de la secuencia PN\n')
    f.write('===========================================\n\n')
    f.write(f'Longitud de la secuencia (N): {N}\n')
    f.write(f'Valor teórico R(0): {N}\n')
    f.write('Valor teórico R(τ) para τ≠0: -1\n\n')
    f.write('Valores obtenidos:\n')
    f.write(f'R(0) = {valores_pico}\n')
    f.write(f'R(τ) promedio para otros τ: {np.mean(valores_resto):.2f}\n')
    f.write(f'Desviación estándar de R(τ) para otros τ: {np.std(valores_resto):.2f}\n')

print('Autocorrelación periódica calculada y graficada (ver 1_autocorrelacion.png). Conclusiones guardadas en 1_autocorrelacion.txt.') 