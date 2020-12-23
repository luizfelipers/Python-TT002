def remove_duplicatas(lista):
  #Transforma a lista recebida num dicionário para remover os elementos duplicados, e re-transforma numa lista
  return list(dict.fromkeys(lista))


#Teste
#Criação de uma lista com elementos que se repetem
testelista=remove_duplicatas(["1", "2", "3", "2", "1","5","3","7","1","4","21","99","4","outro", "1", "2", "3", "2", "6", "1", "2", "3", "2","8"])
print(testelista)

#Entrada
novaLista = remove_duplicatas(input("Digite os elementos da lista separados por espaço (Digite quantos quiser).").split())
print(novaLista)
