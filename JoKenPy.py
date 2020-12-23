import random

moves = ['Pedra','Papel','Tesoura']
keep_playing = True

pscore,cscore = 0, 0


while keep_playing == True:
    cmove = random.choice(moves)
    print("Jogue contra a IA no jogo mais difícil do mundo")
    pmove = input("Escolha um movimento: Pedra, Papel ou Tesoura?").capitalize()
    print("VOCÊ ESCOLHEU", pmove)

      ## LÓGICA DA IA MAIS DIFÍCIL DO MUNDO 
      
      #if pmove == 'Pedra':
        #cmove = 'Tesoura'
      #elif pmove =='Tesoura:
        #cmove= 'Papel'
      #else:
        #cmove ='Pedra'
   
    print("A IA ESCOLHEU: ", cmove)
    #Logic to game    
    if cmove == pmove:
        print("EMPATE TÉCNICO")
        print(pscore, cscore)

    elif pmove == "Pedra" and cmove == "Tesoura":
        print("VOCÊ VENCEU A MÁQUINA! PARABÉNS!")
        pscore+=10
        print(pscore, cscore)

    elif pmove == "Pedra" and cmove == "Papel":
        print("A IA VENCEU VOCÊ! HUMANO INFERIOR! Treine mais!")
        cscore+=10
        print(pscore, cscore)

    elif cmove == "Papel" and cmove == "Pedra":
        print("VOCÊ VENCEU A MÁQUINA! PARABÉNS!")
        pscore+=10
        print(pscore, cscore)

    elif pmove == "Papel" and cmove == "Tesoura":
        print("A IA VENCEU VOCÊ! HUMANO INFERIOR! Treine mais!")
        cscore+=10
        print(pscore, cscore)

    elif pmove == "Tesoura" and cmove == "Papel":
        print("VOCÊ VENCEU A MÁQUINA! PARABÉNS!")
        pscore+=10
        print(pscore, cscore)

    elif pmove == "Tesoura" and cmove == "Pedra":
        print("A IA VENCEU VOCÊ! HUMANO INFERIOR! Treine mais!")
        cscore+=10
        print(pscore, cscore)

    # Reiniciar?
    play_again = input("Quer Continuar? Tenha consciência que a IA é muito boa. Digite Sim ou S para jogar ou R para Reiniciar com placar Zerado")
    
    if play_again.lower().startswith('s'):
      keep_playing = True

    if play_again.lower().startswith('r'):
      cmove,pmove = 0 , 0
      keep_playing = True
    else:
      keep_playing = False
