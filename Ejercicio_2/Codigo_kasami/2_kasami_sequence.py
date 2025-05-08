import numpy as np
import matplotlib.pyplot as plt
import os

def ensure_dir_exists():
    """
    Asegura que el directorio de salida existe
    """
    # Obtiene el directorio donde está el script
    output_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def generate_msequence(polynomial, initial_state):
    """
    Genera una secuencia-m usando LFSR
    polynomial: lista con las posiciones de los taps (1-based indexing)
    initial_state: estado inicial del registro
    """
    n = len(initial_state)
    sequence = []
    state = list(initial_state)  # Convertimos a lista Python
    
    for _ in range(2**n - 1):
        sequence.append(state[0])
        feedback = sum(state[tap-1] for tap in polynomial) % 2  # XOR de los taps
        state = [feedback] + state[:-1]
    
    return np.array(sequence)

def decimate_sequence(sequence, factor):
    """
    Diezma una secuencia por un factor dado
    """
    N = len(sequence)
    decimated = []
    for i in range(N):
        decimated.append(sequence[(i * factor) % N])
    return np.array(decimated)

def generate_single_kasami(m=6):
    """
    Genera una única secuencia Kasami
    m: grado del polinomio (debe ser par)
    """
    # Polinomio generador y estado inicial para m=6
    polynomial = [6, 1]  # x^6 + x + 1
    initial_state = [1, 1, 1, 1, 1, 1]  # Estado inicial todo en 1s
    
    # Genera secuencia m
    sequence_m = generate_msequence(polynomial, initial_state)
    
    # Diezma la secuencia
    decimation = 2**(m//2) + 1
    sequence_y = decimate_sequence(sequence_m, decimation)
    
    # Genera secuencia Kasami mediante XOR
    kasami = np.logical_xor(sequence_m, sequence_y)
    
    return kasami.astype(int)

def plot_kasami_sequence(sequence, output_dir):
    """
    Grafica la secuencia Kasami en el dominio del tiempo
    """
    Rc = 1.2288e6  # Hz
    Tc = 1/Rc      # segundos
    
    # Genera vector de tiempo
    t = np.arange(len(sequence)) * Tc
    
    # Configura el gráfico
    plt.figure(figsize=(12, 4))
    plt.step(t*1e6, sequence, 'b-', where='post', label='Secuencia Kasami')
    plt.grid(True)
    plt.xlabel('Tiempo (µs)')
    plt.ylabel('Amplitud')
    plt.title('Secuencia Kasami en el Dominio del Tiempo')
    plt.legend()
    plt.ylim(-0.2, 1.2)
    
    # Guarda el gráfico
    plt.savefig(os.path.join(output_dir, 'kasami_sequence_temporal.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()

def main():
    output_dir = ensure_dir_exists()
    
    # Genera la secuencia
    kasami_sequence = generate_single_kasami()
    
    # Guarda la secuencia en una sola fila
    output_file = os.path.join(output_dir, 'kasami_sequence.txt')
    np.savetxt(output_file, [kasami_sequence], fmt='%d', delimiter=' ')
    
    # Grafica la secuencia
    plot_kasami_sequence(kasami_sequence, output_dir)
    
    print(f"Longitud de la secuencia: {len(kasami_sequence)}")
    print(f"Secuencia guardada en {output_file}")
    print(f"Gráfico guardado en {output_dir}/kasami_sequence_temporal.png")

if __name__ == "__main__":
    main()