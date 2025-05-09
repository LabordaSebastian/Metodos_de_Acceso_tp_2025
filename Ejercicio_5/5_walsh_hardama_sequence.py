import numpy as np
import matplotlib.pyplot as plt

def generate_walsh_hadamard_matrix(n):
    """Generate Walsh-Hadamard matrix of size n x n"""
    if n == 1:
        return np.array([[1]])
    else:
        h = generate_walsh_hadamard_matrix(n//2)
        return np.vstack([np.hstack([h, h]), np.hstack([h, -h])])

def walsh_transform(signal, hadamard_matrix):
    """Perform Walsh transform on the signal"""
    return np.dot(hadamard_matrix, signal) / len(signal)

# Parámetros
N = 64  # Longitud de la secuencia
noise_variance = 0.1  # Varianza del ruido blanco
noise_std = np.sqrt(noise_variance)  # Desviación estándar del ruido

# Generar matriz de Walsh-Hadamard
hadamard_matrix = generate_walsh_hadamard_matrix(N)

# Obtener secuencias Walsh-Hadamard de orden 10 y 60
walsh_seq_10 = hadamard_matrix[10]  # Sequence 10
walsh_seq_60 = hadamard_matrix[60]  # Sequence 60

# Generar ruido blanco para ambas señales
white_noise_10 = np.random.normal(0, noise_std, N)
white_noise_60 = np.random.normal(0, noise_std, N)

# Combinar secuencias con ruido
signal_10 = walsh_seq_10 + white_noise_10
signal_60 = walsh_seq_60 + white_noise_60

# Calcular las transformadas de Walsh-Hadamard
wht_10 = walsh_transform(signal_10, hadamard_matrix)
wht_60 = walsh_transform(signal_60, hadamard_matrix)

# Visualización
plt.figure(figsize=(12, 6))

# Graficar WHT vs sequence index para ambas secuencias
plt.plot(range(N), wht_10, 'b-', label='WHT 10', linewidth=1)
plt.plot(range(N), wht_60, 'r-', label='WHT 60', linewidth=1)
plt.xlabel('Sequence Index')
plt.ylabel('WHT Amplitude')
plt.title('Walsh-Hadamard Transform vs Sequence Index')
plt.grid(True)
plt.legend()

# Guardar la gráfica
plt.savefig('walsh_hadamard_transform.png')
plt.close()

# Exportar datos para el script de decodificación
data_to_save = {
    'walsh_seq_10': walsh_seq_10,
    'walsh_seq_60': walsh_seq_60,
    'signal_10': signal_10,
    'signal_60': signal_60
}
np.savez('walsh_hadamard_data.npz', **data_to_save)