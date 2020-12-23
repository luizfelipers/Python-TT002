#Função
def inverteFrase(x):
  return x[::-1]


#Teste
teste = inverteFrase("Socorram-me, subi no ônibus em Marrocos!")
print(teste)

#Entrada
frase = inverteFrase(input('Digite uma frase para ser invertida'))
#Saída
print(frase)
