# Exercise 01 — Testing Pipeline Duration

## Objective

Write unit tests for a function that calculates the duration of a pipeline execution.

The goal of this exercise is to practice translating software requirements into clear and testable assertions before implementing the actual functionality.

## Specification

Implement tests for a function named `calculate_duration(start, end)`.

The function represents the execution time of a pipeline run.

Requirements:

- The function should calculate and return the duration between `start` and `end`.
- The duration should be returned in seconds.
- If `start` and `end` are equal, the function should return `0`.
- If `end` occurs before `start`, the function should raise a `ValueError`.

For this exercise, `start` and `end` can be represented as numeric values in seconds.

## Task

Using Python's `unittest` framework:

1. Create a test class that inherits from `unittest.TestCase`.
2. Translate each requirement into one or more test cases.
3. Include tests for normal behavior, boundary conditions, and invalid input described by the specification.
4. Do not implement the production function until the expected behavior has been expressed through tests.

## Goal

The test suite should clearly describe the expected behavior of `calculate_duration()` and act as an executable specification for its future implementation.