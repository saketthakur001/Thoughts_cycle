# Thoughts_cycle

A small command-line Python script for jotting down thoughts and diary entries from
the terminal. Each entry is timestamped and saved to disk with `pickle`.

## Files

- `what's_happening.py` — the main program (interactive CLI loop).
- `thoughts.dat` — pickled thoughts saved by the `-t` command (contains sample data from testing).
- `diary.dat` — pickled diary entries saved by the `-d` command (contains sample data from testing).
- `tests.py` — a scratch file experimenting with `datetime.now()`; not an automated test suite.

## Usage

Requires Python 3 (standard library only, no extra dependencies).

```bash
python "what's_happening.py"
```

Then type a command at the `what's up?:` prompt:

- `-h` — show help.
- `-t` — enter thoughts mode. Type a thought (5+ characters) at each prompt; type `exit` to stop and save. Each saved thought is timestamped and appended to `thoughts.dat`.
- `-d` — enter diary mode. Same flow as thoughts, appended to `diary.dat`.
- `-r` — meant to read back saved entries; currently only shows the help text and doesn't actually read `thoughts.dat`/`diary.dat` (see Limitations).
- `exit` — quit the program.

## Limitations

- The `-r` (read) command is a stub: it never loads or prints the saved `.dat` files.
- Only the entries from the *current* run are printed back (via `pickle.load`) after saving; there's no way to view the full history of previously saved entries.
- Entries shorter than 5 characters are silently discarded.
- `thoughts.dat` and `diary.dat` currently contain leftover sample entries from development/testing rather than being empty data files.

This is a personal, work-in-progress hobby script rather than a polished tool.
