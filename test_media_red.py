# Aluno: Bruno Henrique Soares de Freitas - 2110778
# Fase Red

import unittest

def calcular_media(nota1, nota2, nota3):
    pass  # A função ainda não foi implementada

class TestCalcularMedia(unittest.TestCase):

    def test_media_notas_normais(self):
        self.assertEqual(calcular_media(7, 8, 9), 8.0)

    def test_media_todas_as_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0.0)

    def test_media_valores_maximos(self):
        self.assertEqual(calcular_media(10, 10, 10), 10.0)

    def test_media_notas_decimais(self):
        self.assertAlmostEqual(calcular_media(7.5, 8.5, 9.0), 8.333333333333334)

    def test_media_nota_invalida(self):
        with self.assertRaises(ValueError):
            calcular_media(11, 8, 9)

if __name__ == '__main__':
    unittest.main()

# Análise dos Erros
#TypeError: unsupported operand type(s) for -: 'NoneType' and 'float': Isso indica que a função calcular_media está retornando None, o que significa que a implementação não foi realizada corretamente.

#ValueError not raised: Isso sugere que a validação das notas inválidas não está sendo executada corretamente.

#None != 8.0 e None != 0.0: Esses erros confirmam que a função não está retornando o valor esperado.