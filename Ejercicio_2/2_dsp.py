import numpy as np
import matplotlib.pyplot as plt

# --- Configuración ---
INPUT_FILE = "Ejercicio_2/2_gold_sequence.txt"  # Archivo con la secuencia Gold
Rc = 1.2288e6                      # Tasa de chip (ejemplo: CDMA)
Tc = 1 / Rc                         # Duración de un chip (0.814 µs)
fs = 10 * Rc                        # Frecuencia de muestreo (10 veces Rc)
ts = 1 / fs                         # Período de muestreo

# --- Leer secuencia Gold ---
try:
    with open(INPUT_FILE, 'r') as f:
        gold_sequence = np.array(list(map(int, f.read().strip())))
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {INPUT_FILE}")
    exit()

# --- Convertir a señal bipolar (-1, 1) ---
signal_bipolar = 2 * gold_sequence - 1

# --- Muestrear la señal ---
samples_per_chip = int(Tc / ts)
signal_sampled = np.repeat(signal_bipolar, samples_per_chip)
N = len(signal_sampled)

# --- Calcular FFT ---
fft_result = np.fft.fft(signal_sampled) / N  # Normalizada
freqs = np.fft.fftfreq(N, ts)
psd = np.abs(fft_result)**2  # Densidad espectral de potencia

# --- Centrar el espectro ---
psd_shifted = np.fft.fftshift(psd)
freqs_shifted = np.fft.fftshift(freqs)

# --- Graficar ---
plt.figure(figsize=(14, 5))

# Gráfico estilo stem (líneas discretas)
markerline, stemlines, baseline = plt.stem(
    freqs_shifted / 1e6,  # Convertir a MHz
    psd_shifted,
    linefmt='b-',
    markerfmt='bo',
    basefmt='k-',
)
plt.setp(stemlines, 'linewidth', 0.7)
plt.setp(markerline, 'markersize', 3)

# Añadir envolvente teórica (sinc²)
f_chip = Rc / 1e6  # Frecuencia de chip en MHz
x_env = np.linspace(-2*f_chip, 2*f_chip, 500)
y_env = (np.sinc(x_env / f_chip))**2
plt.plot(x_env, y_env * np.max(psd_shifted), 'r--', label='Envolvente teórica (sinc²)')

plt.title('Densidad Espectral de Potencia (DSP) del Código Gold\n'
          f'Tasa de chip: {Rc/1e6} MHz | Longitud: {len(gold_sequence)} chips')
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('DSP (Lineal)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-2.5, 2.5)
plt.tight_layout()
plt.savefig('2_gold_sequence_psd.png', dpi=150)
plt.close()

# --- Guardar datos numéricos ---
with open('2_gold_sequence_psd_data.txt', 'w') as f:
    f.write('Frecuencia (MHz)\tDSP (Lineal)\n')
    for frq, val in zip(freqs_shifted/1e6, psd_shifted):
        f.write(f'{frq:.4f}\t{val:.6f}\n')

print("Análisis completado:")
print(f"- Gráfico DSP guardado como '2_gold_sequence_psd.png'")
print(f"- Datos numéricos guardados en '2_gold_sequence_psd_data.txt'")