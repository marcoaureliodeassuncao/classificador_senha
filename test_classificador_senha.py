import unittest
from src.classificador_senhas_marco import classificar_senha


testWeak = 0

testMedium = 1

testStrong = 2

testFalse = False


class Tester(unittest.TestCase):


	def test_classifica_senha_lower_case(self):
		self.assertEqual(classificar_senha('hasiudh'), testWeak)
		pass

	def test_classifica_senha_upper_case(self):
		self.assertEqual(classificar_senha('LFSTYMWVIL'), testWeak)
		pass

	def test_classifica_senha_lower_and_upper_case(self):
		self.assertEqual(classificar_senha('RHNyOPpsDKHcG'), testWeak)
		pass

	def test_classfica_senha_numbers(self):
		self.assertEqual(classificar_senha('5641321987'), testWeak)
		pass

	def test_classifica_senha_palavra(self):
		self.assertEqual(classificar_senha('pizza'), testWeak)
		pass

	def test_classifica_senha_symbols(self):
		self.assertEqual(classificar_senha('!@##$@#$@!@$@#'),testWeak)

	def test_classifica_senha_lower_upper_numbers(self):
		self.assertEqual(classificar_senha('RGSGFSsfgsfsf345'), testWeak)
		pass

	def test_classifica_senha_medium_case(self):
		self.assertEqual(classificar_senha('RGSGFSs@s34'), testMedium)
		pass

	def test_classifica_senha_strong_case(self):
		self.assertEqual(classificar_senha('123$%aSDamsdpoqj'), testStrong)
		pass

	def test_classifica_senha_espaco(self):
		self.assertEqual(classificar_senha('tesT@ de 3spAç0'),testFalse)


if __name__ == '__main__':

	unittest.main()
