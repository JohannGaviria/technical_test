# Account Balance Processor

## Context

A fintech startup is building a simple banking backend. One core component processes a sequence of operations on a customer account and produces a final summary. The company needs this component to correctly enforce business rules, calculate fees, and track account statistics.

## Objective

Implement a function that processes a list of banking operations on an account and returns a summary of the final state.

## Problem

You are given:

* An **initial balance** (a non-negative number).
* A **list of operations**, where each operation is a dictionary with:

| Field    | Type   | Description                                                                 |
| -------- | ------ | --------------------------------------------------------------------------- |
| `type`   | `str`  | One of: `"deposit"`, `"withdraw"`, `"transfer"`                            |
| `amount` | `float`| A positive number representing the amount                                   |
| `to`     | `str`  | *(Optional)* Recipient name. Required only for `"transfer"` operations.     |

Your function must process each operation **in order** and apply the following rules:

### Deposit

* Increases the account balance by `amount`.
* Always succeeds.

### Withdraw

* Decreases the account balance by `amount`.
* **Fails** if the resulting balance would be negative.
* A failed withdrawal does **not** modify the balance and is **not** counted.

### Transfer

* A transfer to another account.
* A **fee** is charged on the transfer amount if it exceeds **1000**.
* The fee is **1.5%** of the transfer amount.
* The total deducted from the balance is `amount + fee`.
* **Fails** if the resulting balance would be negative after deducting both the amount and the fee.
* A failed transfer does **not** modify the balance, does **not** charge a fee, and is **not** counted.

### Fee Rounding

Fees must be rounded to **2 decimal places** using standard rounding (round half up). For example, a fee of `15.005` becomes `15.01`.

## Output

The function must return a dictionary with the following keys:

```python
{
    "balance": float,        # Final account balance
    "operations": {          # Count of successful operations by type
        "deposit": int,
        "withdraw": int,
        "transfer": int
    },
    "fees": float,           # Total fees charged across all transfers
    "max_balance": float     # Highest balance reached at any point during processing
}
```

## Constraints

* `0 <= initial_balance <= 100,000`
* `0 < amount <= 100,000`
* `0 <= number of operations <= 100,000`
* All monetary values are floats with up to 2 decimal places.

## Examples

### Example 1: Basic Operations

```python
initial_balance = 1000
operations = [
    {"type": "deposit", "amount": 500},
    {"type": "withdraw", "amount": 200},
    {"type": "transfer", "amount": 300, "to": "alice"},
]

result = process_operations(initial_balance, operations)
# balance = 1000 + 500 - 200 - 300 = 1000.00
# No fee (300 <= 1000)
# max_balance = 1500 (after deposit)
# operations = {"deposit": 1, "withdraw": 1, "transfer": 1}
# fees = 0.00
```

### Example 2: Transfer with Fee

```python
initial_balance = 5000
operations = [
    {"type": "transfer", "amount": 2000, "to": "bob"},
]

result = process_operations(initial_balance, operations)
# Fee = 2000 * 0.015 = 30.00
# balance = 5000 - 2000 - 30 = 2970.00
# max_balance = 5000
# operations = {"deposit": 0, "withdraw": 0, "transfer": 1}
# fees = 30.00
```

### Example 3: Failed Withdrawal

```python
initial_balance = 100
operations = [
    {"type": "withdraw", "amount": 500},
]

result = process_operations(initial_balance, operations)
# Withdrawal fails (100 - 500 = -400 < 0)
# balance = 100 (unchanged)
# max_balance = 100
# operations = {"deposit": 0, "withdraw": 0, "transfer": 0}
# fees = 0.00
```

## Edge Cases

* Empty operations list — the result should reflect only the initial balance with all counts at zero.
* Operations that bring the balance exactly to zero are valid.
* A transfer of exactly 1000 does not incur a fee; a transfer of 1000.01 does.
* The `max_balance` is the highest balance observed **after** each successful operation, including the initial balance.
* Multiple operations in sequence where the max balance occurs mid-way.

## Expected Interface

```python
def process_operations(initial_balance: float, operations: list) -> dict:
    """Process banking operations and return the account summary."""
    raise NotImplementedError
```
