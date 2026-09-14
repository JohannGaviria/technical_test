# Evaluación — Procesador de Balance de Cuenta

## Concepto de Solución de Referencia

La solución itera a través de las operaciones secuencialmente, manteniendo el saldo actual y un máximo acumulado. Para cada operación, valida las reglas de negocio, aplica el cambio de saldo (o rechaza la operación) y actualiza las estadísticas.

### Lógica de Procesamiento

1. Inicializar `balance = initial_balance`, `max_balance = initial_balance`, `fees = 0.0` y contadores de operaciones en cero.
2. Para cada operación:
   - **deposit**: sumar `amount` al saldo, incrementar contador de depósitos.
   - **withdraw**: si `balance - amount >= 0`, restar `amount` del saldo, incrementar contador de retiros; de lo contrario, omitir.
   - **transfer**: calcular comisión si `amount > 1000` (`amount * 0.015`, redondeado a 2 decimales). Si `balance - amount - fee >= 0`, aplicar la deducción, agregar comisión al total, incrementar contador de transferencias; de lo contrario, omitir.
   - Después de cada operación exitosa, actualizar `max_balance = max(max_balance, balance)`.
3. Devolver el diccionario de resumen.

### Cálculo de Comisión

- La comisión se aplica solo cuando `amount > 1000`.
- Comisión = `round(amount * 0.015, 2)`.
- Total deducido = `amount + fee`.

### Enfoques Válidos

- Una iteración de pasada simple O(n) es el enfoque esperado.
- Un enfoque voraz (procesar operaciones en orden) es correcto y suficiente.
- Rastrear max_balance requiere actualizar después de cada operación exitosa.

## Complejidad Esperada

- **Tiempo**: O(n) donde n es el número de operaciones.
- **Espacio**: O(1) espacio auxiliar (excluyendo la entrada).

## Reglas de Negocio Importantes

1. Las operaciones fallidas no deben modificar el saldo.
2. Las operaciones fallidas no deben contarse.
3. Las transferencias fallidas no deben cobrar comisión.
4. La comisión de transferencia se aplica solo cuando amount > 1000 (no >=).
5. La comisión se redondea a 2 decimales.
6. max_balance incluye el saldo inicial.
7. Las operaciones se procesan secuencialmente en el orden dado.

## Errores Comunes

- Contar operaciones fallidas en el resumen.
- Cobrar comisiones en transferencias fallidas.
- No actualizar max_balance después de cada operación exitosa.
- Usar el umbral de comisión incorrecto (1000 vs 1000.01).
- Redondear comisiones incorrectamente.
- No incluir el saldo inicial en el cálculo de max_balance.

## Lógica de los Tests Ocultos

Los tests ocultos se enfocan en:
- Condiciones de frontera (saldo exactamente en cero, monto exactamente en el umbral de comisión).
- Transferencias fallidas sin cobro de comisión.
- Lista vacía de operaciones.
- Saldo máximo ocurriendo a mitad de la secuencia.
- Múltiples fallos consecutivos.
- Montos grandes con cálculos de comisión precisos.
