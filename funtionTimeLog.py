import datetime

def decorator(funcao):
    def wrapper():
        a = datetime.datetime.now()
        funcao()
        b = datetime.datetime.now()
        time = b-a
        print(time)

    return wrapper

def outra_funcao():
    print ("Sou a função cheia de tralha que terá seu tempo de execução medido. Quanto será que levou?")
    print ("Lorem Ipsum?")
    print ("4 + 4 = 8?")
    print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
    print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
  #  print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
  #  print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
    print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
  #  print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
    print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
  #  print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
    print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
  #  print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")
  #  print ("Tire o comentário dessa linha para que a função leve mais tempo para ser executada")


#chamada oficial da funcao
funcaodoida = decorator(outra_funcao)
funcaodoida()
