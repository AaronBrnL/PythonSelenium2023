import pytest


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo


class TestCuentaBancaria:

    def setup_method(self):
        self.cuenta = CuentaBancaria("Aaron", 100)

    def test_retirar(self):
        self.cuenta.retirar(80)
        assert self.cuenta.consultar_saldo() == 20, "El saldo debe ser 20 despues de retirar 80"

    def test_depositar(self):
        self.cuenta.depositar(50)
        assert self.cuenta.consultar_saldo() == 150, "El saldo debe ser 150 despues de depositar 50"

    def test_saldo_insuficiente(self):
        with pytest.raises(ValueError) as exc_info:
            self.cuenta.retirar(1000)