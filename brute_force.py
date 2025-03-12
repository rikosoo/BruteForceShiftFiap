from random import choice
import string
import time

# Criando lista de caracteres permitidos (letras minúsculas, maiúsculas, números e símbolos)
caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Solicita a senha ao usuário
senha = input("Digite a senha que você quer encontrar: ")

# Inicializa variáveis
tentativa = ""
tentativas = 0

# Inicia a contagem do tempo
inicio = time.time()

# Loop de força bruta
while tentativa != senha:
    tentativa = "".join(choice(caracteres) for _ in range(len(senha)))
    tentativas += 1
    print(f"Tentativa {tentativas}: {tentativa}")

# Tempo total
fim = time.time()
tempo_total = fim - inicio

# Resultado final
print(f"\nSenha encontrada: {tentativa}")
print(f"Total de tentativas: {tentativas}")
print(f"Senha original: {senha}")
print(f"Tempo total: {tempo_total:.2f} segundos")

