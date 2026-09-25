import random
import pytest

@pytest.fixture
def max_rolls(monkeypatch):
    monkeypatch.setattr(random, "randint", lambda a, b: b)

@pytest.fixture
def min_rolls(monkeypatch):
    monkeypatch.setattr(random, "randint", lambda a, b: a)

@pytest.fixture
def avg_rolls(monkeypatch):
    monkeypatch.setattr(random, "randint", lambda a, b: b/2)