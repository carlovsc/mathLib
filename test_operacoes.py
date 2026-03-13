import pytest
from operacoes import BibliotecaArrays

@pytest.fixture
def lib():
    """Fixture para instanciar a biblioteca antes de cada teste[cite: 53]."""
    return BibliotecaArrays()

def test_max(lib):
    assert lib.max([1, 5, 3]) == 5.0
    assert lib.max([-10, -2, -5]) == -2.0

def test_min(lib):
    assert lib.min([1, 5, 3]) == 1.0
    assert lib.min([0, 100, -5]) == -5.0

def test_size(lib):
    assert lib.size([1, 2, 3, 4]) == 4
    assert lib.size([]) == 0

def test_average(lib):
    assert lib.average([10, 20, 30]) == 20.0
    assert lib.average([]) == 0.0

def test_std_dev(lib):
    # Desvio padrão de [10, 10, 10] é 0
    assert lib.std_dev([10, 10, 10]) == 0.0
    # Desvio padrão de [2, 4] -> média 3 -> sqrt(((2-3)^2 + (4-3)^2)/2) = sqrt(1) = 1
    assert lib.std_dev([2, 4]) == 1.0

def test_sort_asc(lib):
    assert lib.sort([3, 1, 2], "asc") == [1, 2, 3]

def test_sort_desc(lib):
    assert lib.sort([1, 3, 2], "desc") == [3, 2, 1]

def test_reverse(lib):
    assert lib.reverse([1, 2, 3]) == [3, 2, 1]
    assert lib.reverse([]) == []