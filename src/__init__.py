"""
Werkwoorden.src package

Entry point for CLI usage. Exposes main() so the package can be driven from a module runner.
"""

from __future__ import annotations

from typing import Optional, Sequence

__all__ = ["main"]
__version__ = "0.1.0"


def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    Package entry point that starts the interactive trainer session.
    Returns a conventional process exit code (0 on success).
    """
    try:
        # Lazy import to avoid side effects on package import.
        from .main import run_session
    except Exception as exc:
        print("Kon de applicatie niet starten: import van '.main' mislukte.")
        print(f"Fout: {exc}")
        return 1

    try:
        run_session()
        return 0
    except KeyboardInterrupt:
        print("\nAfgebroken.")
        return 130


if __name__ == "__main__":
    import sys

    sys.exit(main())