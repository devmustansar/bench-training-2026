#!/usr/bin/env python3

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"
VALID_STATUSES = ("todo", "done")
DATE_FMT = "%Y-%m-%d %H:%M:%S"

class TaskManager:
    def __init__(self, filepath: Path = TASKS_FILE) -> None:
        self._filepath = filepath
        self._tasks: list[dict] = self._load()

    def _load(self) -> list[dict]:
        if not self._filepath.exists():
            return []
        try:
            raw = self._filepath.read_text(encoding="utf-8").strip()
            if not raw:
                return []
            data = json.loads(raw)
            if not isinstance(data, list):
                raise ValueError("Expected a JSON array at top level.")
            return data
        except json.JSONDecodeError as exc:
            print(
                f"[error] tasks.json is corrupt and cannot be parsed: {exc}\n"
                "Rename or delete the file to start fresh.",
                file=sys.stderr,
            )
            sys.exit(1)
        except ValueError as exc:
            print(f"[error] Unexpected data format: {exc}", file=sys.stderr)
            sys.exit(1)

    def _save(self) -> None:
        self._filepath.write_text(
            json.dumps(self._tasks, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def _next_id(self) -> int:
        return max((t["id"] for t in self._tasks), default=0) + 1

    def _find(self, task_id: int) -> dict | None:
        return next((t for t in self._tasks if t["id"] == task_id), None)

    def add_task(self, title: str) -> dict:
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        task = {
            "id": self._next_id(),
            "title": title,
            "status": "todo",
            "created_at": datetime.now(timezone.utc).strftime(DATE_FMT),
        }
        self._tasks.append(task)
        self._save()
        return task

    def complete_task(self, task_id: int) -> dict:
        task = self._find(task_id)
        if task is None:
            raise KeyError(f"No task with id={task_id}.")
        if task["status"] == "done":
            print(f"[info] Task #{task_id} is already marked done.")
            return task
        task["status"] = "done"
        self._save()
        return task

    def delete_task(self, task_id: int) -> dict:
        task = self._find(task_id)
        if task is None:
            raise KeyError(f"No task with id={task_id}.")
        self._tasks.remove(task)
        self._save()
        return task

    def list_tasks(self, status_filter: str | None = None) -> list[dict]:
        if status_filter is not None and status_filter not in VALID_STATUSES:
            raise ValueError(
                f"Invalid filter '{status_filter}'. Choose from: {VALID_STATUSES}"
            )
        if status_filter:
            return [t for t in self._tasks if t["status"] == status_filter]
        return list(self._tasks)

def _print_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("  (no tasks)")
        return

    col_id    = 4
    col_title = max(len(t["title"]) for t in tasks)
    col_title = max(col_title, 20)
    col_stat  = 6

    header  = f"  {'ID':<{col_id}}  {'Title':<{col_title}}  {'Status':<{col_stat}}  Created"
    divider = "  " + "─" * (len(header) - 2)

    print(divider)
    print(header)
    print(divider)
    for t in tasks:
        print(
            f"  {t['id']:<{col_id}}  {t['title']:<{col_title}}"
            f"  {t['status']:<{col_stat}}  {t['created_at']}"
        )
    print(divider)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tasks.py",
        description="A minimal CLI task tracker with JSON persistence.",
    )
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.required = True

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task title (wrap in quotes)")

    # done
    p_done = sub.add_parser("done", help="Mark a task as completed")
    p_done.add_argument("id", type=int, help="Task ID")

    # delete
    p_del = sub.add_parser("delete", help="Delete a task permanently")
    p_del.add_argument("id", type=int, help="Task ID")

    # list
    p_list = sub.add_parser("list", help="List tasks (optionally filtered)")
    p_list.add_argument(
        "--filter",
        dest="filter",
        choices=VALID_STATUSES,
        help="Show only 'todo' or 'done' tasks",
    )

    return parser

def main() -> None:
    parser = build_parser()
    args   = parser.parse_args()
    mgr    = TaskManager()

    try:
        if args.command == "add":
            task = mgr.add_task(args.title)
            print(f"[added] #{task['id']} — {task['title']}")

        elif args.command == "done":
            task = mgr.complete_task(args.id)
            print(f"[done]  #{task['id']} — {task['title']}")

        elif args.command == "delete":
            task = mgr.delete_task(args.id)
            print(f"[deleted] #{task['id']} — {task['title']}")

        elif args.command == "list":
            tasks = mgr.list_tasks(status_filter=args.filter)
            label = f"Tasks ({args.filter})" if args.filter else "All Tasks"
            print(f"\n{label}:")
            _print_tasks(tasks)

    except KeyError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
