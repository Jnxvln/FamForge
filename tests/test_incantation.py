import sys
from pathlib import Path
import pytest

# Ensure the package can be imported when running tests directly from the repo
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from famforge.incantation import generate_incantation


def test_generate_incantation_is_deterministic():
    seed = "84aa90ae-3417-47b5-b4e9-beee20273ba9"
    first = generate_incantation(seed)
    second = generate_incantation(seed)
    assert first == second
