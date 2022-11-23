
# Using/Testing:

## General:
- Typer
- Protocols (comp w/: ABC)
- Generators for file processing (see also: CoRoutine set-ups)
- TQDM
- possibly: Pydantic for verification
- proper pathing & access despite use of `/src` structure

## Dev:
- Poetry (venv, dependencies, locking, (possibly) publishing)
- PDocs
- Black
- Pylint (possbly comp it & Black w/: flake8)
- Pyright (possibly comp it with MyPy as an asynch check)
- Pytest (possibly check relations with Hypothesis -- particularly for reversability)
