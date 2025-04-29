# Script para determinar el período de la secuencia PN

# Leer la secuencia desde el archivo generado
with open('1_pn_sequence.txt', 'r') as f:
    secuencia = list(map(int, f.read().strip().split()))

# Buscar el período: la secuencia debe repetirse después de su longitud máxima
# Buscamos el menor período p tal que secuencia[:p] == secuencia[p:2*p]
def encontrar_periodo(seq):
    for p in range(1, len(seq)):
        if seq[:p] == seq[p:2*p]:
            return p
    return len(seq)

periodo = encontrar_periodo(secuencia)

# Guardar el resultado en un archivo .txt
with open('1_periodo.txt', 'w') as f:
    f.write(f"Período de la secuencia PN: {periodo}\n")
    f.write(f"Secuencia analizada: {len(secuencia)} bits\n")

print(f"Período de la secuencia PN: {periodo} (resultado guardado en 1_periodo.txt)") 