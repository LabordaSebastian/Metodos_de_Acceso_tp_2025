import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os

def ensure_dir_exists():
    """
    Asegura que el directorio de salida existe
    """
    output_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def calculate_autocorrelation(sequence):
    """
    Calcula la autocorrelación de la secuencia
    """
    # Convierte 0s a -1s para el cálculo de correlación
    sequence_bipolar = 2*sequence - 1
    # Calcula la autocorrelación sin normalizar
    autocorr = signal.correlate(sequence_bipolar, sequence_bipolar, mode='full')
    return autocorr

def plot_autocorrelation(autocorr, output_dir):
    """
    Grafica la autocorrelación
    """
    N = (len(autocorr) - 1) // 2
    lags = np.arange(-N, N + 1)
    
    plt.figure(figsize=(12, 6))
    plt.plot(lags, autocorr, 'b-', label='Autocorrelación')
    plt.grid(True)
    plt.xlabel('Desplazamiento τ')
    plt.ylabel('R(τ)')
    plt.title('Autocorrelación de Secuencia Kasami')
    plt.legend()
    
    plt.savefig(os.path.join(output_dir, 'kasami_autocorrelacion.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def main():
    output_dir = ensure_dir_exists()
    
    # Lee la secuencia del archivo
    kasami_sequence = np.loadtxt(os.path.join(output_dir, 'kasami_sequence.txt'), dtype=int)
    
    # Calcula la autocorrelación
    autocorr = calculate_autocorrelation(kasami_sequence)
    
    # Guarda los valores de autocorrelación
    np.savetxt(os.path.join(output_dir, 'kasami_autocorrelacion.txt'), autocorr, fmt='%d')
    
    # Grafica la autocorrelación
    plot_autocorrelation(autocorr, output_dir)
    
    print("Autocorrelación calculada y guardada")
    print(f"Gráfico guardado en {output_dir}/kasami_autocorrelacion.png")
    print(f"Valores guardados en {output_dir}/kasami_autocorrelacion.txt")

if __name__ == "__main__":
    main()