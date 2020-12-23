#Fibonacci Doido em Python 

def fibonacciDoido(numeroDesejado): 
    a = 0
    b = 1

      
    if numeroDesejado == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2,numeroDesejado):
          c=a+b 
          a = b 
          b = c 
          print(c) 
    
   
         
  

numero = input("Digite o número limite para a sequência de Fibonacci ser gerada")
fibonacciDoido(int(numero))
  
