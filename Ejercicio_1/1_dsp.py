"""
Densidad Espectral de Potencia (DSP):
La DSP es la Transformada de Fourier de la función de autocorrelación (Teorema de Wiener-Khinchin).
Para una secuencia PN periódica, el espectro está compuesto por líneas discretas separadas 
según el período de la secuencia, con amplitudes que siguen una envolvente tipo sinc².
Referencia: MetAccesoCap3-2022.pdf, Fig 3.6
"""
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
Rc = 1.2288e6          # Tasa de chip (chips/segundo)
Tc = 1 / Rc            # Duración de un chip (segundos)
fs = 10 * Rc           # Frecuencia de muestreo (10 veces Rc para resolución)
ts = 1 / fs            # Período de muestreo

# Secuencia PN proporcionada (mapeada a bipolar: 0 -> -1, 1 -> +1)
pn_sequence = np.array([
    0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 
    1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1
])
signal_bipolar = 2 * pn_sequence - 1  # Señal bipolar

# --- Señal temporal muestreada (1 período) ---
# Número de muestras por chip
samples_per_chip = int(Tc / ts)
# Repetir cada valor de la secuencia 'samples_per_chip' veces
signal_sampled = np.repeat(signal_bipolar, samples_per_chip)
# Crear eje de tiempo
t = np.arange(0, len(signal_sampled) * ts, ts)

# Graficar señal temporal (1 período)
plt.figure(figsize=(12, 4))
plt.plot(t, signal_sampled, color='blue')
plt.title('Señal PN Muestreada en el Tiempo (1 Período)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True, linestyle='--')
plt.xlim(0, len(pn_sequence) * Tc)
plt.ylim(-1.5, 1.5)
plt.savefig('pn_sequence_temporal.png', dpi=300, bbox_inches='tight')
plt.show()

# --- Cálculo de la FFT ---
N = len(signal_sampled)
fft_result = np.fft.fft(signal_sampled) / N  # Normalizar por N
freqs = np.fft.fftfreq(N, ts)
fft_magnitude = np.abs(fft_result)

# Centrar el espectro
fft_magnitude_shifted = np.fft.fftshift(fft_magnitude)
freqs_shifted = np.fft.fftshift(freqs)

# Graficar la magnitud de la FFT (PSD lineal)
#plt.figure(figsize=(12, 4))
#plt.plot(freqs_shifted, fft_magnitude_shifted, color='red')
#plt.title('Espectro de la Señal PN (FFT) - Centrado en Cero')
#plt.xlabel('Frecuencia (Hz)')
#plt.ylabel('Magnitud (Lineal)')
#plt.grid(True, linestyle='--')
#plt.xlim(-2 * Rc, 2 * Rc)
#plt.ylim(0, np.max(fft_magnitude_shifted) * 1.1)
#plt.show()

plt.figure(figsize=(12, 4))
markerline, stemlines, baseline = plt.stem(
    freqs_shifted, 
    fft_magnitude_shifted, 
    linefmt='b-',          # Líneas rojas continuas
    markerfmt='bo',        # Marcadores rojos circulares
    basefmt='k-',          # Línea base negra
)
plt.setp(stemlines, linewidth=0.5)  # Grosor de líneas
plt.setp(markerline, markersize=3)  # Tamaño de marcadores
plt.title('Espectro de la Señal PN (FFT) - Centrado en Cero')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (Lineal)')
plt.grid(True, linestyle='--')
plt.xlim(-2 * Rc, 2 * Rc)
plt.ylim(0, np.max(fft_magnitude_shifted) * 1.1)
plt.savefig('dsp_pn_sequence.png', dpi=300, bbox_inches='tight')
plt.show()