import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos guardados
data = np.load('walsh_hadamard_data.npz')
walsh_seq_10 = data['walsh_seq_10']
walsh_seq_60 = data['walsh_seq_60']
signal_10 = data['signal_10']
signal_60 = data['signal_60']

# Combinar señales (simulando la señal recibida)
received_signal = signal_10 + signal_60

# Decodificar señales usando la propiedad de ortogonalidad
N = len(received_signal)
decoded_10 = np.sum(received_signal * walsh_seq_10) * walsh_seq_10 / N
decoded_60 = np.sum(received_signal * walsh_seq_60) * walsh_seq_60 / N

# Visualización de la decodificación
plt.figure(figsize=(12, 8))

# Graficar señal original vs decodificada para secuencia 10
plt.subplot(2, 1, 1)
t = np.arange(len(signal_10))
plt.plot(t, signal_10, 'b-', label='Original Signal 10', linewidth=1)
plt.plot(t, decoded_10, 'r--', label='Decoded Signal 10', linewidth=1)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Original vs Decoded Signal - Walsh-Hadamard 10')
plt.grid(True)
plt.legend()

# Graficar señal original vs decodificada para secuencia 60
plt.subplot(2, 1, 2)
plt.plot(t, signal_60, 'b-', label='Original Signal 60', linewidth=1)
plt.plot(t, decoded_60, 'r--', label='Decoded Signal 60', linewidth=1)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Original vs Decoded Signal - Walsh-Hadamard 60')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('walsh_hadamard_decoded.png')
plt.close()

# Calcular error cuadrático medio para cada señal decodificada
mse_10 = np.mean((signal_10 - decoded_10) ** 2)
mse_60 = np.mean((signal_60 - decoded_60) ** 2)

print(f"Error cuadrático medio para señal 10: {mse_10:.6f}")
print(f"Error cuadrático medio para señal 60: {mse_60:.6f}")