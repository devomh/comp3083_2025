"""
Module 3 — Standard Library Core Objects

Complete the exercises below. A small demo runs when executed directly.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

from datetime import date, datetime, timedelta
from pathlib import Path
from collections import Counter, deque, namedtuple, defaultdict
import random
import string


def days_until(month: int, day: int, today: date | None = None) -> int:
    """Return number of days from today until the next occurrence of month/day.

    Example: days_until(12, 25) near December returns small number, otherwise wraps to next year.
    """
    d0 = today or date.today()
    target = date(d0.year, month, day)
    if target < d0:
        target = date(d0.year + 1, month, day)
    return (target - d0).days


def count_extensions(root: Path) -> Counter[str]:
    """Return a Counter mapping file extensions (lowercased, including dot) to counts.

    Skips directories. Example: {'.py': 5, '.md': 2, '': 1}
    """
    ctr: Counter[str] = Counter()
    for p in root.iterdir():
        if p.is_file():
            ctr[p.suffix.lower()] += 1
    return ctr


def generate_password(
    length: int = 12,
    *,
    uppercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
    seed: int | None = None,
) -> str:
    """Generate a random password meeting the requested criteria.

    Ensures at least one char from each selected category when possible.
    """
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

    # Guarantee one from each chosen pool (except lowercase which is always included)
    chosen: list[str] = [rng.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chosen.extend(rng.choice(all_chars) for _ in range(max(0, length - len(chosen))))
    rng.shuffle(chosen)
    return "".join(chosen[:length])


def top_n_letters(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the top-N most common letters (case-insensitive) using Counter."""
    letters = [ch.lower() for ch in text if ch.isalpha()]
    return Counter(letters).most_common(n)


def _demo() -> None:
    print("Days until birthday (Aug 15):", days_until(8, 15))

    print("\nExtensions in current dir:")
    for ext, count in count_extensions(Path("." )).most_common():
        print(f"  {ext or '<no-ext>'}: {count}")

    print("\nRandom password (seeded):", generate_password(12, seed=42))

    print("\nTop letters:", top_n_letters("Hello, world!!", 2))


if __name__ == "__main__":
    _demo()

