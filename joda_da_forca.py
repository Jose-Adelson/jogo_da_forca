from palavras import palavras
import random

#Selecionar palavras
def selecionar_palavras():
    palavra = random.choice(palavras)
    return palavra.upper()

#iniciar o jogo
def jogar(palavra):
    composicao_palavra = "_" * len(palavra)
    adivinhou = False
    letras_vazias = []
    letras_utilizadas = []
    tentativas = 6

    #Boas vindas ao usuário!
    print("Olá! Vamos jogar forca!")
    print("Essa é a palavra %s" %composicao_palavra)
    print(exibir_forca(tentativas))
   
    print(composicao_palavra)

    #Enquanto houver chances para advinhar
    while not adivinhou and tentativas > 0:
        tentativa = input("Digite uma letra ou palavra se souber: ").upper()
        print(tentativa)

    #Tentativa de uma letra
    #Verficar se a letra já foi utilizada
        if len(tentativa) == 1 and tentativa.isalpha():
    #verificar se a letra já foi utlizada
       
            if tentativa in letras_utilizadas:
                print("Você  já utilizou esta letra antes: %s" %tentativa)
        #Verificar se a tentativa não está na palavra
            elif tentativa not in palavra:
                print("A letra %s não está na palavra!" %tentativa)
                tentativas -= 1
                letras_utilizadas.append(tentativa)

        #Quando a letra está na palavra
            else:
                print("Parabéns! A letra %s está na palavra!" %tentativa)
                letras_utilizadas.append(tentativa)
        #Transformar a palavra em uma lista
                palavra_lista = list(composicao_palavra)
        #Onde pode substituir o anderline por uma letra dita
                indice = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indice:
                    palavra_lista[indice] = tentativa
                
                composicao_palavra = "".join(palavra_lista)
                
                print(composicao_palavra)

                if "_" not in composicao_palavra:
                    adivinhou = True

        #Quando o usuário tentar adivinahr a palavra toda:
        
        elif len(tentativa) == len(palavra) and tentativa.isalpha():

            #Palavra já utilizada
            if tentativa in letras_utilizadas:
                print("Você já tentou usar essa palavra %s" %letras_utilizadas)
            
            #Palavra errada
            elif tentativa != palavra:
                print("A tentativa %s está errada!"%letras_utilizadas)
                tentativas =- 1
                letras_utilizadas.append(tentativa)

            #Palavra correta
            elif tentativa == palavra:
                adivinhou = True
                composicao_palavra = palavra
                print("Parábens você acertou a palavra %s!" %palavra )     

        #tentativa invalida
        else:
            print("Tentativa inválida, tente novamente!")

        #Exibir o status do jogo
        print(exibir_forca(tentativas))
        print(composicao_palavra)
        
    #Finalizar o jogo se o jogador acertou ou perdeu todas as tentativas!    
    if adivinhou:
        print("Parabéns! Você acertou a palavra!")
    else:
        print("Que pena! Você não acertou a palavra e a palavra era %s" %palavra)

#status do jogo
def exibir_forca(tentativas):
    estagios=[#Fim de jogo! 
    """
    _ _ _ 
    |    |
    |    O
    |   /|\ 
    |   / \ 

    """,
    #Falta 01 tentativa
    """
    _ _ _ 
    |    |
    |    O
    |   /|\ 
    |   / 

    """,
    #Falta 02 tentativas
    """
    _ _ _ 
    |    |
    |    O
    |   /|\ 
    |    

    """,
    #Falta 03 tentativas
    """
    _ _ _ 
    |    |
    |    O
    |   /|
    |    

    """,
    #Falta 04 tentativas
    """
    _ _ _ 
    |    |
    |    O
    |    |
    |    

    """,
    #Falta 05 tentativas
    """
    _ _ _ 
    |    |
    |    O
    |   
    |    

    """,
    #Estado inicial
    """
    _ _ _ 
    |    |
    |    
    |   
    |    

    """]
    return estagios[tentativas]

#Iniciar jogo e continuação
def iniciar ():
    palavra = selecionar_palavras()
    jogar(palavra)
    #Se o usuário querer cntinuar jogando
    while input("Quer jogar novamente? S/N").upper() == "S":
     palavra = selecionar_palavras()
     jogar(palavra)


iniciar()

