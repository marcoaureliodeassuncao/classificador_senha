import unittest
from src.classificador_senhas_marco import classificar_senha


testWeak = 0

testMedium = 1

testStrong = 2


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

	def test_classifica_senha_lower_upper_numbers(self):
		self.assertEqual(classificar_senha('RGSGFSsfgsfsf345'), testWeak)
		pass

	def test_classifica_senha_medium_case(self):
		self.assertEqual(classificar_senha('RGSGFSs@s34'), testMedium)
		pass

	def test_classifica_senha_strong_case(self):
		self.assertEqual(classificar_senha('123$%aSDamsdpoqj'), testStrong)


if __name__ == '__main__':

	unittest.main()
