import pytest
class Calculadora:
   def __init__(self):
       pass

   def suma(self, num_a: int, num_b: int):
       return num_a + num_b

   def resta(self, num_a: int, num_b: int):
       return num_a - num_b

   def multiplicacion(self, num_a: int, num_b: int):
       return num_a * num_b

   def division(self, num_a: int, num_b: int):
       return num_a / num_b

def test_suma_valid_input():
    calc = Calculadora()
    result = calc.suma(2, 2)
    assert result == 4, "La suma de 2+2 debe ser igual a 4"

def test_resta_valid_input():
    calc = Calculadora()
    result = calc.resta(2, 2)
    assert result == 0, "La resta de 2 - 2 debe ser igual 0"

def test_multiplicacion_valid_input():
    calc = Calculadora()
    result = calc.multiplicacion(2, 5)
    assert result == 10, "La multiplicacion de 2 * 2 debe ser igual a 4"

def test_division_valid_input():
    calc = Calculadora()
    result = calc.division(5, 2)
    assert result == 2.5, "La division de 4/2 debe ser igual a 2"