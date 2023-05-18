
def es_par(num_a: int, num_b: int) -> bool:
    if num_a % 2 == 0 and num_b % 2 == 0:
        return True
    else:
        return False

def test_positive():
    result = es_par(4, 2)
    assert result, "4  y 2 son pares"

def test_negativo():
    result = es_par(5, 3)
    assert not result, "3 no es un num par"