import unittest
from src.password_checker import check_password_strength

class TestPasswordChecker(unittest.TestCase):
    def test_empty_password(self):
        strength, feedback = check_password_strength("")
        self.assertEqual(strength, "Fraca")
        self.assertIn("A senha não pode ser vazia.", feedback)

    def test_common_password(self):
        strength, feedback = check_password_strength("password123")
        self.assertEqual(strength, "Fraca")
        self.assertIn("A senha está em uma lista de senhas comuns.", feedback)

    def test_strong_password(self):
        strength, feedback = check_password_strength("P@ssw0rd!2023")
        self.assertEqual(strength, "Forte")
        self.assertIn("Senha excelente!", feedback)

    def test_moderate_password(self):
        strength, feedback = check_password_strength("Pass123")
        self.assertEqual(strength, "Moderada")
        self.assertIn("A senha é aceitável, mas pode ser melhorada.", feedback)

    def test_weak_password(self):
        strength, feedback = check_password_strength("pass")
        self.assertEqual(strength, "Fraca")
        self.assertIn("A senha deve ter pelo menos 8 caracteres.", feedback)

if __name__ == "__main__":
    unittest.main()
