"""
Module 1 — Variables and Types Review (Fundamentals)

Complete the TODOs. Run this file directly to see sample output.
Focus: identity vs equality, mutability, type hints, and object exploration.
"""

from __future__ import annotations
from typing import Any


def identity_vs_equality_examples() -> list[tuple[bool, bool]]:
    """Return a list of (equals, is_same_object) results for curated pairs.

    Students: Predict before running, then verify.
    """
    # Numbers (small ints may be interned by CPython)
    a = 42
    b = 42
    # Lists (distinct objects with same values)
    x = [1, 2]
    y = [1, 2]
    z = x

    results: list[tuple[bool, bool]] = []
    results.append((a == b, a is b))  # likely (True, True) because of interning
    results.append((x == y, x is y))  # (True, False)
    results.append((x == z, x is z))  # (True, True)
    return results


def mutation_station() -> tuple[str, str, list[int], list[int]]:
    """Demonstrate immutable vs mutable behavior.

    Returns:
    - original_string, uppercased_string (original unchanged)
    - original_list_after_append, returned_value_from_append (None)
    """
    s = "alice"
    s2 = s.upper()  # new string

    nums = [3, 1, 2]
    returned = nums.sort()  # in-place mutation; returns None

    return s, s2, nums, [returned]  # wrap returned in list to make it visible


def type_explorer(obj: Any) -> dict[str, Any]:
    """Return basic inspection info for an object.

    Includes: type name, id, a few public attributes/methods, and doc (first line).
    """
    t = type(obj)
    name = getattr(t, "__name__", str(t))
    public = [m for m in dir(obj) if not m.startswith("_")][:10]
    doc = (getattr(obj, "__doc__", None) or "").strip().splitlines()[:1]
    return {
        "type": name,
        "id": id(obj),
        "public_attrs_preview": public,
        "doc_first_line": doc[0] if doc else None,
    }


def annotate_and_count(names: list[str]) -> int:
    """Example function with type hints: return number of names.

    Students: add or modify hints as you see fit.
    """
    return len(names)


def _demo() -> None:
    print("Identity vs Equality:")
    for i, (eq, same) in enumerate(identity_vs_equality_examples(), start=1):
        print(f"  Case {i}: == {eq}, is {same}")

    print("\nMutability:")
    s, s2, nums, returned = mutation_station()
    print(f"  s={s!r}, s.upper() -> {s2!r}")
    print(f"  nums after sort() -> {nums}, returned -> {returned[0]}")

    print("\nType Explorer (list example):")
    info = type_explorer([1, 2, 3])
    for k, v in info.items():
        print(f"  {k}: {v}")

    print("\nType Hints Example:")
    print("  annotate_and_count(['a','b','c']) ->", annotate_and_count(["a", "b", "c"]))


if __name__ == "__main__":
    _demo()

