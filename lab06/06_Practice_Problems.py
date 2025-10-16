"""
Lab 06 — Practice Problems (Pick any 3)

Guidelines
- Solve using standard library objects emphasized in this lab.
- Keep functions pure where reasonable; use type hints.
- Write a short demo under `if __name__ == "__main__":` to verify.

Problems
1) Birthday Countdown — days until next birthday.
2) File Extension Reporter — counts by extension in a folder.
3) Random Password Generator — configurable password string.
4) Study Session Planner — generate time blocks with breaks.
5) Directory Tree Analyzer — total size and counts by extension (recursive).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from datetime import date, datetime, timedelta
from pathlib import Path
from collections import Counter, defaultdict, namedtuple, deque
import random
import string


def birthday_countdown(month: int, day: int, today: date | None = None) -> tuple[int, str]:
    """Return (days_until, weekday_name) for the next occurrence of month/day.

    Examples
    >>> d, w = birthday_countdown(12, 25, today=date(2025, 12, 20))
    >>> d, w
    (5, 'Thursday')
    """
    d0 = today or date.today()
    target = date(d0.year, month, day)
    if target < d0:
        target = date(d0.year + 1, month, day)
    days = (target - d0).days
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][
        target.weekday()
    ]
    return days, weekday


def file_extension_report(root: Path) -> Counter[str]:
    """Return counts of file extensions (including dot, lowercased) in `root` (non-recursive)."""
    ctr: Counter[str] = Counter()
    for p in root.iterdir():
        if p.is_file():
            ctr[p.suffix.lower()] += 1
    return ctr


def random_password(
    length: int = 12,
    *,
    uppercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
    seed: int | None = None,
) -> str:
    """Generate a random password. Ensure at least one of each selected category."""
    if length < 4:
        raise ValueError("length must be >= 4")
    rng = random.Random(seed)

    pools = [string.ascii_lowercase]
    if uppercase:
        pools.append(string.ascii_uppercase)
    if digits:
        pools.append(string.digits)
    if symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?/\\|")

    chosen = [rng.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chosen.extend(rng.choice(all_chars) for _ in range(max(0, length - len(chosen))))
    rng.shuffle(chosen)
    return "".join(chosen[:length])


def study_session_plan(
    start: datetime,
    duration_minutes: int,
    focus_block: int = 25,
    break_minutes: int = 5,
) -> list[tuple[datetime, datetime, str]]:
    """Return a list of (block_start, block_end, label) tuples.

    Blocks alternate between focus and short breaks, ending at or before the allotted time.
    """
    out: list[tuple[datetime, datetime, str]] = []
    remaining = timedelta(minutes=duration_minutes)
    t = start
    while remaining > timedelta(0):
        # Focus block
        f = timedelta(minutes=min(focus_block, int(remaining.total_seconds() // 60)))
        if f <= timedelta(0):
            break
        out.append((t, t + f, "focus"))
        t += f
        remaining -= f
        if remaining <= timedelta(0):
            break
        # Break block
        b = timedelta(minutes=min(break_minutes, int(remaining.total_seconds() // 60)))
        if b <= timedelta(0):
            break
        out.append((t, t + b, "break"))
        t += b
        remaining -= b
    return out


def directory_tree_analyzer(root: Path) -> tuple[int, Counter[str]]:
    """Return (total_size_in_bytes, counts_by_extension) recursively for a directory.

    Skips broken symlinks. Follows regular files only.
    """
    total = 0
    counts: Counter[str] = Counter()
    for p in root.rglob("*"):
        try:
            if p.is_file():
                total += p.stat().st_size
                counts[p.suffix.lower()] += 1
        except FileNotFoundError:
            # race condition or broken link; skip
            continue
    return total, counts


def _demo() -> None:
    print("Birthday Countdown (12/25):", birthday_countdown(12, 25, today=date(2025, 12, 20)))
    print("\nExtension report (lab06/):", file_extension_report(Path("lab06")))
    print("\nRandom password (seeded):", random_password(12, seed=7))

    print("\nStudy plan:")
    blocks = study_session_plan(datetime(2025, 1, 1, 9, 0), 60)
    for b in blocks:
        print("  ", b[0].strftime("%H:%M"), "->", b[1].strftime("%H:%M"), b[2])

    print("\nDirectory tree analyzer (lab06/):")
    total, counts = directory_tree_analyzer(Path("lab06"))
    print("  total bytes:", total)
    print("  top counts:", counts.most_common(3))


if __name__ == "__main__":
    _demo()

