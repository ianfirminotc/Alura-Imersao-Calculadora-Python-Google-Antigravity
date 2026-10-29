import unittest
from calculadora import somar, subtrair, multiplicar, dividir, porcentagem

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-2, -3), -5)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(0, 5), -5)
        self.assertEqual(subtrair(-3, -2), -1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(5, 2), 2.5)
        # Teste do caso especial: divisão por zero
        self.assertEqual(dividir(10, 0), "Erro: Não é possível dividir por zero!")

    def test_porcentagem(self):
        self.assertEqual(porcentagem(200, 15), 30.0)
        self.assertEqual(porcentagem(50, 10), 5.0)
        self.assertEqual(porcentagem(100, 0), 0.0)

if __name__ == '__main__':
    unittest.main()
