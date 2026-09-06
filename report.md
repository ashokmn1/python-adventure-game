# Building a Python Adventure Game with an AI Coding Assistant

Project report — `adventure_game.py`

## Overview

This project implements a text-based CLI adventure game in Python, following the
course-end project brief. The player is asked for their name, then chooses between
exploring a forest or a mysterious cave. Each path branches into a further decision,
ultimately leading to one of two outcomes — finding the treasure (win) or ending the
quest early (lose) — after which the player is offered the option to restart.

## How the AI Coding Assistant Helped

- **Function scaffolding:** Given the task description for each function
  (`start_game()`, `forest_path()`, `cave_path()`), the assistant generated an
  initial structure and prompt/print flow in seconds, which was then reviewed and
  adjusted rather than written from scratch.
- **Input validation:** The assistant suggested factoring repeated "ask until
  valid" logic into a single reusable `get_choice()` helper that takes a list of
  valid choices, instead of duplicating validation code in every branch.
- **Branch design:** It proposed adding a second decision inside each of the
  forest and cave paths (e.g. river → row/walk, torch → proceed/rush) so that each
  initial choice leads to a further event rather than an immediate win/lose,
  matching the brief's requirement that "each choice will trigger a new event,
  leading to more decisions."
- **Game loop:** The assistant suggested wrapping the whole game in a `while True`
  loop inside `main()` with an explicit yes/no restart prompt, so the program
  keeps running until the player chooses to stop.
- **Readability pass:** Minor suggestions on variable naming and consolidating
  duplicate print statements kept the final script compact.

## Key Challenges Faced

- **Balancing depth vs. complexity:** The brief asks for meaningful
  decision-making without turning the game into an unwieldy tree of branches. The
  solution was to keep exactly two decision levels per path (four scenarios
  total), which is enough to feel like a real adventure without becoming hard to
  test or follow.
- **Handling invalid input:** Early versions of the game crashed or behaved oddly
  if the player typed something other than the expected choice. This was solved
  with the shared `get_choice()` validator that re-prompts until a valid option is
  entered.
- **Testing all paths:** Because the game is interactive, verifying every
  win/lose branch required scripting input sequences (e.g. piping
  `"name\nforest\nriver\nrow\n..."` into the program) to simulate a full
  playthrough of each path non-interactively.

## Enhancements Made Beyond the Base Requirements

- Added a second-level choice within both the forest and cave paths (rather than
  a single choice leading straight to an outcome), giving four distinct win/lose
  scenarios instead of two.
- Added a reusable input-validation helper (`get_choice`) so the game never
  crashes or behaves unexpectedly on unrecognized input — it simply re-prompts
  the player.
- Defaulted a blank name entry to `"Explorer"` so the game doesn't break if the
  player just presses Enter.
- Wrapped the game in a restart loop with an explicit yes/no prompt, satisfying
  the "restarting" ending condition from the brief.

## Conclusion

The final `adventure_game.py` script meets all five tasks in the brief: game
setup, an introduction/name-entry function, a forest path, a cave path, and a
runnable game loop with a restart option. Using an AI coding assistant sped up
the initial scaffolding and helped surface a cleaner way to handle input
validation, while the overall game design, branch balancing, and testing were
driven and verified manually.
