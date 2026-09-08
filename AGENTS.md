# AGENTS.md

## Repository Purpose

This repository contains technical programming exercises designed to simulate technical interviews for:

* Junior Backend Developers
* Software Engineering Interns
* Junior Python Developers

The primary programming language is Python.

The repository is intended to evaluate:

* Problem-solving ability
* Python fundamentals
* Algorithms and data structures
* Business logic implementation
* Edge-case handling
* Code quality
* Computational complexity

Exercises must remain focused on programming and problem solving rather than framework-specific implementation.

---

## Persistent Rules

These rules apply to every agent operating in this repository.

### 1. Exercise Scope

Each exercise must represent **one single coherent programming problem**.

One exercise must never contain:

* Multiple independent exercises
* Exercise 1 / Exercise 2 / Exercise 3
* A collection of unrelated challenges
* A multi-question technical test
* Several independent tasks bundled together

A single exercise may contain multiple interacting requirements when they belong to the same problem.

---

### 2. Candidate Level

All exercises must target:

* Junior Backend Developer
* Software Engineering Intern
* Junior Python Developer

Exercises must assume solid Python fundamentals but should not require advanced knowledge.

Do not design exercises for:

* Senior developers
* Advanced competitive programming
* Advanced system design
* Complex architecture
* Distributed systems
* Infrastructure engineering

---

### 3. Exercise Duration

Every exercise must be realistically solvable within:

**30–60 minutes**

The exercise should be challenging enough to evaluate the candidate while remaining appropriate for the target level.

---

### 4. Technology Scope

Python is the primary language.

Prefer the Python Standard Library.

Exercises must not require:

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

Frameworks or infrastructure may only be mentioned as contextual background when they are not required to solve the exercise.

---

### 5. Code Language

All source code must be written in English.

This includes:

* Variables
* Functions
* Classes
* Methods
* Constants
* Docstrings
* Comments
* Test names

Documentation must be provided in:

* English
* Spanish

---

# Exercise Generation

When asked to create an exercise:

1. Read `docs/EXERCISE_RULES.md`.
2. Generate exactly one exercise.
3. Create a new exercise directory.
4. Generate the required documentation.
5. Generate the minimal starter solution.
6. Generate public and hidden tests.
7. Register the exercise in the root `README.md`.
8. Set its initial status to `Pending`.

Do not skip the registration step.

---

# Exercise Evaluation

When asked to evaluate a solution:

1. Read `docs/EVALUATION_RULES.md`.
2. Read the exercise documentation.
3. Inspect the candidate implementation.
4. Run the available tests.
5. Evaluate the implementation according to the evaluation rules.
6. Generate the evaluation documents.
7. Calculate the final score and grade.
8. Update the existing exercise entry in the root `README.md`.

Do not create a second registry entry for an already existing exercise.

---

# Exercise Tracking

The root `README.md` contains the official exercise tracking table.

The table is the repository's source of truth for exercise progress.

Agents must keep this table synchronized with the actual state of the repository.

### When Creating an Exercise

The agent must:

* Add exactly one row to the table.
* Register the exercise using its directory name or a link to the exercise directory.
* Record:

  * Date
  * Exercise name
  * Type
  * Difficulty
  * Estimated time
  * Status
* Leave score and grade empty.
* Set status to `Pending`.

### When Evaluating an Exercise

The agent must:

* Locate the existing exercise row.
* Update that row.
* Add the final score.
* Add the grade.
* Update the status.
* Add evaluation-related information when useful.

Never create a new row for an exercise that already exists.

### When Re-evaluating

If an exercise is evaluated again:

* Update the existing row.
* Do not create another row.
* Replace outdated score/status information with the latest evaluation.

### Exercise Statuses

Use only these statuses unless the repository rules explicitly define another one:

* `Pending` — generated but not yet solved or evaluated.
* `Completed` — solution evaluated successfully.
* `Needs Review` — solution works partially or requires improvement.
* `Failed` — solution does not meet the minimum requirements.

---

# Existing Exercises

Agents must not modify an existing exercise unless explicitly requested.

This includes:

* Exercise requirements
* Examples
* Starter code
* Public tests
* Hidden tests
* Evaluation criteria

When evaluating an exercise, do not alter the candidate's implementation or tests merely to make them pass.

---

# Starter Solutions

Starter code must provide the **minimum necessary public interface** required for the candidate to begin the exercise.

The starter code exists to answer:

> **Where do I implement my solution?**

It must not answer:

> **How should I implement the solution?**

### Starter Code Philosophy

The candidate must derive the implementation from the exercise specification.

The starter should normally contain only:

* One public function, or
* One public class when a class is genuinely the natural public interface.

Type annotations may be included when they are necessary to define the public contract.

A concise docstring may describe the general purpose of the entry point.

### Starter Code Must Not Provide

Do not predefine implementation decisions such as:

* Business-rule constants
* Error constants
* Error classes
* Enums
* Dataclasses
* Internal models
* Helper functions
* Internal data structures
* Predefined result structures
* Validation categories
* Processing steps
* Algorithm hints
* Suggested algorithms
* Implementation-specific comments
* Detailed docstrings that restate the exercise requirements

Do not decompose the problem into helper functions or classes before the candidate has done so.

Do not encode business rules in constants, names, types, or comments that effectively reveal how the problem should be solved.

### Public Interface

The starter may define the public entry point required by the tests.

For example:

```python
def process_bookings(rooms: list, requests: list) -> dict:
    """Process booking requests and return the allocation report."""
    raise NotImplementedError
```

The exact interface depends on the exercise.

The candidate is responsible for deciding:

* Internal data models
* Helper functions
* Constants
* Validation strategy
* Error handling
* Data structures
* Processing strategy
* Algorithm
* Internal organization

Additional types or classes are allowed in the starter only when they are genuinely part of the required public contract and cannot reasonably be left for the candidate to design.

### Starter Code and Difficulty

Starter code must not make the exercise substantially easier by exposing the intended solution structure.

The exercise documentation defines **what the program must do**.

The starter code defines **where the candidate begins**.

The candidate decides **how the program works internally**.

---

# Tests

Tests use `pytest`.

Tests must validate **observable behavior through the documented public interface**.

Tests must not depend on a particular internal implementation.

A valid candidate solution may use:

* Different helper functions
* Different classes
* Different data structures
* Different algorithms
* Different internal organization

as long as it satisfies the documented public contract and requirements.

### Public Tests

Public tests should cover:

* Main examples
* Normal cases
* Basic edge cases
* Main business rules
* Relevant invalid cases

### Hidden Tests

Hidden tests should focus on:

* Edge cases
* Boundary conditions
* Interacting business rules
* Empty input
* Single-element input
* Duplicate values
* Zero and negative values when relevant
* Large inputs when complexity matters
* Common incomplete implementations

Hidden tests must also use only the documented public interface.

Never write tests that expect the candidate to reproduce an imagined reference implementation.

---

# Quality Standards

Exercises must be realistic technical assessments.

Avoid trivial exercises such as:

* FizzBuzz
* Factorial
* Basic Fibonacci
* Simple sum
* Simple maximum/minimum
* Basic palindrome checking
* Other exercises requiring almost no reasoning

Exercises must not be direct copies of:

* LeetCode
* HackerRank
* CodeSignal
* Other existing coding challenge platforms

Known algorithms and patterns may be used, but the exercise should use an original scenario and problem formulation.

---

# Agent Behavior

Before modifying files:

1. Inspect the repository structure.
2. Read the applicable rules.
3. Understand the existing exercise state.
4. Avoid unnecessary changes.
5. Preserve the established repository conventions.

When generating an exercise, ensure that:

* The README explains the complete problem.
* The starter exposes only the minimum public interface.
* Tests depend only on that public interface.
* The candidate is free to design the internal solution.
* The root `README.md` is updated exactly once.

When evaluating a solution:

* Evaluate the candidate's actual implementation.
* Do not require a specific internal architecture unless explicitly stated in the exercise.
* Do not penalize a valid implementation merely because it differs from the reference solution.
* Do not modify the candidate's code to make it pass.
* Use behavior and documented requirements as the basis for evaluation.

When rules conflict, use this priority:

1. `AGENTS.md`
2. The applicable document in `docs/`
3. Existing repository conventions
4. The user's explicit request

The user's explicit request may override repository conventions when the request clearly requires a different behavior.
