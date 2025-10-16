"""
Module 2 — Objects and Methods Fundamentals

Complete the TODOs and run this file to see sample output.
"""

from __future__ import annotations
from typing import Any


def method_hunt(obj: Any, name_contains: str) -> list[str]:
    """Return sorted list of public attributes whose names contain the substring.

    Example: method_hunt("hello", "count") -> ["count"]
    """
    substr = name_contains.lower()
    hits = [m for m in dir(obj) if not m.startswith("_") and substr in m.lower()]
    return sorted(hits)


def split_attributes_and_methods(obj: Any) -> tuple[list[str], list[str]]:
    """Return (attributes, methods) for public names on the object.

    Heuristic: callability implies method. Attributes are non-callable.
    """
    attrs: list[str] = []
    methods: list[str] = []
    for name in dir(obj):
        if name.startswith("_"):
            continue
        value = getattr(obj, name, None)
        (methods if callable(value) else attrs).append(name)
    return sorted(attrs), sorted(methods)


def chain_reaction(text: str) -> str:
    """Demonstrate method chaining using an immutable string.

    Requirement: trim, lowercase, replace spaces with underscores.
    """
    return text.strip().lower().replace(" ", "_")


def docs_first_line(obj: Any, member: str) -> str | None:
    """Return the first line of the docstring for obj.member if available."""
    if not hasattr(obj, member):
        return None
    target = getattr(obj, member)
    doc = getattr(target, "__doc__", None)
    if not doc:
        return None
    return doc.strip().splitlines()[0]


def _demo() -> None:
    print('Method Hunt ("hello", contains=\'count\'):')
    print("  ", method_hunt("hello", "count"))

    print("\nSplit attributes/methods (datetime example):")
    import datetime as _dt
    attrs, methods = split_attributes_and_methods(_dt.datetime.now())
    print("  attrs:", attrs[:8], "...")
    print("  methods:", methods[:8], "...")

    print("\nChain Reaction:")
    print("  ", chain_reaction("  Hello World  "))

    print("\nDocs first line (str.split):")
    print("  ", docs_first_line("hello world", "split"))


if __name__ == "__main__":
    _demo()
