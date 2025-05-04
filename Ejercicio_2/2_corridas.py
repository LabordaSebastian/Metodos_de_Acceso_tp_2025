import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# --- Configuración ---
INPUT_FILE = "Ejercicio_2/2_gold_sequence.txt"  # Archivo con la secuencia Gold
OUTPUT_REPORT = "Ejercicio_2/2_corridas_report.txt"  # Reporte de análisis
OUTPUT_HISTOGRAM = "Ejercicio_2/2_corridas_histogram.png"  # Gráfico de corridas

# --- Leer secuencia ---
try:
    with open(INPUT_FILE, 'r') as f:
        sequence = list(map(int, f.read().strip()))
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {INPUT_FILE}")
    exit()

# --- Función para contar corridas ---
def count_runs(seq):
    runs = []
    if not seq:
        return runs
    
    current_bit = seq[0]
    run_length = 1
    
    for bit in seq[1:]:
        if bit == current_bit:
            run_length += 1
        else:
            runs.append((current_bit, run_length))
            current_bit = bit
            run_length = 1
    runs.append((current_bit, run_length))
    return runs

# --- Análisis de corridas ---
runs = count_runs(sequence)
total_runs = len(runs)
run_stats = defaultdict(lambda: {'0': 0, '1': 0})

for bit, length in runs:
    run_stats[length][str(bit)] += 1

# --- Calcular estadísticas teóricas ---
n = int(np.log2(len(sequence) + 1))  # Estimación del grado del polinomio
expected_runs = 2**(n - 1)  # Total esperado de corridas (teoría m-secuencias)

# --- Generar reporte ---
report = f"""Análisis de Propiedad de Corridas - Código Gold
{'='*60}
Longitud de la secuencia: {len(sequence)} bits
Total de corridas encontradas: {total_runs}
Total esperado (teoría m-secuencias): ~{expected_runs}

Distribución por longitud:
{'Longitud':<10} | {'Ceros':<10} | {'Unos':<10} | {'Total':<10}
{'-'*45}
"""

max_length = max(run_stats.keys()) if run_stats else 0
for length in sorted(run_stats.keys()):
    ceros = run_stats[length]['0']
    unos = run_stats[length]['1']
    report += f"{length:<10} | {ceros:<10} | {unos:<10} | {ceros+unos:<10}\n"

report += f"""
Notas teóricas para m-secuencias:
1. Número total de corridas ≈ {expected_runs} (para n={n})
2. Distribución esperada:
   - 50% corridas de longitud 1
   - 25% de longitud 2
   - 12.5% de longitud 3, etc.
3. Balance: #corridas de unos ≈ #corridas de ceros
"""

with open(OUTPUT_REPORT, 'w') as f:
    f.write(report)

# --- Graficar histograma ---
lengths = sorted(run_stats.keys())
ceros = [run_stats[l]['0'] for l in lengths]
unos = [run_stats[l]['1'] for l in lengths]

plt.figure(figsize=(10, 6))
x = np.arange(len(lengths))
width = 0.35

plt.bar(x - width/2, ceros, width, label='Ceros', color='blue', alpha=0.7)
plt.bar(x + width/2, unos, width, label='Unos', color='orange', alpha=0.7)

plt.xlabel('Longitud de Corrida')
plt.ylabel('Cantidad de Corridas')
plt.title('Distribución de Corridas en Código Gold')
plt.xticks(x, lengths)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig(OUTPUT_HISTOGRAM, dpi=120)
plt.close()

# --- Mostrar resultados ---
print(report)
print(f"\nResultados guardados en:")
print(f"- Reporte: {OUTPUT_REPORT}")
print(f"- Histograma: {OUTPUT_HISTOGRAM}")