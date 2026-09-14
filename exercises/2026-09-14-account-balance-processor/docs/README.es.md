# Procesador de Balance de Cuenta

## Contexto

Una startup de fintech está construyendo un backend bancario simple. Un componente central procesa una secuencia de operaciones sobre una cuenta de cliente y produce un resumen final. La empresa necesita que este componente aplique correctamente las reglas de negocio, calcule comisiones y rastree estadísticas de la cuenta.

## Objetivo

Implementar una función que procese una lista de operaciones bancarias sobre una cuenta y devuelva un resumen del estado final.

## Problema

Se le proporcionan:

* Un **saldo inicial** (un número no negativo).
* Una **lista de operaciones**, donde cada operación es un diccionario con:

| Campo    | Tipo   | Descripción                                                                 |
| -------- | ------ | --------------------------------------------------------------------------- |
| `type`   | `str`  | Uno de: `"deposit"`, `"withdraw"`, `"transfer"`                            |
| `amount` | `float`| Un número positivo que representa el monto                                  |
| `to`     | `str`  | *(Opcional)* Nombre del destinatario. Requerido solo para `"transfer"`.     |

Su función debe procesar cada operación **en orden** y aplicar las siguientes reglas:

### Depósito (`deposit`)

* Incrementa el saldo de la cuenta por `amount`.
* Siempre se ejecuta correctamente.

### Retiro (`withdraw`)

* Reduce el saldo de la cuenta por `amount`.
* **Falla** si el saldo resultante sería negativo.
* Un retiro fallido **no** modifica el saldo y **no** se cuenta.

### Transferencia (`transfer`)

* Una transferencia a otra cuenta.
* Se cobra una **comisión** sobre el monto transferido si excede **1000**.
* La comisión es el **1.5%** del monto transferido.
* El total deducido del saldo es `amount + fee`.
* **Falla** si el saldo resultante sería negativo tras deducir tanto el monto como la comisión.
* Una transferencia fallida **no** modifica el saldo, **no** cobra comisión y **no** se cuenta.

### Redondeo de Comisiones

Las comisiones deben redondearse a **2 decimales** usando redondeo estándar (redondear a la mitad hacia arriba). Por ejemplo, una comisión de `15.005` se convierte en `15.01`.

## Salida

La función debe devolver un diccionario con las siguientes claves:

```python
{
    "balance": float,        # Saldo final de la cuenta
    "operations": {          # Conteo de operaciones exitosas por tipo
        "deposit": int,
        "withdraw": int,
        "transfer": int
    },
    "fees": float,           # Total de comisiones cobradas en todas las transferencias
    "max_balance": float     # Saldo más alto alcanzado en cualquier momento durante el procesamiento
}
```

## Restricciones

* `0 <= initial_balance <= 100,000`
* `0 < amount <= 100,000`
* `0 <= número de operaciones <= 100,000`
* Todos los valores monetarios son floats con hasta 2 decimales.

## Ejemplos

### Ejemplo 1: Operaciones Básicas

```python
initial_balance = 1000
operations = [
    {"type": "deposit", "amount": 500},
    {"type": "withdraw", "amount": 200},
    {"type": "transfer", "amount": 300, "to": "alice"},
]

result = process_operations(initial_balance, operations)
# balance = 1000 + 500 - 200 - 300 = 1000.00
# Sin comisión (300 <= 1000)
# max_balance = 1500 (después del depósito)
# operations = {"deposit": 1, "withdraw": 1, "transfer": 1}
# fees = 0.00
```

### Ejemplo 2: Transferencia con Comisión

```python
initial_balance = 5000
operations = [
    {"type": "transfer", "amount": 2000, "to": "bob"},
]

result = process_operations(initial_balance, operations)
# Comisión = 2000 * 0.015 = 30.00
# balance = 5000 - 2000 - 30 = 2970.00
# max_balance = 5000
# operations = {"deposit": 0, "withdraw": 0, "transfer": 1}
# fees = 30.00
```

### Ejemplo 3: Retiro Fallido

```python
initial_balance = 100
operations = [
    {"type": "withdraw", "amount": 500},
]

result = process_operations(initial_balance, operations)
# El retiro falla (100 - 500 = -400 < 0)
# balance = 100 (sin cambios)
# max_balance = 100
# operations = {"deposit": 0, "withdraw": 0, "transfer": 0}
# fees = 0.00
```

## Casos Límite

* Lista vacía de operaciones — el resultado debe reflejar solo el saldo inicial con todos los conteos en cero.
* Operaciones que llevan el saldo exactamente a cero son válidas.
* Una transferencia de exactamente 1000 no genera comisión; una de 1000.01 sí.
* El `max_balance` es el saldo más alto observado **después** de cada operación exitosa, incluyendo el saldo inicial.
* Múltiples operaciones en secuencia donde el saldo máximo ocurre a mitad del camino.

## Interfaz Esperada

```python
def process_operations(initial_balance: float, operations: list) -> dict:
    """Procesa operaciones bancarias y devuelve el resumen de la cuenta."""
    raise NotImplementedError
```
