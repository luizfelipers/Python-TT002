
#list = input("Digite numeros separados por espaço").split()

def parOuImpar(lista):
  
  #Separa os elementos da string pelo espaço, e atualiza a formatação na própria variável recebida por parâmetro
  lista = lista.split()
  
  #list comprehension que percorre todos os elementos string da lista recebida por parâmetro e os transforma em números inteiros
  list = ["Even" if i%2==0 else "odd" for i  in map(int,lista)] 
  #Print do resultado
  print(list)

#teste
#teste = parOuImpar('1 2 3 4 5 6 7 8 9')

#Função ParOuImpar sendo chamada a partir do Input do usuário
agoraVai = parOuImpar(input('Digite uma sequência de números, separados por espaço'))
