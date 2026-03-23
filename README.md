# Markov Decision Process

## Description

A Markov Decision Process, or MDP, is a model used in artificial intelligence for making decisions step by step over time. In an MDP, an agent is in a state, chooses an action, moves to a new state, and receives a reward or penalty. The goal is to choose actions that lead to the best total result in the future.

## How It Works

1. Identify the possible states.
2. Identify the possible actions in each state.
3. Give rewards or penalties for outcomes.
4. Predict what state may happen next after each action.
5. Choose the action that gives the best long-term result.

## Examples

### 1. Campus Navigation at USM

An MDP can be used at the University of Southern Mindanao to help a student or campus staff member decide the best path from one office or college building to another. At each step, the person chooses where to go next, and each decision affects how quickly the destination can be reached. In the demo, the campus states use more realistic names such as the Administration Building, the College of Education, the College of Arts and Sciences, the College of Engineering and Information Technology, the College of Agriculture, and the Admission and Records Office.

### 2. Study Planning Before an Exam at USM

An MDP can also be used by a student at the University of Southern Mindanao to decide whether to study, review, or rest each day before an exam. Each choice changes the student’s preparation level and affects the final exam result.

## Demo Files

- `campus_navigation_mdp_demo.py` shows a simple MDP that recommends the best next move between USM buildings.
- `study_planner_mdp_demo.py` shows a simple MDP that recommends the best action before an exam.

## Summary

Markov Decision Processes help AI choose the best action step by step. They are useful when each decision affects future outcomes, such as navigation, planning, and scheduling.
