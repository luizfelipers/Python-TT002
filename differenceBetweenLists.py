def difListas(lista1,lista2):
  
    diferenca= list(set(lista1) ^ set(lista2))
    if len(diferenca) == 0:
      print("Não existem diferenças")
    else:
      print(diferenca)


l1 = input("Digite numeros separados por espaco").split()
l2 = input("Digite numeros separados por espaco").split()



l3 = difListas(l1,l2)
print(l3)


