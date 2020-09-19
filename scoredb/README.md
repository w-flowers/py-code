A simple score database api using sqlite3.

Score db contains functions to:
- Enter a score with a name, time taken and date entered
- Return a list of scores in order of entry (newest to oldest)
- Return a list of scores from a particular username in order of entry (newest to oldest)
- Return a list of scores in order of score (use can specify high to low or low to high)

Included in this repository is a simple guessing game to demonstrate the usage of this module.

Also included is a sample database file to query.

Possible future expansions:
- Enable listing scores by date range
- Enable deleting or modifying score database entries
- Enable users to access multiple tables (useful for a game which has multiple stages/difficulty levels)