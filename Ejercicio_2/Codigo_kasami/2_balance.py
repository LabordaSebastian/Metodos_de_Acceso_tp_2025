import matplotlib.pyplot as plt
import os

# --- Configuración ---
INPUT_FILE = "kasami_sequence.txt"  # Archivo con la secuencia Kasami
OUTPUT_REPORT = "kasami_balance_report.txt"  # Reporte de análisis
OUTPUT_HISTOGRAM = "kasami_balance_histogram.png"  # Gráfico de balance

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
    
    # --- Leer secuencia del archivo ---
    try:
        with open(os.path.join(output_dir, INPUT_FILE), 'r') as f:
            # Limpia la secuencia eliminando espacios y saltos de línea
            sequence = list(map(int, f.read().strip().replace('\n', '').replace(' ', '')))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {INPUT_FILE}")
        exit()
    except ValueError as e:
        print(f"Error al procesar el archivo {INPUT_FILE}: {e}")
        exit()

    # --- Análisis de balance ---
    length = len(sequence)
    num_ones = sum(sequence)
    num_zeros = length - num_ones

    # Propiedades a evaluar
    is_mseq_balance = (num_ones == num_zeros + 1)  # Propiedad estricta para m-secuencias
    is_gold_balance = abs(num_ones - num_zeros) <= 1  # Tolerancia para códigos Gold

    # --- Generar reporte ---
    report_content = f"""Análisis de Balance - Secuencia Kasami
{'='*40}
Longitud total: {length} bits
• Unos: {num_ones} ({num_ones/length:.2%})
• Ceros: {num_zeros} ({num_zeros/length:.2%})
Diferencia: {abs(num_ones - num_zeros)}

Propiedades:
1. Balance m-secuencia (unos = ceros + 1): {'✔' if is_mseq_balance else '✖'}
2. Balance Gold (diferencia ≤ 1): {'✔' if is_gold_balance else '✖'}

Notas:
- Las m-secuencias siempre cumplen la propiedad 1 exactamente
- Los códigos Gold y Kasami generalmente cumplen la propiedad 2
"""

    with open(os.path.join(output_dir, OUTPUT_REPORT), 'w') as f:
        f.write(report_content)

    # --- Generar histograma ---
    plt.figure(figsize=(8, 5))
    bars = plt.bar(['Ceros', 'Unos'], 
                   [num_zeros, num_ones],
                   color=['#1f77b4', '#ff7f0e'],
                   width=0.6)

    plt.title(f'Distribución de Bits\nSecuencia Kasami de {length} bits', pad=20)
    plt.ylabel('Cantidad de bits')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Añadir valores encima de las barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height}\n({height/length:.1%})',
                 ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, OUTPUT_HISTOGRAM), dpi=120)
    plt.close()

    # --- Mostrar resultados ---
    print(report_content)
    print(f"\nResultados guardados en:")
    print(f"- Análisis: {os.path.join(output_dir, OUTPUT_REPORT)}")
    print(f"- Gráfico: {os.path.join(output_dir, OUTPUT_HISTOGRAM)}")

if __name__ == "__main__":
    main()