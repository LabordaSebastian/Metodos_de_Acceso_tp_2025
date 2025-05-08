import numpy as np
import matplotlib.pyplot as plt

# --- Configuración ---
Rc = 1.2288e6  # Tasa de chip (ej: CDMA)
Tc = 1 / Rc     # Duración de un chip (0.814 µs)
n = 6            # Grado de los polinomios
N = 2**n - 1     # Longitud teórica de la secuencia (63 bits)

# --- Polinomios ---
poly1 = 0b1000011  # [6,1] → x^6 + x + 1
poly2 = 0b1100111  # [6,5,2,1] → x^6 + x^5 + x^2 + x + 1

# --- Semilla ---
seed = 0b000001    # 6 bits (LSB es la salida)

# --- Generador LFSR ---
def lfsr(seed, poly, length):
    state = seed
    seq = []
    for _ in range(length):
        seq.append(state & 1)
        if poly == 0b1000011:  # Para poly1
            feedback = (state >> 5) ^ (state >> 0)
        elif poly == 0b1100111:  # Para poly2
            feedback = (state >> 5) ^ (state >> 4) ^ (state >> 1) ^ (state >> 0)
        state = (state >> 1) | ((feedback & 1) << (n-1))
    return seq

# --- Generar secuencias ---
m_seq1 = lfsr(seed, poly1, N)
m_seq2 = lfsr(seed, poly2, N)
gold_code = [m_seq1[i] ^ m_seq2[i] for i in range(N)]  # k=0

# --- Medir longitud de la secuencia ---
longitud = len(gold_code)

# --- Guardar secuencia en archivo ---
with open("2_gold_sequence.txt", "w") as f:
    f.write("".join(map(str, gold_code)))

# --- Graficar ---
plt.figure(figsize=(12, 4))
plt.step(np.arange(N) * Tc * 1e6, gold_code, where='post', linewidth=1.5, color='blue')
plt.title(f'Código Gold (n={n}, k=0)\nLongitud: {longitud} bits', pad=20)
plt.xlabel('Tiempo (µs)')
plt.ylabel('Nivel')
plt.yticks([0, 1])
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, N * Tc * 1e6)

# --- Guardar figura ---
plt.savefig("2_gold_sequence.png", dpi=300, bbox_inches='tight')
plt.show()

# --- Mostrar resultados ---
print("="*50)
print(f"Longitud de la secuencia generada: {longitud} bits")
print("Secuencia Gold guardada en '2_gold_sequence.txt'")
print("Figura guardada como '2_gold_sequence.png'")
print("\nPrimeros 10 bits del código Gold:", "".join(map(str, gold_code[:10])))
print("="*50)