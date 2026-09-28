"""Convenience launcher for the standalone OMSI spline generator."""

from pathlib import Path
from runpy import run_path
import sys


tool_dir = Path(__file__).with_name("tool")
sys.path.insert(0, str(tool_dir))
run_path(tool_dir / "main.py", run_name="__main__")
