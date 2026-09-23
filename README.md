# OSRIC 3.0 Character Generator

A command-line Python tool for rapidly generating player characters for
**OSRIC 3.0** (Old School Reference and Index Compilation), an OSR ruleset
based on 1st Edition AD&D. The goal is to let a player interactively build
a legal OSRIC 3.0 character of any level, with a GUI planned as a later
phase.

## Status

Early / work-in-progress. Currently a single script, `chargen.py`, that
generates **level 1** characters only, interactively via the terminal.

## What it does today

- Prompts for number of characters to generate, desired ancestry (or "any"),
  desired class (or "any"), and an ability score rolling method.
- Rolls ability scores (3d6 "Hardest Mode" and 4d6-drop-lowest "Normal Mode"
  are implemented; "Difficult" and "Flexible" modes are not).
- Applies racial ability adjustments and filters out illegal
  race/class combinations based on minimum/maximum ability scores
  (including multi-class combinations).
- Rolls hit points at level 1 (including CON modifier and the ranger's
  double-CON-bonus rule).
- Randomly determines alignment consistent with class restrictions.
- Randomly determines a level 1 spellbook for magic-users and illusionists.
- Rolls starting gold.
- Rolls height, weight, age, and gender.
- Prints a formatted character summary to the console.

## Requirements

- Python 3 (standard library only — `random`, `re`)

## Usage

```bash
python chargen.py
```

Follow the interactive prompts.

## TODO

### Ancestry
- [ ] Add ancestry level limits by class.
- [ ] Implement special ancestry abilities (e.g. dwarf detect depth
      underground, gnome direction sense, elf secret door detection, etc.).
- [ ] Select and record actual starting languages (racial + alignment
      tongue + INT-based bonus languages), rather than just listing what's
      *available* to a race.

### Ability scores
- [X] Implement "Difficult Mode" (3d6, arrange freely).
- [ ] Implement "Flexible Mode" (4d6 drop lowest, arrange freely).
- [ ] Roll exceptional strength (18/01–18/00) for fighters, paladins, and
      rangers with 18 STR.
- [ ] Compute and store derived ability modifiers (to-hit/damage/encumbrance
      for STR, AC/missile/initiative/agility-save for DEX, resurrection
      survival % and system shock % for CON, bonus languages for INT,
      mental save modifier for WIS, loyalty/reaction/henchman-limit for CHA).
- [ ] Apply ability score adjustments for age.

### Classes
- [ ] Let the player choose specific weapon proficiencies (currently only
      the *count* per class exists).
- [ ] Implement optional weapon specialization for fighter/paladin/ranger.
- [ ] Implement class special abilities (cleric turn undead, paladin detect
      evil/lay on hands/protection from evil, ranger tracking, monk special
      attacks, druid nature abilities, etc.) — currently classes are just
      stat blocks.

### Spellcasting
- [ ] Magic-user: starting spellbook should be 2 randomly rolled spells +
      2 player-chosen spells (one of which must be Read Magic if not
      rolled) — currently all 4 are chosen randomly with no player input.
- [ ] Illusionist: starting spellbook should be 2 randomly rolled spells +
      1 player-chosen spell — currently all 3 are random.
- [ ] Implement cleric spellcasting entirely (spell list, per-level spell
      slot table, WIS bonus spell slots, memorization step) — not present
      at all currently.
- [ ] Implement druid spellcasting entirely (same as above).
- [ ] Add spell-level slot progression tables for magic-user/illusionist
      beyond level 1 (needed for "any level" generation).

### Thief / Assassin
- [ ] Implement thief skill percentages (backstab, climb, hide, listen,
      pick locks, pick pockets, read languages, move quietly, find/remove
      traps) plus DEX and ancestry adjustments.

### Equipment & combat stats
- [ ] Implement starting equipment purchase (armor, weapons, general gear)
      — gold is currently rolled but never spent.
- [ ] Calculate Armour Class from purchased armor/shield/DEX.
- [ ] Calculate encumbrance (carried weight vs. STR allowance) and its
      effect on movement rate.

### Levels
- [ ] Support generating characters above level 1 (stated project goal —
      currently hard-coded to level 1 only).

### Code quality
- [ ] `get_available_race_and_classes` recomputes racial ability
      adjustments purely to test eligibility, then discards the result;
      `select_available_race_and_classes` independently re-implements the
      same adjustment/clamp logic on the real ability scores. Factor this
      into one shared helper to avoid the two copies drifting apart (this
      duplication is how the half-orc CHA bug went unnoticed).
- [ ] Consider a clearer name for `get_available_race_and_classes` — it
      filters/computes eligible combinations rather than fetching existing
      data.
- [ ] No persistence — generated characters aren't saved to a file.

### GUI
- [ ] Design and build an interactive GUI (stated long-term project goal).