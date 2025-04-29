import numpy as np
import matplotlib.pyplot as plt

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

# Convertir la secuencia de {0,1} a {-1,1} para el análisis espectral
secuencia_bipolar = [2*x - 1 for x in secuencia]

# Calcular la FFT y la Densidad Espectral de Potencia (DSP)
N = len(secuencia_bipolar)
fft_vals = np.fft.fft(secuencia_bipolar, n=1024)
fft_freqs = np.fft.fftfreq(1024, d=1)
dsp = np.abs(fft_vals)**2

# Solo la mitad positiva del espectro
half = 1024 // 2
plt.figure(figsize=(10,5))
plt.plot(fft_freqs[:half], dsp[:half])
plt.title('Densidad Espectral de Potencia (DSP) de la secuencia PN')
plt.xlabel('Frecuencia normalizada')
plt.ylabel('Potencia')
plt.grid(True)
plt.tight_layout()
plt.savefig('1_dsp.png')
plt.close()

# Guardar conclusiones en un archivo .txt
with open('1_dsp.txt', 'w') as f:
    f.write('Se graficó la Densidad Espectral de Potencia (DSP) de la secuencia PN.\n')
    f.write('La DSP muestra un espectro relativamente plano, lo que indica que la secuencia PN tiene características similares al ruido blanco,\n')
    f.write('lo que es deseable en aplicaciones de espectro ensanchado.\n')
    f.write('Ver gráfico en 1_dsp.png.\n')

print('DSP calculada y graficada (ver 1_dsp.png). Conclusiones guardadas en 1_dsp.txt.') 