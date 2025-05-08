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
    """
    Asegura que el directorio de salida existe
    """
    output_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def main():
    output_dir = ensure_dir_exists()
    
    # Parámetros
    Rc = 1.2288e6          # Tasa de chip (chips/segundo)
    Tc = 1 / Rc            # Duración de un chip (segundos)
    fs = 10 * Rc           # Frecuencia de muestreo (10 veces Rc para resolución)
    ts = 1 / fs            # Período de muestreo
    
    # Lee la secuencia Kasami del archivo
    kasami_sequence = np.loadtxt(os.path.join(output_dir, 'kasami_sequence.txt'), dtype=int)
    
    # Convierte a señal bipolar (-1, +1)
    signal_bipolar = 2 * kasami_sequence - 1
    
    # --- Señal temporal muestreada (1 período) ---
    samples_per_chip = int(Tc / ts)
    signal_sampled = np.repeat(signal_bipolar, samples_per_chip)
    t = np.arange(0, len(signal_sampled) * ts, ts)
    
    # Graficar señal temporal
    plt.figure(figsize=(12, 4))
    plt.plot(t, signal_sampled, color='blue')
    plt.title('Señal Kasami Muestreada en el Tiempo (1 Período)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True, linestyle='--')
    plt.xlim(0, len(kasami_sequence) * Tc)
    plt.ylim(-1.5, 1.5)
    plt.savefig(os.path.join(output_dir, 'kasami_sequence_temporal.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    # --- Cálculo de la FFT ---
    N = len(signal_sampled)
    fft_result = np.fft.fft(signal_sampled) / N  # Normalizar por N
    freqs = np.fft.fftfreq(N, ts)
    fft_magnitude = np.abs(fft_result)
    
    # Centrar el espectro
    fft_magnitude_shifted = np.fft.fftshift(fft_magnitude)
    freqs_shifted = np.fft.fftshift(freqs)
    
    # Graficar la DSP usando stem
    plt.figure(figsize=(12, 4))
    markerline, stemlines, baseline = plt.stem(
        freqs_shifted, 
        fft_magnitude_shifted, 
        linefmt='b-',          # Líneas azules continuas
        markerfmt='bo',        # Marcadores azules circulares
        basefmt='k-',          # Línea base negra
    )
    plt.setp(stemlines, linewidth=0.5)  # Grosor de líneas
    plt.setp(markerline, markersize=3)  # Tamaño de marcadores
    
    plt.title('Espectro de la Señal Kasami (FFT) - Centrado en Cero')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud (Lineal)')
    plt.grid(True, linestyle='--')
    plt.xlim(-2 * Rc, 2 * Rc)
    plt.ylim(0, np.max(fft_magnitude_shifted) * 1.1)
    
    plt.savefig(os.path.join(output_dir, 'kasami_sequence_dsp.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print("DSP calculada y guardada correctamente")

if __name__ == "__main__":
    main()