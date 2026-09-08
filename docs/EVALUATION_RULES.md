# Exercise Evaluation Rules

## Purpose

This document defines how candidate solutions must be evaluated.

The objective is to simulate a realistic technical interview evaluation for a Junior Backend Developer or Software Engineering Intern.

Evaluation must focus on the candidate's actual implementation.

Do not replace the candidate's solution with a better implementation and evaluate the replacement.

---

# 1. Evaluation Scope

The evaluator must assess:

* Functional correctness
* Business-rule correctness
* Edge-case handling
* Python fundamentals
* Algorithms and data structures
* Computational complexity
* Code quality
* Maintainability
* Completeness

The evaluator must consider the candidate's expected level.

Do not apply senior-level expectations to a Junior/Intern candidate.

---

# 2. Files to Inspect

Before evaluating, inspect:

1. Exercise `README.md`
2. Exercise `docs/README.es.md`
3. `solution/solution.py`
4. `tests/test_solution.py`
5. `tests/test_solution_hidden.py`
6. `EVALUATION.md`
7. `docs/EVALUATION.es.md`

The evaluator should use all relevant information available in the exercise.

If the exercise contains additional relevant documentation, inspect it as necessary.

---

# 3. Candidate Implementation

Evaluate the implementation that actually exists in:

```text
solution/solution.py
```

Do not:

* Rewrite the candidate's solution
* Implement missing functionality on their behalf
* Modify the candidate code to make tests pass
* Modify the exercise requirements
* Modify public or hidden tests to accommodate the candidate

The purpose is to evaluate the submitted implementation as-is.

---

# 4. Public Contract vs. Internal Implementation

The exercise README and starter code define the **public contract** that the candidate must satisfy.

The candidate is free to determine the internal implementation.

A valid solution may use a different:

* Internal structure
* Data model
* Class structure
* Set of helper functions
* Algorithm
* Data structure
* Validation strategy
* Error-handling strategy
* Processing strategy

than the evaluator or exercise author originally expected.

The evaluator must evaluate whether the implementation satisfies the documented behavior, not whether it matches an imagined reference implementation.

### Tests Must Follow the Public Contract

Tests must interact only with the documented public interface.

Tests must not require:

* Specific helper functions
* Specific class names that are not part of the public contract
* Specific constants
* Specific enums
* Specific dataclasses
* Specific internal variables
* Specific internal data structures
* Specific algorithm implementations
* Specific processing steps
* Specific module organization

If two implementations produce the same documented behavior through the public interface, both should be considered valid regardless of their internal design.

### Reference Implementations

A reference implementation may exist to help the evaluator understand expected behavior.

It must not become an implicit implementation contract.

The candidate must not be penalized for producing a correct solution that differs from the reference implementation.

---

# 5. Test Execution

Run the available pytest suite whenever possible.

Use:

```bash
pytest
```

If useful, run:

```bash
pytest -v
```

The evaluator should determine:

* Number of passing tests
* Number of failing tests
* Whether failures are related to correctness
* Whether failures are related to edge cases
* Whether failures indicate incomplete implementation
* Whether hidden tests reveal missing requirements

Do not treat the number of passing tests as the only evaluation criterion.

A candidate may pass many tests while still having significant design, complexity, or correctness problems.

Likewise, a test failure should be investigated before concluding that the candidate implementation is incorrect.

If a test depends on an internal implementation detail that is not part of the public contract, the test itself should not be used as evidence against the candidate.

---

# 6. Functional Correctness

Functional correctness is the most important criterion.

Verify that the implementation:

* Produces the expected output.
* Handles normal inputs correctly.
* Implements all explicit requirements.
* Implements all relevant business rules.
* Produces deterministic results when required.
* Handles invalid input correctly when specified.
* Does not omit required conditions.

Pay particular attention to interactions between requirements.

For example, if an exercise contains:

* Eligibility rules
* Maximum limits
* Validation
* Prioritization

verify both individual rules and combinations of rules.

A candidate does not need to follow the evaluator's preferred implementation strategy if the resulting behavior is correct.

---

# 7. Business Logic Evaluation

When an exercise contains business rules, evaluate each rule independently and in combination.

Check for:

* Missing conditions
* Incorrect condition ordering
* Incorrect state transitions
* Incorrect limits
* Incorrect calculations
* Incorrect prioritization
* Invalid combinations being accepted
* Valid combinations being rejected

A solution that handles the algorithm correctly but violates an important business rule must lose functional-correctness points.

The evaluation should focus on the observable business behavior, not on how the candidate internally represents that behavior.

---

# 8. Edge Cases

Evaluate whether the candidate considered relevant edge cases.

Possible cases include:

* Empty input
* One element
* Duplicate values
* Zero
* Negative values
* Minimum values
* Maximum values
* Boundary conditions
* Missing values
* Repeated operations
* Conflicting business rules
* Invalid combinations

Only apply cases that make sense for the exercise.

Do not penalize candidates for unsupported input that the exercise explicitly excludes.

When an edge case is not clearly defined by the exercise, do not invent a new requirement during evaluation.

---

# 9. Algorithms and Data Structures

Evaluate whether the candidate selected an appropriate approach.

Consider:

* Correct data structure choice
* Appropriate algorithm
* Avoidance of unnecessary work
* Readability of the approach
* Whether the implementation matches the problem constraints

Examples of reasonable choices may include:

* Dictionary for frequency counting
* Set for membership checks
* Sorting when ordering is required
* Stack for LIFO behavior
* Queue for FIFO behavior
* Two pointers for suitable sequence problems
* Sliding window for suitable range problems

Do not require a specific algorithm if multiple approaches are valid and satisfy the constraints.

The candidate should receive credit for any algorithmically valid approach that meets the stated requirements and constraints.

---

# 10. Computational Complexity

Evaluate both:

* Time complexity
* Space complexity

Determine whether the implementation is appropriate for the stated constraints.

Examples:

```text
O(n)
O(n log n)
O(n²)
```

If the constraints allow O(n²), do not penalize a correct O(n²) implementation merely because O(n) exists.

If the constraints make O(n²) impractical, the candidate should receive a meaningful complexity penalty.

Complexity must be evaluated in context.

Do not penalize a candidate for using a different algorithm from the reference implementation if its complexity is equally appropriate or better.

---

# 11. Python Usage

Evaluate whether the candidate demonstrates appropriate Python fundamentals.

Consider:

* Correct type usage
* Functions
* Classes when appropriate
* Lists
* Dictionaries
* Sets
* Iteration
* Comprehensions
* Built-in functions
* Exception handling when relevant
* Standard library usage
* Readability
* Pythonic conventions

Do not reward obscure Python tricks.

The goal is maintainable Python rather than clever Python.

Do not require type annotations, classes, dataclasses, or other language features unless they are appropriate to the exercise or part of its public contract.

---

# 12. Code Quality

Evaluate:

* Naming
* Readability
* Structure
* Function size
* Duplication
* Comments
* Documentation
* Separation of concerns where appropriate
* Simplicity
* Maintainability

Avoid requiring unnecessary architecture.

A Junior/Intern exercise should normally be solvable with a small number of functions or a simple class.

Do not penalize a candidate for not introducing:

* Hexagonal Architecture
* Clean Architecture
* DDD
* Dependency Injection frameworks
* Complex design patterns

unless the exercise explicitly requires them.

Likewise, do not reward unnecessary abstraction merely because it appears architecturally sophisticated.

The preferred solution is the simplest maintainable solution appropriate for the problem.

---

# 13. Incomplete Implementations

Identify incomplete implementations such as:

* `pass`
* `TODO` left unresolved
* `NotImplementedError`
* Hardcoded outputs
* Partial business rules
* Handling only examples
* Handling only happy paths
* Ignoring constraints

An implementation that only works for the public examples should not receive a passing score.

---

# 14. Public vs Hidden Tests

Public tests are visible to the candidate.

Hidden tests are evaluator-only.

Use hidden tests to identify:

* Missing requirements
* Boundary errors
* Incomplete logic
* Incorrect assumptions
* Complexity problems
* Interaction between rules

Do not reveal the complete hidden test suite in the evaluation report.

It is acceptable to explain the category of hidden cases that failed.

For example:

> The implementation fails boundary conditions involving the maximum allowed number of active reservations.

Do not provide unnecessary details that expose the exact hidden test implementation.

### Test Independence

Public and hidden tests must remain independent of the candidate's internal implementation.

Tests should verify:

* Inputs
* Outputs
* Observable state
* Documented side effects, when applicable

Tests should not verify implementation details unless those details are explicitly part of the public contract.

If a test fails because the candidate chose a different valid internal design, the test must not be treated as evidence of a candidate failure.

---

# 15. Scoring

Use a 100-point scale.

Default distribution:

| Category               |  Points |
| ---------------------- | ------: |
| Functional correctness |      50 |
| Edge cases             |      15 |
| Code quality           |      15 |
| Complexity             |      10 |
| Python usage           |      10 |
| **Total**              | **100** |

Adjust category weighting only when the exercise strongly justifies it.

The final score must always be normalized to 100.

---

# 16. Grade

Convert the final score to a grade from 1.0 to 10.0.

Use:

```text
Grade = Score / 10
```

Examples:

| Score | Grade |
| ----: | ----: |
|   100 |  10.0 |
|    90 |   9.0 |
|    80 |   8.0 |
|    70 |   7.0 |
|    60 |   6.0 |
|    50 |   5.0 |

Use one decimal place.

---

# 17. Evaluation Status

Use the following statuses:

### Completed

Use when:

* The implementation satisfies the requirements.
* Important edge cases are handled.
* The solution is appropriate for the candidate level.
* No significant correctness issue remains.

Typical score:

```text
7.0–10.0
```

---

### Needs Review

Use when:

* The main idea is correct.
* The solution has meaningful issues.
* Some edge cases fail.
* Some requirements are incomplete.
* Complexity could be improved.
* Code quality needs improvement.

Typical score:

```text
6.0–6.9
```

---

### Failed

Use when:

* The core solution is incorrect.
* Important business rules are missing.
* The implementation is substantially incomplete.
* The solution cannot solve the exercise reliably.

Typical score:

```text
1.0–5.9
```

---

# 18. Evaluation Report

After evaluating a solution, generate:

```text
SOLUTION_EVALUATION.md
SOLUTION_EVALUATION.es.md
```

Both files must contain the same evaluation information in their respective languages.

The report should include:

1. Exercise
2. Candidate level
3. Final score
4. Grade
5. Status
6. Test results
7. Functional correctness
8. Edge cases
9. Algorithm and data structures
10. Complexity
11. Python usage
12. Code quality
13. Strengths
14. Problems found
15. Interviewer feedback
16. Recommendations

---

# 19. Strengths

Identify concrete strengths.

Examples:

* Correct use of dictionaries for efficient lookups.
* Clear separation of validation and processing.
* Good handling of boundary conditions.
* Appropriate O(n) complexity.
* Readable naming and structure.
* Good use of Python standard-library functionality.

Do not provide generic praise without evidence.

---

# 20. Problems Found

Describe concrete issues.

For each important problem, explain:

1. What is wrong.
2. Why it matters.
3. Which requirement or principle it affects.
4. How severe it is.

Prioritize correctness problems over style issues.

Do not describe a difference from the reference implementation as a problem unless that difference causes incorrect behavior, inappropriate complexity, or a meaningful quality issue.

---

# 21. Recommendations

Classify recommendations as:

* High
* Medium
* Low

### High

Problems that affect:

* Correctness
* Business rules
* Important edge cases
* Complexity under realistic constraints

### Medium

Problems that affect:

* Maintainability
* Structure
* Readability
* Python usage

### Low

Minor improvements such as:

* Naming refinements
* Small stylistic changes
* Optional documentation improvements

---

# 22. Interviewer Feedback

The final feedback should answer:

> Would this candidate be ready for a Junior Backend Developer / Software Engineering Intern role based on this exercise?

Consider:

* Problem-solving ability
* Independence
* Python fundamentals
* Ability to reason about edge cases
* Understanding of business rules
* Code quality
* Ability to choose reasonable data structures
* Complexity awareness

Do not make hiring decisions based exclusively on this exercise.

The feedback should describe the technical evidence observed.

---

# 23. Exercise Tracking

The root `README.md` contains the official exercise tracking table.

After every evaluation, the evaluator must update the existing exercise entry.

The registry must remain synchronized with the evaluation result.

## Required Updates

At minimum, update:

* Score
* Grade
* Status

When useful, also update:

* Evaluation date
* Tests passed
* Notes
* Main issue
* Improvement status

Example:

```markdown
| 2026-09-08 | [Order Discount Validator](exercises/2026-09-08-order-discount-validator/) | Business Logic | Medium | 45 min | 84 | 8.4 | Completed |
```

---

# 24. Never Duplicate Registry Entries

Before updating the root README:

1. Locate the exercise directory.
2. Search the Exercises table for the exercise.
3. Identify the existing row.
4. Update that row.

Never add a second row for the same exercise.

If the exercise was previously evaluated, overwrite the previous evaluation data with the latest result.

---

# 25. Re-evaluation

When a solution is re-evaluated:

* Use the latest implementation.
* Run the relevant tests again.
* Recalculate the score.
* Recalculate the grade.
* Update the status.
* Update the existing README row.

Do not create another exercise entry.

The registry represents exercises, not individual evaluation attempts.

---

# 26. Candidate Improvements

If the candidate improves their solution after feedback, evaluate the new implementation again.

Compare:

* Previous score
* New score
* Fixed issues
* Remaining issues
* Complexity improvements
* Edge-case improvements

The README registry should contain the latest meaningful status.

Historical details may be recorded in the evaluation report when useful, but the registry should remain concise.

---

# 27. Final Evaluation Checklist

Before finishing an evaluation, verify:

* [ ] Candidate implementation was evaluated as-is.
* [ ] Exercise requirements were reviewed.
* [ ] Public contract was identified.
* [ ] Evaluation does not depend on the reference implementation's internal structure.
* [ ] Public tests were executed.
* [ ] Hidden tests were considered.
* [ ] Tests used only the documented public interface.
* [ ] Functional correctness was evaluated.
* [ ] Business rules were evaluated.
* [ ] Edge cases were evaluated.
* [ ] Algorithm and data structures were evaluated.
* [ ] Time complexity was evaluated.
* [ ] Space complexity was evaluated.
* [ ] Python usage was evaluated.
* [ ] Code quality was evaluated.
* [ ] Score totals 100 points.
* [ ] Grade is correctly calculated.
* [ ] Status is correct.
* [ ] English evaluation exists.
* [ ] Spanish evaluation exists.
* [ ] Root README exercise row was updated.
* [ ] No duplicate registry row was created.
