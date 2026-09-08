# Technical Tests

A collection of technical programming exercises for practicing interviews for **Junior Backend Developer**, **Junior Python Developer**, and **Software Engineering Intern** roles.

The exercises focus on:

* Python
* Problem solving
* Algorithms and data structures
* Business logic
* Edge cases
* Code quality
* Time and space complexity

The exercises are intentionally self-contained and do not require backend infrastructure such as databases, frameworks, Redis, Docker, or external services.

---

## How It Works

```text
Generate
   ↓
Solve
   ↓
Test
   ↓
Evaluate
   ↓
Review
   ↓
Improve
```

Exercises are generated and evaluated with the help of AI coding agents such as OpenCode. The repository rules define how exercises should be created and evaluated.

### Rules

* [`AGENTS.md`](AGENTS.md) — global repository rules
* [`docs/EXERCISE_RULES.md`](docs/EXERCISE_RULES.md) — exercise generation rules
* [`docs/EVALUATION_RULES.md`](docs/EVALUATION_RULES.md) — evaluation rules

---

## Exercises

| Date       | Exercise                                                               | Type           | Difficulty  |   Time | Score | Grade | Status  |
| ---------- | ---------------------------------------------------------------------- | -------------- | ----------- | -----: | ----: | ----: | ------- |
| 2026-09-08 | [Meeting Room Allocator](exercises/2026-09-08-meeting-room-allocator/) | Business Logic | Medium | 45 min | — | — | Pending |

### Status

* `Pending` — generated but not yet evaluated.
* `Completed` — solution successfully evaluated.
* `Needs Review` — solution requires improvement.
* `Failed` — solution did not meet the minimum requirements.

The table is the source of truth for exercise progress. Existing exercises must be updated rather than duplicated.

---

## Exercise Structure

Each exercise is self-contained:

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

* `README.md` / `README.es.md` — candidate-facing exercise specification.
* `EVALUATION.md` / `EVALUATION.es.md` — evaluator documentation.
* `solution/` — candidate implementation.
* `tests/` — public and hidden tests.

---

## Creating an Exercise

Start OpenCode from the repository root:

```bash
opencode
```

Then ask for an exercise, for example:

```text
Create a new technical exercise about inventory management.
```

The agent will follow the repository rules, generate one exercise, create its files, add the exercise to the table above, and mark it as `Pending`.

---

## Solving an Exercise

Open the exercise README and implement the solution in:

```text
solution/solution.py
```

Run the tests from the exercise directory:

```bash
pytest
```

The starter code provides only the minimum public interface. The candidate decides the internal implementation.

---

## Evaluating a Solution

After completing an exercise, ask the agent:

```text
Evaluate the current solution.
```

The evaluation produces a score from **0–100**, a grade from **1–10**, and an evaluation status.

The existing exercise entry in the table is then updated with the latest result.

---

## Requirements

Recommended environment:

* Python 3.12+
* pytest
* OpenCode or another AI coding agent

Exercises should primarily use the Python Standard Library.

---

## Goal

Build a repeatable practice routine for technical interviews while keeping each exercise focused on **problem solving and Python**, rather than infrastructure or framework knowledge.

---

## License

Distributed under the **MIT License**. See [LICENSE](/LICENSE) for more details.

---

> Created with ♥️ by [JohannGaviria](https://github.com/JohannGaviria); always open to connect for feedback, collaboration, or to explore job opportunities.