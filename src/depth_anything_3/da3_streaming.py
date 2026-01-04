"""Shim module to import DA3-Streaming from the vendor checkout."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType


def _load_da3_streaming() -> ModuleType:
    repo_root = Path(__file__).resolve().parents[2]
    da3_root = repo_root / "da3_streaming"
    if str(da3_root) not in sys.path:
        sys.path.insert(0, str(da3_root))
    return importlib.import_module("da3_streaming")


_module = _load_da3_streaming()

DA3_Streaming = getattr(_module, "DA3_Streaming")

__all__ = ["DA3_Streaming"]
