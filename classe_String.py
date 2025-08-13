texto = "Python é Incrível"

print ("1. Alterar letras (case)\n")

print(texto.lower()) # "python é incrível" - tudo minúsculo
print(texto.upper()) # "PYTHON É INCRÍVEL" - tudo maiúsculo
print(texto.title())  #"Python É Incrível" - primeira letra maiúscula de cada palavra
print(texto.capitalize()) # "Python é incrível" - só a primeira maiúscula
print(texto.swapcase()) # "pYTHON é iNCRÍVEL" - inverte maiúsculas/minúsculas

print ( "2. Remover espaços e caracteres\n")

texto = "  olá mundo"

print(texto.strip()) # "Olá mundo" Remove os espaços dos dois lados
print(texto.lstrip()) #  "Olá mundo" Remove da esquerda
print(texto.rstrip()) # "   Olá mundo!" - remove da direita
print("...abc...".strip (".")) # "abc" - remove pontos

print ("3. Buscar e verificar conteúdo\n")

texto = "Programar é divertido"
print(texto.startswith("Programar")) #true
print(texto.endswith("divertido")) # true
print(texto.find("Python"))  # (posição da palavra)
#print(texto.index("Python")) # (igual ao find, mas erro se não achar)
print(texto.count("e")) # quantas vezes o 'e' aparece

print ("4. Testes de tipo de string\n")

print("123".isdigit()) # Só número
print("abc".isalpha()) # Só letras
print("abc123".isalnum()) # letras e números
print("python".islower()) # tudo minúsculo
print("PYTHON".isupper()) # tudo maísculo
print(" ".isspace()) # só espaços

print("5. Substituir e dividir")

texto = "gato, cachorro, passaro"

print(texto.replace("gato","tigre")) # troca a palavra
print(texto.split(",")) # divide em listas
print("_" .jopin(["a", "b", "c"])) # Une lista com traços

print("6. Formatação")

nome = "Maria Eduarda"
idade = 30

print(f"Meu nome é {nome} e tenho {idade} anos") # f-string
print("Meu nome é {} e tenho {} anos".format(nome, idade))
print("R$ {:.2f}".format(1234.5678)) # 2 casas decimais --> "R$ 1234.57"

print("Python".center(20, "_")) # centaliza "-------Python-------"
print("Python".ljust(10, ".")) # à esquerda -> "Python...."
print("Python".rjust(10, ".")) # à direita  -> "....Python"
print("olá". encode()) # b'ol\xc3\xa1' (bytes)
print(b"ol\xc3\xa1".decode) # "olá"