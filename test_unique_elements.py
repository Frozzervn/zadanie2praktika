# test_unique_elements.py

import pytest
from unique_elements import unique_elements

def test_unique_elements1():
    assert unique_elements([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

def test_unique_elements2():
    assert unique_elements(['a', 'b', 'b', 'c']) == ['a', 'b', 'c']

def test_unique_elements3():
    assert unique_elements([1, 1, 1, 1, 1]) == [1]

def test_unique_elements4():
    assert unique_elements([]) == []

def test_unique_elements5():
    assert unique_elements([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unique_elements6():
    assert unique_elements([1, 2, 2]) == [1, 2,]

def test_unique_elements7():
    assert unique_elements([1.1, 1.1, 2.2, 3.3, 3.3]) == [1.1, 2.2, 3.3]

def test_unique_elements8():
    assert unique_elements([-1, -1, 2, -2, 2]) == [-2, -1, 2]

def test_unique_elements9():
    large_input = [1] * 10000 + [2] * 10000 + [3] * 10000
    assert unique_elements(large_input) == [1, 2, 3]

def test_unique_elements10():
    assert unique_elements(['apple', 'banana', 'apple', 'orange']) == ['apple', 'banana', 'orange']

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
