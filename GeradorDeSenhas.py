import random  # importa a biblioteca random

senha = "" #define a senha como uma string sem nada

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&*?çÇ" # todos os caracteres para combinação

for digito in range (15): # declara que a senha terá 15 caracteres
    senhaaleatoria = random.choice(letras)
    senha += senhaaleatoria # joga a senha gerada na string vazia
print("-" * 25)
print(senha)
print("-" * 25)
print("Esta é sua senha.")
