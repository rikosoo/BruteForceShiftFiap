# 🔓 Brute Force Password Cracker

Este é um projeto simples que simula um ataque de **força bruta** para encontrar uma senha digitada pelo usuário. Ele gera tentativas aleatórias até encontrar a senha correta e mede o tempo necessário para isso.

---

## 📜 Como funciona?
1. O usuário insere uma senha.
2. O programa gera combinações aleatórias de caracteres e compara com a senha fornecida.
3. O processo continua até que a senha seja encontrada.
4. O número de tentativas e o tempo total são exibidos no final.

⚠ **Aviso:** Este código é apenas para fins educacionais. **Não utilize para atividades mal-intencionadas.**

---

## 🚀 Melhorias implementadas
✅ **Suporte a letras maiúsculas, minúsculas, números e caracteres especiais**  
✅ **Uso de `choice()` e `.join()` para otimizar a geração de senhas**  
✅ **Adição de um contador de tentativas**  
✅ **Medição do tempo total de execução com `time.time()`**  
✅ **Código limpo e organizado**  

---

## 🖥️ Como rodar o programa?
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/rikosoo/brute-force-password.git

## Entre na pasta do projeto:
cd brute-force-password

## Execute o codigo
python brute_force.py

## Exemplo de execução
Digite a senha que você quer encontrar: A1b!
Tentativa 1: 3$x@
Tentativa 2: R7t&
Tentativa 3: A1b!
Senha encontrada: A1b!
Total de tentativas: 3
Tempo total: 0.01 segundos


## Tecnologias utilizadas
Python 3
Módulo random para geração de senhas
Módulo string para caracteres permitidos
Módulo time para medição de tempo

## Considerações sobre segurança
Senhas curtas e simples podem ser quebradas em segundos.
Senhas longas e complexas aumentam drasticamente o tempo necessário.
Use sempre autenticação de dois fatores (2FA) para mais segurança.

