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
samples_per_chip = int(Tc / ts)
signal_sampled = np.repeat(signal_bipolar, samples_per_chip)

# --- Cálculo de la FFT y PSD ---
N = len(signal_sampled)
fft_result = np.fft.fft(signal_sampled) / N  # Normalizar por N
freqs = np.fft.fftfreq(N, ts)
psd = np.abs(fft_result)**2  # PSD (magnitud al cuadrado)

# Centrar el espectro
psd_shifted = np.fft.fftshift(psd)
freqs_shifted = np.fft.fftshift(freqs)

# --- Graficar PSD ---
plt.figure(figsize=(12, 4))
markerline, stemlines, baseline = plt.stem(
    freqs_shifted / 1e6,  # Eje en MHz
    psd_shifted,
    linefmt='b-',
    markerfmt='bo',
    basefmt='k-',
)
plt.setp(stemlines, linewidth=0.5)
plt.setp(markerline, markersize=3)

# Añadir envolvente teórica
f_chip = Rc / 1e6  # Frecuencia de chip en MHz
x_env = np.linspace(-2 * f_chip, 2 * f_chip, 500)
y_env = (np.sinc(x_env / f_chip))**2
plt.plot(x_env, y_env * np.max(psd_shifted), 'r--', label='Envolvente teórica (sinc²)')

# Configuración del gráfico
plt.title('Densidad Espectral de Potencia (PSD) de la Señal PN')
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('DSP (Lineal)')
plt.grid(True, linestyle='--')
plt.xlim(-2 * f_chip, 2 * f_chip)
plt.ylim(0, np.max(psd_shifted) * 1.1)
plt.legend()

# Mostrar y guardar gráfico
plt.tight_layout()
plt.savefig('psd_pn_sequence.png', dpi=300, bbox_inches='tight')
plt.show()