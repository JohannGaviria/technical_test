# Evaluation — Account Balance Processor

## Reference Solution Concept

The solution iterates through operations sequentially, maintaining the current balance and a running maximum. For each operation, it validates the business rules, applies the balance change (or rejects the operation), and updates statistics.

### Processing Logic

1. Initialize `balance = initial_balance`, `max_balance = initial_balance`, `fees = 0.0`, and operation counters to zero.
2. For each operation:
   - **deposit**: add `amount` to balance, increment deposit counter.
   - **withdraw**: if `balance - amount >= 0`, subtract `amount` from balance, increment withdraw counter; else skip.
   - **transfer**: calculate fee if `amount > 1000` (`amount * 0.015`, rounded to 2 decimals). If `balance - amount - fee >= 0`, apply deduction, add fee to total fees, increment transfer counter; else skip.
   - After each successful operation, update `max_balance = max(max_balance, balance)`.
3. Return the summary dictionary.

### Fee Calculation

- Fee applies only when `amount > 1000`.
- Fee = `round(amount * 0.015, 2)`.
- Total deducted = `amount + fee`.

### Valid Approaches

- Single-pass O(n) iteration is the expected approach.
- A greedy approach (process operations in order) is correct and sufficient.
- Tracking max_balance requires updating after each successful operation.

## Expected Complexity

- **Time**: O(n) where n is the number of operations.
- **Space**: O(1) auxiliary space (excluding input).

## Important Business Rules

1. Failed operations must not modify the balance.
2. Failed operations must not be counted.
3. Failed transfers must not charge a fee.
4. Transfer fee applies only when amount > 1000 (not >=).
5. Fee is rounded to 2 decimal places.
6. max_balance includes the initial balance.
7. Operations are processed sequentially in the order given.

## Common Mistakes

- Counting failed operations in the summary.
- Charging fees on failed transfers.
- Not updating max_balance after every successful operation.
- Using the wrong fee threshold (1000 vs 1000.01 boundary).
- Incorrectly rounding fees.
- Not including initial balance in max_balance calculation.

## Hidden Test Rationale

Hidden tests focus on:
- Boundary conditions (balance exactly at zero, amount exactly at fee threshold).
- Failed transfers not charging fees.
- Empty operations list.
- Max balance occurring mid-sequence.
- Multiple consecutive failures.
- Large amounts with precise fee calculations.
