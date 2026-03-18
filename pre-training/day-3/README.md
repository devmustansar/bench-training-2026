# Day 3 - Task Tracker CLI

## Usage Examples

```bash
# Add tasks
python3 tasks.py add 'Fix login bug'
python3 tasks.py add 'Write unit tests'
python3 tasks.py add 'Deploy to staging'

# Mark a task done (by its ID)
python3 tasks.py done 1

# List all tasks
python3 tasks.py list

# List only pending tasks
python3 tasks.py list --filter todo

# List only completed tasks
python3 tasks.py list --filter done

# Delete a task permanently
python3 tasks.py delete 2
```

## Sample Output

```
All Tasks:
  ──────────────────────────────────────────────────────────
  ID    Title                 Status  Created
  ──────────────────────────────────────────────────────────
  1     Fix login bug         done  2026-03-18 22:04:30
  2     Write unit tests      todo  2026-03-18 22:04:31
  3     Deploy to staging     todo  2026-03-18 22:04:32
  ──────────────────────────────────────────────────────────
```

## Why a Class Instead of Just Functions?

A class lets you bundle **state** and **behaviour** together in one place.

`TaskManager` owns the task list and the file path, every method it exposes operates on that same internal state, so there is no need to pass the list around as an argument to every function call.
If I had used plain functions, I would have had to either keep a global variable or pass the task list in and out of every function.
The class also makes the persistence layer invisible to the caller, whoever calls `add_task` doesn't have to remember to call `save()` afterwards, because the class does it internally.
