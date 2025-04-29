# Informe: Propiedades de los Códigos PN

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
- **Gráfico:** ![Secuencia PN](1_pn_sequence.png)
- **Explicación:** En los códigos PN, el período es igual al largo de la secuencia generada porque esta es una propiedad fundamental de los códigos PN: un LFSR de longitud n produce una secuencia máxima de período $2^n-1$, y la secuencia se repite exactamente después de ese número de bits.
- **Conclusión:** El período coincide con el valor teórico esperado para un LFSR de la longitud utilizada, verificando la propiedad de periodicidad de los códigos PN.

---

### 2. Autocorrelación
- **Consigna:** Graficar la autocorrelación de la secuencia para 3 períodos completos y extraer conclusiones.
- **Resultado:** El script `1_autocorrelacion.py` generó la gráfica `1_autocorrelacion.png` y el análisis en `1_autocorrelacion.txt`.
- **Gráfico:** ![Autocorrelación](1_autocorrelacion.png)
- **Conclusión:** Se observa un pico principal y valores bajos fuera de fase, cumpliendo la propiedad de autocorrelación ideal de los códigos PN, como describe Sklar.

---

### 3. Densidad Espectral de Potencia (DSP)
- **Consigna:** Calcular y graficar la DSP de la secuencia.
- **Resultado:** El script `1_dsp.py` generó la gráfica `1_dsp.png` y el análisis en `1_dsp.txt`.
- **Gráfico:** ![DSP](1_dsp.png)
- **Conclusión:** El espectro obtenido es relativamente plano, confirmando la apariencia de ruido blanco de la secuencia PN, en línea con la teoría.

---

### 4. Propiedad de Balance
- **Consigna:** Verificar que la secuencia cumple con la propiedad de balance (igual cantidad de unos y ceros, o diferencia de uno).
- **Resultado:** El script `1_balance.py` generó el análisis en `1_balance.txt` y la gráfica `1_balance_histograma.png`.
- **Gráfico:** ![Balance](1_balance_histograma.png)
- **Conclusión:** La secuencia cumple con la propiedad de balance, presentando una diferencia máxima de uno entre la cantidad de unos y ceros por período.

---

### 5. Propiedad de Corridas
- **Consigna:** Verificar la propiedad de corridas (distribución de secuencias de unos y ceros consecutivos).
- **Resultado:** El script `1_corridas.py` generó el análisis en `1_corridas.txt` y la gráfica `1_corridas_histograma.png`.
- **Gráfico:** ![Corridas](1_corridas_histograma.png)
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

**Todos los scripts, resultados y gráficos se encuentran en este repositorio.**