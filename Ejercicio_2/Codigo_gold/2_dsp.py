import numpy as np
import matplotlib.pyplot as plt

# Configuración
INPUT_FILE = "2_gold_sequence.txt"
Rc = 1.2288e6
Tc = 1 / Rc
fs = 10 * Rc
ts = 1 / fs

# Leer secuencia Gold
try:
    with open(INPUT_FILE, 'r') as f:
        gold_sequence = np.array(list(map(int, f.read().strip())))
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {INPUT_FILE}")
    exit()

# Procesamiento
signal_bipolar = 2 * gold_sequence - 1
samples_per_chip = int(Tc / ts)
signal_sampled = np.repeat(signal_bipolar, samples_per_chip)
N = len(signal_sampled)

# Cálculo PSD
fft_result = np.fft.fft(signal_sampled) / N
freqs = np.fft.fftfreq(N, ts)
psd = np.abs(fft_result)**2
psd_shifted = np.fft.fftshift(psd)
freqs_shifted = np.fft.fftshift(freqs)

# Gráfico
plt.figure(figsize=(14, 5))
markerline, stemlines, baseline = plt.stem(
    freqs_shifted / 1e6,
    psd_shifted,
    linefmt='b-',
    markerfmt='bo',
    basefmt='k-',
)
plt.setp(stemlines, 'linewidth', 0.7)
plt.setp(markerline, 'markersize', 3)

# Envolvente teórica mejorada
f_chip = Rc / 1e6
x_env = np.linspace(-2.5 * f_chip, 2.5 * f_chip, 500)
y_env = (np.sinc(x_env / f_chip))**2
plt.plot(x_env, y_env * np.max(psd_shifted), 'r--', linewidth=1.5, label='Envolvente teórica (sinc²)')

plt.title('Densidad Espectral de Potencia (PSD) - Secuencia Gold\n'
          f'Tasa de chip: {Rc/1e6} MHz | Longitud: {len(gold_sequence)} chips')
plt.xlabel('Frecuencia (MHz)')
plt.ylabel('DSP (Lineal)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-2.5, 2.5)
plt.ylim(0, np.max(psd_shifted) * 1.1)
plt.tight_layout()
plt.savefig('gold_sequence_psd_enhanced.png', dpi=300)
plt.close()

# Guardar datos (opcional)
with open('gold_sequence_psd_data.txt', 'w') as f:
    f.write('Frecuencia (MHz)\tDSP (Lineal)\n')
    for frq, val in zip(freqs_shifted/1e6, psd_shifted):
        f.write(f'{frq:.4f}\t{val:.6f}\n')