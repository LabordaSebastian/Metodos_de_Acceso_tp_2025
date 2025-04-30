"""
Densidad Espectral de Potencia (DSP):
La DSP es la Transformada de Fourier de la función de autocorrelación (Teorema de Wiener-Khinchin).
Para una secuencia PN periódica, el espectro está compuesto por líneas discretas separadas 
según el período de la secuencia, con amplitudes que siguen una envolvente tipo sinc².
Referencia: MetAccesoCap3-2022.pdf, Fig 3.6
"""
import numpy as np
import matplotlib.pyplot as plt

# Leer la autocorrelación desde el archivo generado por 1_autocorrelacion.py
with open('1_autocorrelacion.txt', 'r') as f:
    lines = f.readlines()
    # Leer N
    for line in lines:
        if line.startswith('Longitud de la secuencia (N):'):
            N = int(line.split(':')[1].strip())
            break
    
    # Buscar la sección de valores de autocorrelación
    for i, line in enumerate(lines):
        if line.strip() == 'Valores de autocorrelación R(τ):':
            # Los valores están en las líneas siguientes
            valores_autocorr = np.loadtxt(lines[i+1:])
            break

# Extraer un período centrado en 0 (N puntos)
centro = len(valores_autocorr) // 2
inicio = centro - N//2
fin = inicio + N
autocorr_periodo = valores_autocorr[inicio:fin]

# Calcular la DSP con más puntos para ver mejor la forma de sinc
nfft = 1024  # Más puntos para la envolvente
dsp = np.abs(np.fft.fft(autocorr_periodo, n=nfft))**2

# Calcular frecuencias en Hz (asumiendo frecuencia de chip = 1 Hz)
fc = 1.0  # Frecuencia de chip en Hz
freq = np.fft.fftfreq(nfft, d=1/fc)

# Reordenar para centrar en cero
dsp = np.fft.fftshift(dsp)
freq = np.fft.fftshift(freq)

# Normalizar solo la amplitud
dsp = dsp/np.max(dsp)

# Graficar la DSP
plt.figure(figsize=(12,6))

# Graficar solo la envolvente continua
plt.plot(freq, dsp, 'b-', linewidth=2, label='Envolvente tipo sinc²')

plt.title('Densidad Espectral de Potencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|S(f)|²')
plt.grid(True, alpha=0.3)
plt.xlim(-0.1*fc, 0.1*fc)
plt.ylim(-0.1, 1.1)
plt.legend()

plt.tight_layout()
plt.savefig('1_dsp.png', dpi=300)
plt.close()

# Guardar conclusiones
with open('1_dsp.txt', 'w') as f:
    f.write('Densidad Espectral de Potencia (DSP) de la secuencia PN\n')
    f.write('===========================================\n\n')
    f.write(f'Longitud de la secuencia (N): {N}\n\n')
    f.write('Método de cálculo:\n')
    f.write('- La DSP se calculó usando el Teorema de Wiener-Khinchin\n')
    f.write('- Se utilizó un período de la autocorrelación centrado en 0\n')
    f.write('- Frecuencias expresadas en Hz (fc = 1 Hz)\n\n')
    f.write('Características de la DSP:\n')
    f.write('- La envolvente sigue una forma de sinc² característica\n')
    f.write('- El ancho del lóbulo principal es inversamente proporcional a N\n')
    f.write(f'- La gráfica se centró en [-0.1, 0.1] Hz para mejor visualización del lóbulo principal\n')

print('DSP calculada y graficada con frecuencias en Hz (ver 1_dsp.png). Conclusiones guardadas en 1_dsp.txt.') 