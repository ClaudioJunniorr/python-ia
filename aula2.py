'''
isso aqui é um comentário de várias linhas.
'''
# comentário de linha única

'''
Criar um sisteminha para receber o nome, idade, peso, altura
Converter a idade para reeber somente numeros inteiros
imprimir os tipos de dados
imprimir todas as informações concatenadas usando f string
'''
#number=30
#number=str(number)
# conversão direta de variável. Converteu int para string
nome=input(" Digite seu nome: ")
idade=int(input(" Sua idade: "))
peso=float(input(" Seu peso: "))
altura=float(input(" Sua altura: "))
print(f" Meu nome é {nome}, tenho {idade} anos de idade, estou pesando {peso} quilos e tenho {altura}")
