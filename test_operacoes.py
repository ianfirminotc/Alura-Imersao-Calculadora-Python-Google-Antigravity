import unittest
from operacoes import somar, subtrair, multiplicar, dividir, porcentagem

class TestOperacoes(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-2, -3), -5)
        self.assertAlmostEqual(somar(0.1, 0.2), 0.3, places=7)

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
        # Teste de divisão por zero:
        self.assertEqual(dividir(10, 0), "Erro: Não é possível dividir por zero!")

    def test_porcentagem(self):
        self.assertEqual(porcentagem(200, 15), 30.0)
        self.assertEqual(porcentagem(50, 10), 5.0)
        self.assertEqual(porcentagem(100, 0), 0.0)

if __name__ == '__main__':
    unittest.main()
