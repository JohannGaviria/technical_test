# Exercise Generation Rules

## Purpose

This document defines the rules for generating technical programming exercises for Junior Backend Developers and Software Engineering Interns.

Every generated exercise must be a realistic technical assessment that evaluates programming fundamentals, problem solving, business logic, and code quality.

---

# 1. Exercise Scope

## Exactly One Exercise

Every generation request must produce **exactly one exercise**.

One execution must never generate:

* Exercise 1 / Exercise 2 / Exercise 3
* Multiple independent problems
* Multiple unrelated functions to implement
* A collection of challenges
* A multi-question technical test
* Several exercises grouped together

The result must be one self-contained and coherent problem.

The exercise may combine several concepts when they belong naturally to the same problem.

For example, an inventory exercise may require:

* Filtering
* Validation
* Stock calculations
* Business rules
* Prioritization

That is still one exercise because all requirements belong to the same domain problem.

---

# 2. Candidate Profile

Exercises target:

* Junior Backend Developers
* Software Engineering Interns
* Junior Python Developers

Assume the candidate knows:

* Python fundamentals
* Functions
* Classes
* Lists
* Dictionaries
* Sets
* Tuples
* Loops
* Conditionals
* Exceptions
* Basic object-oriented programming
* Basic algorithms
* Basic data structures
* Basic complexity concepts

Do not assume knowledge of advanced frameworks or infrastructure.

---

# 3. Difficulty

Allowed difficulty levels:

* Easy
* Easy/Medium
* Medium

Do not generate:

* Hard
* Expert
* Competitive-programming-level problems

The exercise should challenge the candidate without requiring advanced mathematical or algorithmic knowledge.

---

# 4. Estimated Duration

The exercise must be realistically solvable within:

**30–60 minutes**

Suggested timeline:

| Time      | Candidate activity                          |
| --------- | ------------------------------------------- |
| 0–10 min  | Understand requirements and design approach |
| 10–40 min | Implement the solution                      |
| 40–60 min | Test, debug, and improve                    |

The main solution must fit this timeframe.

An optional optimization bonus may be included, but it must not be required to complete the main exercise.

---

# 5. Technology Requirements

Python is the required programming language.

Prefer the Python Standard Library.

Do not require:

* FastAPI
* Django
* Flask
* PostgreSQL
* MySQL
* MongoDB
* Redis
* Docker
* Kubernetes
* External APIs
* External services
* Cloud infrastructure
* Network access

The candidate should be able to solve the exercise locally with Python and pytest.

---

# 6. Problem Categories

Exercises should alternate naturally between different types of problems.

## Algorithmic and Logical Problems

Possible concepts include:

* Strings
* Lists
* Dictionaries
* Sets
* Sorting
* Searching
* Hash maps
* Two pointers
* Sliding window
* Stacks
* Queues
* Matrices
* Recursion
* Binary search
* Greedy strategies
* Frequency counting
* Data transformation
* Filtering
* Aggregation
* Basic complexity analysis

Do not force an algorithm simply because it is on this list.

The algorithm should naturally arise from the problem.

---

## Business Logic Problems

Possible domains include:

* Inventory
* Orders
* Reservations
* Loans
* Users
* Permissions
* Discounts
* Billing
* Resource allocation
* Eligibility rules
* State transitions
* Limits
* Transaction processing
* Prioritization
* Scheduling
* Resource management

Business rules should be explicit and meaningful.

---

## Combined Problems

The preferred exercises often combine:

**Business logic + algorithmic reasoning**

Example:

An order-processing problem may require the candidate to:

1. Validate an order.
2. Apply business rules.
3. Group products.
4. Calculate totals.
5. Prioritize items.
6. Return a deterministic result.

This remains one coherent exercise.

---

# 7. Problem Quality

Exercises should resemble realistic technical interview problems.

Avoid exercises that are:

* Artificially complicated
* Trivial
* Extremely verbose
* Dependent on obscure Python features
* Dependent on external systems
* Primarily framework configuration
* Primarily architecture design

The challenge should come from reasoning and implementation.

---

# 8. Avoid Trivial Exercises

Do not generate exercises whose primary challenge is:

* FizzBuzz
* Factorial
* Basic Fibonacci
* Simple sum
* Simple average
* Finding a minimum or maximum
* Basic palindrome checking
* Basic string reversal
* Basic counting with no additional reasoning

These may appear as small sub-operations inside a larger exercise, but they must not constitute the exercise itself.

---

# 9. Originality

Do not directly copy exercises from:

* LeetCode
* HackerRank
* CodeSignal
* Codility
* InterviewBit
* Other coding challenge platforms

Known algorithmic patterns are allowed.

The scenario, requirements, examples, and formulation should be original.

---

# 10. Constraints

Every exercise should include meaningful constraints.

Constraints should help the candidate reason about:

* Input size
* Performance
* Memory
* Boundary conditions
* Business limits

If an inefficient O(n²) solution could become problematic, the constraints should make that relevant.

Do not introduce artificial constraints solely to force a specific algorithm.

---

# 11. Expected Interface

The exercise must define a clear public interface.

The preferred interface is:

* One public function, or
* One public class when a class is genuinely the natural abstraction for the problem.

Use multiple public methods only when the problem genuinely requires them.

The public interface must include:

* Name
* Parameters
* Input representation
* Return type or return structure
* Expected behavior

The interface defines the **public contract**, not the internal implementation.

The exercise must not require a specific internal architecture unless that architecture is explicitly part of the exercise.

The candidate should be free to choose:

* Internal classes
* Dataclasses
* Helper functions
* Constants
* Enums
* Internal data structures
* Validation strategy
* Error-handling strategy
* Algorithm
* Processing strategy

as long as the documented public contract and requirements are satisfied.

---

# 12. Starter Solution

The starter solution must be generated directly under:

```text
solution/solution.py
```

The starter must provide the **minimum possible starting point** for the candidate.

Its purpose is to define:

> **Where should the candidate implement the solution?**

It must not define:

> **How should the candidate implement the solution?**

### Minimal Starter Philosophy

The starter should normally contain only:

* The public entry-point function, or
* The public entry-point class.

Type annotations may be included when necessary to make the public contract clear.

A short docstring may describe the general purpose of the entry point.

For example:

```python
def process_bookings(rooms: list, requests: list) -> dict:
    """Process booking requests and return the allocation report."""
    raise NotImplementedError
```

The exact signature must reflect the documented public interface.

### What the Starter Must Not Reveal

Do not predefine implementation decisions such as:

* Business-rule constants
* Error constants
* Error classes
* Enums
* Dataclasses
* Internal models
* Helper functions
* Helper signatures
* Internal data structures
* Predefined result structures
* Validation categories
* Processing stages
* Algorithm hints
* Suggested algorithms
* Implementation steps
* Detailed implementation comments

Do not decompose the problem into helper functions or classes before the candidate has done so.

Do not encode business rules into names, constants, types, or comments that reveal how the problem should be solved.

### Concise Docstrings

The starter docstring must describe only the general purpose of the entry point.

It should **not** restate the exercise specification.

Avoid docstrings that reveal:

* Business rules
* Edge cases
* Validation requirements
* Processing order
* Internal data structures
* Algorithmic approach
* Exact output decomposition
* Implementation steps

The candidate should obtain those details from the exercise README.

### Additional Types

Additional classes, types, dataclasses, enums, or constants may be included in the starter **only when they are genuinely required as part of the public interface**.

They must not be added merely for convenience or because they appear in a reference implementation.

### Starter Code Principle

The starter should satisfy the following principle:

> **README → tells the candidate what to do.**
> **Starter → tells the candidate where to do it.**
> **Candidate → decides how to do it.**
> **Tests → verify whether the behavior is correct.**

---

# 13. Documentation

Every exercise must contain:

```text
README.md
README.es.md
EVALUATION.md
EVALUATION.es.md
```

## README Files

`README.md` must be written in English.

`README.es.md` must be written in Spanish.

Both files must contain the same information.

Use natural and professional technical terminology rather than literal translations.

Required sections:

1. Context
2. Objective
3. Problem
4. Requirements
5. Input
6. Output
7. Constraints
8. Examples
9. Edge Cases
10. Expected Interface

The candidate-facing README must describe the complete behavior required from the solution.

It must not reveal the intended implementation.

---

# 14. Public Tests

Public tests must be placed in:

```text
tests/test_solution.py
```

They must use pytest.

Tests should validate observable behavior through the documented public interface.

Public tests should include:

* Main examples
* Normal cases
* Basic edge cases
* Important business rules
* Relevant invalid inputs

Tests should be understandable to the candidate.

The candidate is allowed to inspect public tests.

Public tests must not depend on:

* Specific helper functions
* Internal classes
* Internal constants
* Internal variables
* Specific dataclasses
* Specific enums
* Specific algorithms
* Internal module organization

unless those elements are explicitly part of the public contract.

---

# 15. Hidden Tests

Hidden tests must be placed in:

```text
tests/test_solution_hidden.py
```

They are evaluator-only.

They should detect incomplete or incorrect implementations.

Include relevant cases such as:

* Empty input
* Single-element input
* Duplicate values
* Zero
* Negative values when relevant
* Minimum boundaries
* Maximum boundaries
* Multiple interacting rules
* Invalid combinations
* Missing conditions
* Index-related errors
* Large inputs when complexity matters
* Common incomplete implementations

Do not make hidden tests arbitrary.

Every hidden test must correspond to a legitimate requirement or important edge case.

Hidden tests must use only the documented public interface.

They must not assume that the candidate reproduced the reference implementation.

---

# 16. Test Independence

Tests must import and interact with the candidate solution through its documented public interface.

For example:

```python
from solution.solution import solve
```

The exact import must match the public interface defined by the exercise.

Running:

```bash
pytest
```

must discover and execute the tests.

The initial starter implementation should cause relevant tests to fail because the candidate has not implemented the solution yet.

Tests must evaluate behavior rather than implementation details.

A valid candidate solution may use a different:

* Internal structure
* Algorithm
* Data structure
* Class structure
* Helper functions
* Validation strategy
* Error-handling strategy

from the reference implementation.

If two implementations satisfy the same public contract, the tests must accept both.

---

# 17. Evaluation Documentation

`EVALUATION.md` and `EVALUATION.es.md` are evaluator-only documents.

They may contain:

* Expected solution concept
* Possible valid approaches
* Expected or acceptable algorithms
* Expected complexity
* Important business rules
* Common mistakes
* Hidden-test rationale
* Scoring criteria

The evaluation documentation may describe a reference approach, but that approach must not become an implicit requirement when multiple valid implementations exist.

Do not expose these documents as part of the candidate-facing instructions.

---

# 18. Scoring

The default scoring model is 100 points:

| Category               |  Points |
| ---------------------- | ------: |
| Functional correctness |      50 |
| Edge cases             |      15 |
| Code quality           |      15 |
| Complexity             |      10 |
| Python usage           |      10 |
| **Total**              | **100** |

The evaluator may adjust the distribution when the exercise requires it, but the final score must always be normalized to 100.

---

# 19. Exercise Directory

Every exercise must have its own directory.

Use:

```text
YYYY-MM-DD-test-name/
```

Example:

```text
exercises/
└── 2026-09-08-order-discount-validator/
```

The name should be:

* Lowercase
* Descriptive
* Kebab-case
* Concise

---

# 20. Required Directory Structure

Each generated exercise must have:

```text
exercises/
└── YYYY-MM-DD-test-name/
    ├── README.md
   ├── EVALUATION.md
   ├── pyproject.toml
   ├── docs/
   │   │── README.es.md
   │   └── EVALUATION.es.md
   ├── solution/
   │   └── solution.py 
   └── tests/
       │── test_solution.py
       └── test_solution_hidden.py
```

---

# 21. Exercise Tracking

The root `README.md` contains the exercise tracking table.

Every generated exercise must be registered there.

The exercise registry is part of the repository workflow and must not be treated as optional documentation.

## When Creating an Exercise

After generating the exercise:

1. Open the root `README.md`.
2. Locate the Exercises table.
3. Add exactly one row for the new exercise.
4. Record:

   * Date
   * Exercise name
   * Type
   * Difficulty
   * Estimated time
5. Leave:

   * Score
   * Grade

   blank.
6. Set status to:

```text
Pending
```

Example:

```markdown
| 2026-09-08 | [Order Discount Validator](exercises/2026-09-08-order-discount-validator/) | Business Logic | Medium | 45 min | — | — | Pending |
```

## Duplicate Prevention

Before adding a row:

1. Check whether the exercise already exists in the table.
2. Check the exercise directory.
3. If the exercise is already registered, do not create another row.

The same exercise must never appear twice in the registry.

---

# 22. Exercise Variability

Each generation should produce a different exercise.

Vary:

* Domain
* Problem formulation
* Data structures
* Algorithmic pattern
* Business rules
* Input/output structure
* Reasoning requirements

Avoid generating the exact same exercise repeatedly.

Do not alternate mechanically between categories. Variation should feel natural.

---

# 23. Final Generation Output

After generating an exercise, report:

* Name
* Level
* Difficulty
* Estimated time
* Category
* Technologies
* Description
* Directory

Then provide the generated files and their paths.

Do not provide the actual solution implementation outside the evaluator documentation.

The generated starter code must be ready for the candidate to begin solving immediately while leaving implementation decisions to the candidate.

---

# 24. Final Checklist

Before finishing an exercise generation, verify:

* [ ] Exactly one exercise was generated.
* [ ] Exercise is coherent and self-contained.
* [ ] Difficulty is Easy, Easy/Medium, or Medium.
* [ ] Estimated duration is 30–60 minutes.
* [ ] Python is sufficient to solve it.
* [ ] No external services are required.
* [ ] Problem is not trivial.
* [ ] Problem is not a direct copy of another platform exercise.
* [ ] Requirements are unambiguous.
* [ ] Constraints are meaningful.
* [ ] Public interface is clearly defined.
* [ ] Starter solution exists.
* [ ] Starter solution exposes only the minimum necessary public interface.
* [ ] Starter solution does not reveal the intended implementation.
* [ ] Starter solution does not unnecessarily define dataclasses, enums, constants, helpers, or internal models.
* [ ] Starter docstring is concise.
* [ ] Starter docstring does not restate the exercise requirements.
* [ ] README.md exists.
* [ ] README.es.md exists.
* [ ] EVALUATION.md exists.
* [ ] EVALUATION.es.md exists.
* [ ] Public tests exist.
* [ ] Hidden tests exist.
* [ ] Tests depend only on the documented public interface.
* [ ] Tests do not depend on the reference implementation.
* [ ] `pytest` can discover the tests.
* [ ] Exercise is registered in the root README.
* [ ] Registry status is `Pending`.
* [ ] No duplicate registry entry exists.
