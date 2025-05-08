"""
Densidad Espectral de Potencia (DSP):
La DSP es la Transformada de Fourier de la función de autocorrelación (Teorema de Wiener-Khinchin).
Para una secuencia PN periódica, el espectro está compuesto por líneas discretas separadas 
según el período de la secuencia, con amplitudes que siguen una envolvente tipo sinc².
"""
import numpy as np
import matplotlib.pyplot as plt
import os

def ensure_dir_exists():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def main():
    output_dir = ensure_dir_exists()
    
    # Parámetros
    Rc = 1.2288e6
    Tc = 1 / Rc
    fs = 10 * Rc
    ts = 1 / fs
    
    # Leer secuencia Kasami
    kasami_sequence = np.loadtxt(os.path.join(output_dir, 'kasami_sequence.txt'), dtype=int)
    signal_bipolar = 2 * kasami_sequence - 1
    
    # Muestreo
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
    plt.figure(figsize=(12, 5))
    markerline, stemlines, baseline = plt.stem(
        freqs_shifted / 1e6,
        psd_shifted,
        linefmt='b-',
        markerfmt='bo',
        basefmt='k-',
    )
    plt.setp(stemlines, linewidth=0.5)
    plt.setp(markerline, markersize=3)

    # Envolvente teórica
    f_chip = Rc / 1e6
    x_env = np.linspace(-2.5 * f_chip, 2.5 * f_chip, 500)
    y_env = (np.sinc(x_env / f_chip))**2
    plt.plot(x_env, y_env * np.max(psd_shifted), 'r--', label='Envolvente teórica (sinc²)')

    plt.title('Densidad Espectral de Potencia (PSD) - Secuencia Kasami\n'
              f'Tasa de chip: {Rc/1e6} MHz | Longitud: {len(kasami_sequence)} chips')
    plt.xlabel('Frecuencia (MHz)')
    plt.ylabel('DSP (Lineal)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(-2.5 * f_chip, 2.5 * f_chip)
    plt.ylim(0, np.max(psd_shifted) * 1.1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'kasami_sequence_psd.png'), dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()