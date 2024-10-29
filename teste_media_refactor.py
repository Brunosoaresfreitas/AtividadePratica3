# Aluno: Bruno Henrique Soares de Freitas - 2110778
# Fase Refactor

import unittest

def calcular_media(nota1, nota2, nota3):
    # Verifica se as notas estão dentro do intervalo permitido
    for nota in (nota1, nota2, nota3):
        if nota < 0 or nota > 10:
            raise ValueError("As notas devem estar entre 0 e 10.")
    return (nota1 + nota2 + nota3) / 3

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

# Resultado após execução: Ran 5 tests in 0.001s