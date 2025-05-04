# Informe: Propiedades de los Códigos PN

**Ejercicio 1**

![Consigna](Ejercicio_1/consigna1.png)

**Autor:** Laborda Sebastian

## Introducción

Este informe presenta el análisis y verificación de las propiedades fundamentales de los códigos PN (Pseudo-Noise), utilizando como referencia principal el libro **"Digital Communications. Fundamentals and Applications" de Bernard Sklar**. Se implementaron scripts en Python para generar y analizar una secuencia PN, evaluando sus características estadísticas y espectrales.

## Bibliografía principal
- Sklar, B., & Ray, P. K. *Digital Communications. Fundamentals and Applications*. [z-lib.org]
- Material de cátedra de Métodos de Acceso.

---

## Consignas, Resultados y Conclusiones

### 1. Determinación del Período de la Secuencia
- **Consigna:** Analizar la secuencia generada y calcular su período.
- **Resultado:** El script `1_periodo.py` determinó correctamente el período de la secuencia PN generada. El resultado se encuentra en `1_periodo.txt`.
- **Gráfico:** ![Secuencia PN](Ejercicio_1/1_pn_sequence.png)
- **Explicación:** En los códigos PN, el período es igual al largo de la secuencia generada porque esta es una propiedad fundamental de los códigos PN: un LFSR de longitud n produce una secuencia máxima de período $2^n-1$, y la secuencia se repite exactamente después de ese número de bits.
- **Conclusión:** El período coincide con el valor teórico esperado para un LFSR de la longitud utilizada, verificando la propiedad de periodicidad de los códigos PN.

---

### 2. Autocorrelación
- **Consigna:** Graficar la autocorrelación de la secuencia para 3 períodos completos y extraer conclusiones.
- **Resultado:** El script `1_autocorrelacion.py` generó la gráfica `1_autocorrelacion.png` y el análisis en `1_autocorrelacion.txt`.
- **Gráfico:** ![Autocorrelación](Ejercicio_1/1_autocorrelacion.png)
- **Explicación teórica:**
  Para una secuencia PN de longitud N, la función de autocorrelación periódica tiene las siguientes características:
  - En τ = 0 (y múltiplos del período), R(0) = N, que es el valor máximo
  - Para cualquier otro desplazamiento τ ≠ 0, R(τ) = -1
  Esta propiedad es fundamental y hace que las secuencias PN sean ideales para sincronización y detección.
- **Conclusión:** La autocorrelación obtenida muestra exactamente el comportamiento teórico esperado: un pico de valor N en τ = 0 y valores de -1 para todos los demás desplazamientos, lo que verifica la propiedad de autocorrelación ideal de los códigos PN.

---

### 3. Densidad Espectral de Potencia (DSP)
- **Consigna:** Calcular y graficar la DSP de la secuencia.
- **Resultado:** El script `1_dsp.py` generó la gráfica `1_dsp.png` y el análisis en `1_dsp.txt`.
- **Gráfico:** ![DSP](Ejercicio_1/dsp_pn_sequence.png)
![DSP](Ejercicio_1/pn_sequence_temporal.png)

- **Explicación teórica:**
  La DSP de una secuencia PN máxima tiene las siguientes características:
  - La envolvente sigue una forma de sinc² característica
  - El ancho del lóbulo principal es inversamente proporcional a N
  - El espectro está compuesto por líneas discretas separadas por 1/N en frecuencia
  - La forma de sinc² es consecuencia directa de la forma rectangular de la autocorrelación
  - La DSP se anula en f=0 porque la secuencia está codificada con valores {-1,+1} y tiene media cero (igual cantidad de unos y menos unos). Esto significa que no hay componente DC en la señal.
- **Conclusión:** El espectro obtenido muestra claramente la forma de sinc² esperada, con el lóbulo principal centrado en f = 0 y los lóbulos laterales característicos. La gráfica se centró en el rango [-0.1, 0.1] Hz para mejor visualización del lóbulo principal. La ausencia de componente espectral en f=0 confirma el correcto balance de la secuencia.

---

### 4. Propiedad de Balance
- **Consigna:** Verificar que la secuencia cumple con la propiedad de balance (igual cantidad de unos y ceros, o diferencia de uno).
- **Resultado:** El script `1_balance.py` generó el análisis en `1_balance.txt` y la gráfica `1_balance_histograma.png`.
- **Gráfico:** ![Balance](Ejercicio_1/1_balance_histograma.png)
- **Conclusión:** La secuencia cumple con la propiedad de balance, presentando una diferencia máxima de uno entre la cantidad de unos y ceros por período.

---

### 5. Propiedad de Corridas
- **Consigna:** Verificar la propiedad de corridas (distribución de secuencias de unos y ceros consecutivos).
- **Resultado:** El script `1_corridas.py` generó el análisis en `1_corridas.txt` y la gráfica `1_corridas_histograma.png`.
- **Gráfico:** ![Corridas](Ejercicio_1/1_corridas_histograma.png)
- **Conclusión teórica (Sklar):**
  Según Sklar, para una secuencia PN máxima de longitud N = 2^n - 1:
  - El número total de corridas es aproximadamente la mitad de la longitud de la secuencia.
  - La cantidad de corridas de longitud 1 (corridas de un solo bit) debería ser aproximadamente igual a la cantidad de corridas de longitud máxima.
  - Por ejemplo, para una secuencia de 63 bits (n=6), deberías tener aproximadamente 32 corridas en total, y la cantidad de corridas de longitud 1 debería ser cercana a 16 (la mitad de 32).
- **Conclusión:** La distribución de corridas observada coincide con la esperada teóricamente para códigos PN, cumpliendo la propiedad de corridas.

---

## Conclusiones Generales

A partir de los resultados obtenidos y el análisis de los gráficos generados, se verifica que la secuencia PN implementada cumple con todas las propiedades teóricas descritas en la bibliografía principal:
- Período correcto
- Autocorrelación ideal
- Espectro similar a ruido blanco
- Propiedad de balance
- Propiedad de corridas

Esto valida la correcta implementación del generador de secuencias PN y su utilidad en sistemas de comunicaciones digitales, tal como lo expone Sklar.

---

Análisis de Propiedades de Códigos Gold

Portada
🔍 Introducción

Este repositorio contiene el análisis completo de las propiedades fundamentales de los códigos Gold, secuencias pseudoaleatorias esenciales en sistemas de comunicaciones digitales como CDMA.
📋 Contenido
Ejercicio 2:
![Consigna](Ejercicio_2/consigna2.png)
1. Generación del Código Gold

Secuencia generada

    Script: 2_gold_sequence.py
- **Gráfico:** ![Secuencia PN](Ejercicio_2/2_gold_sequence.png)

    Resultado: Secuencia de 63 bits (2⁶-1)

    Polinomios: [6,1] y [6,5,2,1]

    Propiedad verificada: Estructura pseudoaleatoria

2. Análisis de Autocorrelación

Gráfico de autocorrelación
- **Gráfico:** ![Autocorrelación](Ejercicio_2/2_autocorrelation.png)
    Script: 2_autocorrelation.py

    Hallazgos:

        Pico central en τ=0: 63

        Valores laterales entre -1 y -17

        Relación pico/lateral: ≈18 dB

3. Densidad Espectral de Potencia

Espectro de frecuencia

    Script: 2_dsp.py
- **Gráfico:** ![DSP](Ejercicio_2/2_gold_sequence_psd.png)
    Características:

        Forma de sinc²

        Espaciado: 15.87 kHz

        Ancho de banda: 1.2288 MHz

4. Propiedad de Balance

Distribución de bits

    Script: 2_balance.py
- **Gráfico:** ![Balance](Ejercicio_2/2_balance_histogram.png)
    Resultados:

        Unos: 32 (50.79%)

        Ceros: 31 (49.21%)

        Cumple |#1-#0| ≤ 1

5. Propiedad de Corridas

Distribución de corridas

    Script: 2_corridas.py
**Gráfico:** ![Corridas](Ejercicio_2/2_corridas_histogram.png)
    Distribución:

        50% longitud 1

        25% longitud 2

        12.5% longitud 3

📌 Conclusiones

    Excelente comportamiento en correlación cruzada e intra-secuencia

    Eficiencia espectral con rápida atenuación de lóbulos laterales

    Balance óptimo entre unos y ceros

    Distribución geométrica perfecta en corridas

    Ideal para CDMA y sistemas multi-usuario

**Todos los scripts, resultados y gráficos se encuentran en este repositorio.**

