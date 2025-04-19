Password Strength Checker
Um projeto de cibersegurança que verifica a força de senhas com base em critérios de segurança, como comprimento, uso de letras maiúsculas/minúsculas, números e caracteres especiais. Inclui verificação contra senhas comuns e fornece feedback detalhado.
Funcionalidades

Avalia a força da senha (Fraca, Moderada, Forte).
Verifica critérios de segurança:
Comprimento mínimo de 8 caracteres.
Presença de letras maiúsculas, minúsculas, números e caracteres especiais.
Não estar em uma lista de senhas comuns.


Fornece feedback para melhorar a senha.
Inclui testes unitários para garantir robustez.

Tecnologias Utilizadas

Python 3.8+: Linguagem principal.
Bibliotecas: re (expressões regulares), unittest (testes).
VS Code: Ambiente de desenvolvimento.

Como Usar
Pré-requisitos

Python 3.8 ou superior instalado.
Visual Studio Code (recomendado).

Instalação

Clone o repositório:
git clone https://github.com/adrielck/password-strength-checker.git
cd password-strength-checker


(Opcional) Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Execute o programa:
python src/password_checker.py


Para rodar os testes:
python -m unittest tests/test_password_checker.py



Exemplo de Uso
=== Verificador de Força de Senha ===
Digite uma senha (ou 'sair' para encerrar): P@ssw0rd!2023
Força da senha: Forte
Feedback:
- Senha excelente!




