# Password Strength Checker  
### Um projeto de cibersegurança que verifica a força de senhas com base em critérios de segurança, como comprimento, uso de letras maiúsculas/minúsculas, números e caracteres especiais. Inclui verificação contra senhas comuns e fornece feedback detalhado.
Funcionalidades

Avalia a força da senha (Fraca, Moderada, Forte).
Verifica critérios de segurança:
Comprimento mínimo de 8 caracteres.
Presença de letras maiúsculas, minúsculas, números e caracteres especiais.
Não estar em uma lista de senhas comuns.

 Fornece feedback para melhorar a senha.
  Inclui testes unitários para garantir robustez.

- Tecnologias Utilizadas
  
  Python 3.8+: Linguagem principal.
  Bibliotecas: re (expressões regulares), unittest (testes).
  VS Code: Ambiente de desenvolvimento.

- Instalação

 ```bash
  git clone https://github.com/adrielck/password-strength-checker.git
 ```
 ```bash
  cd password-strength-checker
 ```

(Opcional) Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Execute o script:
 ```bash
python src/password_checker.py
 ```


Para rodar os testes:
```bash
python -m unittest tests/test_password_checker.py
 ```

Exemplo de Uso
```bash
=== Verificador de Força de Senha ===
Digite uma senha (ou 'sair' para encerrar): P@ssw0rd!2023
Força da senha: Forte
Feedback:
 Senha excelente!
```



