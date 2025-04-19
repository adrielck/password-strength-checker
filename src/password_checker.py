import re
import string

# Lista simulada de senhas comuns (em um projeto real, use um banco maior)
COMMON_PASSWORDS = ["password123", "admin123", "12345678", "qwerty"]

def check_password_strength(password):
    """
    Verifica a força de uma senha com base em critérios de segurança.
    Retorna uma tupla (força, mensagens de feedback).
    """
    if not password:
        return "Fraca", ["A senha não pode ser vazia."]

    feedback = []
    score = 0

    # Critério 1: Comprimento mínimo
    if len(password) < 8:
        feedback.append("A senha deve ter pelo menos 8 caracteres.")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    # Critério 2: Letras maiúsculas
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Inclua pelo menos uma letra maiúscula.")

    # Critério 3: Letras minúsculas
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Inclua pelo menos uma letra minúscula.")

    # Critério 4: Números
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Inclua pelo menos um número.")

    # Critério 5: Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Inclua pelo menos um caractere especial (ex.: !, @, #).")

    # Critério 6: Verificar senhas comuns
    if password.lower() in [p.lower() for p in COMMON_PASSWORDS]:
        feedback.append("A senha está em uma lista de senhas comuns. Escolha outra.")
        return "Fraca", feedback

    # Determinar força com base no score
    if score >= 6:
        strength = "Forte"
        if not feedback:
            feedback.append("Senha excelente!")
    elif score >= 4:
        strength = "Moderada"
        feedback.append("A senha é aceitável, mas pode ser melhorada.")
    else:
        strength = "Fraca"
        feedback.append("A senha é muito fraca. Considere adicionar mais variedade.")

    return strength, feedback

def main():
    print("=== Verificador de Força de Senha ===")
    while True:
        password = input("Digite uma senha (ou 'sair' para encerrar): ")
        if password.lower() == "sair":
            break
        strength, feedback = check_password_strength(password)
        print(f"\nForça da senha: {strength}")
        print("Feedback:")
        for msg in feedback:
            print(f"- {msg}")
        print()

if __name__ == "__main__":
    main()