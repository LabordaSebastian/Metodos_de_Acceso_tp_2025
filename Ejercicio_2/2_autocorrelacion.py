import numpy as np
import matplotlib.pyplot as plt

# --- Configuración ---
INPUT_FILE = "2_gold_sequence.txt"  # Archivo con la secuencia Gold
OUTPUT_REPORT = "2_autocorrelation_report.txt"  # Reporte de análisis
OUTPUT_PLOT = "2_autocorrelation_plot.png"  # Gráfico de autocorrelación

# --- Leer secuencia del archivo ---
try:
    with open(INPUT_FILE, 'r') as f:
        sequence = list(map(int, f.read().strip()))
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {INPUT_FILE}")
    exit()

# --- Convertir a formato bipolar (-1, 1) ---
bipolar_seq = np.array([1 if bit else -1 for bit in sequence])
N = len(bipolar_seq)

# --- Función de autocorrelación periódica ---
def periodic_autocorrelation(seq):
    corr = np.zeros(N)
    for shift in range(N):
        shifted = np.roll(seq, shift)
        corr[shift] = np.sum(seq * shifted)
    return corr

# --- Calcular autocorrelación ---
autocorr = periodic_autocorrelation(bipolar_seq)

# --- Desplazamientos (lags) ---
lags = np.arange(-N//2, N//2 + 1)
full_autocorr = np.concatenate((autocorr[N//2:], autocorr[:N//2 + 1]))

# --- Análisis teórico ---
peak_value = full_autocorr[N//2]  # Valor en τ=0
other_values = np.delete(full_autocorr, N//2)  # Todos los demás valores

# --- Generar reporte ---
report_content = f"""Análisis de Autocorrelación - Secuencia Gold
{'='*50}
Longitud de la secuencia (N): {N} bits
Valor teórico para τ=0: {N}
Valor teórico para τ≠0: -1

Resultados obtenidos:
• R(0) = {peak_value} (diferencia: {abs(peak_value - N)})
• Media de R(τ≠0): {np.mean(other_values):.2f}
• Desviación estándar de R(τ≠0): {np.std(other_values):.2f}
• Mínimo de R(τ≠0): {np.min(other_values):.2f}
• Máximo de R(τ≠0): {np.max(other_values):.2f}

Notas:
- Para códigos Gold ideales, se espera:
  - Pico en τ=0 igual a N
  - Valores bajos (≈ -1) para otros τ
- Los códigos Gold reales pueden mostrar pequeñas variaciones
"""

with open(OUTPUT_REPORT, 'w') as f:
    f.write(report_content)

# --- Graficar autocorrelación ---
plt.figure(figsize=(12, 6))
plt.plot(lags, full_autocorr, 'b-', linewidth=1.5)
plt.axhline(y=-1, color='r', linestyle='--', label='Valor teórico para τ≠0')
plt.axvline(x=0, color='g', linestyle=':', alpha=0.5)
plt.title(f'Autocorrelación Periódica de Secuencia Gold (N={N})')
plt.xlabel('Desplazamiento (τ)')
plt.ylabel('R(τ)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_PLOT, dpi=120)
plt.close()

# --- Mostrar resultados ---
print(report_content)
print(f"\nResultados guardados en:")
print(f"- Reporte: {OUTPUT_REPORT}")
print(f"- Gráfico: {OUTPUT_PLOT}")