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

def plot_temporal_signal(sequence, Rc, output_dir):
    """
    Grafica la señal temporal
    """
    Tc = 1/Rc
    t = np.arange(len(sequence)) * Tc
    
    plt.figure(figsize=(12, 4))
    plt.step(t*1e6, sequence, 'b-', where='post')
    plt.grid(True)
    plt.xlabel('Tiempo (µs)')
    plt.ylabel('Amplitud')
    plt.title('Secuencia Kasami')
    plt.savefig(os.path.join(output_dir, 'kasami_sequence_temporal.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def plot_psd(freq, psd, output_dir):
    """
    Grafica la densidad espectral de potencia
    """
    plt.figure(figsize=(12, 6))
    plt.plot(freq/1e6, psd)
    plt.grid(True)
    plt.xlabel('Frecuencia (MHz)')
    plt.ylabel('Densidad Espectral de Potencia')
    plt.title('Densidad Espectral de Potencia - Secuencia Kasami')
    plt.savefig(os.path.join(output_dir, 'kasami_sequence_dsp.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def main():
    output_dir = ensure_dir_exists()
    
    # Parámetros
    Rc = 1.2288e6  # Hz
    Tc = 1/Rc
    
    # Lee la secuencia del archivo
    kasami_sequence = np.loadtxt(os.path.join(output_dir, 'kasami_sequence.txt'), dtype=int)
    N = len(kasami_sequence)
    
    # Grafica señal temporal
    plot_temporal_signal(kasami_sequence, Rc, output_dir)
    
    # Calcula y grafica PSD
    fft_result = np.fft.fft(kasami_sequence)
    fft_shifted = np.fft.fftshift(fft_result)
    freq = np.fft.fftshift(np.fft.fftfreq(N, Tc))
    psd = np.abs(fft_shifted)**2
    
    plot_psd(freq, psd, output_dir)
    
    # Guarda resultados
    np.savetxt(os.path.join(output_dir, 'kasami_sequence_dsp.txt'), 
               np.column_stack((freq, psd)), 
               header='Frecuencia(Hz) PSD', 
               delimiter='\t')
    
    print("Densidad espectral de potencia calculada")
    print(f"Gráficos guardados en {output_dir}")
    print(f"Valores guardados en {output_dir}/kasami_sequence_dsp.txt")

if __name__ == "__main__":
    main()