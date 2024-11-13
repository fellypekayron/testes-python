from calculadoraIMC import calculadoraIMC

import unittest

class TestCalculadoraIMC(unittest.TestCase):

    def setUp(self):
        self.calc = calculadoraIMC()

    def test_resultado(self):
        # Testando o resultado para magreza
        self.assertEqual(self.calc.resultado(60, 1.90), 16.62, 'magreza')

if __name__ == '__name__':
   unittest.main()            