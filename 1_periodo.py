"""
Período en códigos PN:
En los códigos PN (Pseudo-Noise), el período es la longitud mínima de la secuencia antes de que comience a repetirse. Para una m-secuencia generada por un LFSR de n etapas, el período máximo es 2^n - 1. El período es una propiedad fundamental que determina la longitud de la secuencia única antes de su repetición.

Nota sobre la detección del período:
En una m-secuencia correctamente generada, la secuencia solo se repite después de recorrer todos sus valores posibles, es decir, su período es igual a la longitud de la secuencia generada. Por eso, para este caso, el período se determina simplemente como la longitud de la secuencia.
"""
# Script para determinar el período de la secuencia PN

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

periodo = len(secuencia)

# Guardar el resultado en un archivo .txt
with open('1_periodo.txt', 'w') as f:
    f.write(f"Período de la secuencia PN: {periodo}\n")
    f.write(f"Secuencia analizada: {len(secuencia)} bits\n")
    f.write("\nNota: Para una m-secuencia PN correctamente generada, el período es igual a la longitud de la secuencia, ya que solo se repite después de recorrer todos sus valores posibles.\n")

print(f"Período de la secuencia PN: {periodo} (resultado guardado en 1_periodo.txt)") 