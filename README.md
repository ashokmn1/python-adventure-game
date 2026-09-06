# Quest for the Lost Treasure

A text-based CLI adventure game written in Python. You play an explorer searching
for a legendary treasure, choosing between a forest or a cave and making a series
of decisions that lead to winning, losing, or restarting the quest.

## Requirements

- Python 3

## How to run

```
python3 adventure_game.py
```

## How to play

1. Enter your name when prompted.
2. Choose a starting path: `forest` or `cave`.
3. **Forest path:** choose `river` or `tree`, then a follow-up choice
   (`row`/`walk` or `higher`/`down`).
4. **Cave path:** choose `torch` or `dark`, then a follow-up choice
   (`proceed`/`rush` or `walking`/`turn`).
5. Each path ends in a win (you find the treasure) or a loss (the quest ends).
6. After each attempt, choose `yes` to play again or `no` to quit.

Input is validated at every prompt — an unrecognized answer re-prompts instead of
crashing the game.

## Project structure

- `adventure_game.py` — the game
- `report.md` — write-up on how an AI coding assistant helped build the game, key
  challenges, and enhancements made beyond the base assignment requirements
- `PROBLEM_STATEMENT.md` — the original course-end project brief this game was built to
