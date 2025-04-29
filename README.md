# Trabajo Práctico: Propiedades de los Códigos PN

## Objetivo

El objetivo de este trabajo es comprender las propiedades de los códigos PN (Pseudo-Noise) y comparar los distintos tipos de códigos existentes, utilizando como referencia principal el libro "Digital Communications. Fundamentals and Applications" de Bernard Sklar.

## Implementación

Se realiza la simulación de un generador de secuencia PN, utilizando un registro de desplazamiento con realimentación lineal (LFSR), como se muestra en el diagrama de bloques adjunto.

**Nota:** Toda la implementación y análisis se realizará en **Python**, utilizando librerías como NumPy, Matplotlib y Scipy.

## Consigna

1. **Determinación del Período de la Señal**
   - Analizar la secuencia generada y calcular su período.

2. **Autocorrelación**
   - Graficar la autocorrelación de la secuencia para 3 períodos completos.
   - Extraer conclusiones sobre las propiedades de autocorrelación de los códigos PN.

3. **Densidad Espectral de Potencia (DSP)**
   - Calcular y graficar la DSP de la secuencia.
   - Analizar y extraer conclusiones sobre el espectro de la señal.

4. **Propiedad de Balance**
   - Verificar que la secuencia cumple con la propiedad de balance (número de unos y ceros en cada período).

5. **Propiedad de Corridas**
   - Verificar la propiedad de corridas (distribución de secuencias de unos y ceros consecutivos).

## Referencias

- Sklar, B., & Ray, P. K. (Año). *Digital Communications. Fundamentals and Applications*. [z-lib.org]
- Material de cátedra de Métodos de Acceso.

## Notas

- Todas las simulaciones y análisis se realizarán utilizando **Python**.
- Se recomienda documentar cada paso con gráficos y conclusiones claras.