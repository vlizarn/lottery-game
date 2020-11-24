import sys #Importa o módulo de sys
import random #Importa o módulo de random

repetir = True

def lotaria_simples(valor):

    print("-----------------Escolheu a aposta simples-----------------")
    print("Quantas vezes pretende apostar: ", valor)

    #Se, número de apostas for maior e igual à 5 e menor, igual à 1.
    if valor <= 5 and valor >= 1: 

        print("------------------Número de apostas(",valor,")-------------------")

        for apostas in range(0, valor, 5):
            apostas = apostas + 1

            for i in range(valor):

                #1º grupo é a operação de chaves
                num = lambda : random.randint(1, 50)

                conjunto1A = random.sample([num(), num(), num(), num(), num()], 5)
                conjunto2A = random.sample([num(), num(), num(), num(), num()], 5)
                conjunto3A = random.sample([num(), num(), num(), num(), num()], 5)
                conjunto4A = random.sample([num(), num(), num(), num(), num()], 5)
                conjunto5A = random.sample([num(), num(), num(), num(), num()], 5)
                conjunto6A = random.sample([num(), num(), num(), num(), num()], 5)

                #2º grupo é a operação de estrelas
                num = lambda : random.randint(1, 9)

                conjunto1B = random.sample([num(), num()], 2)
                conjunto2B = random.sample([num(), num()], 2)
                conjunto3B = random.sample([num(), num()], 2)
                conjunto4B = random.sample([num(), num()], 2)
                conjunto5B = random.sample([num(), num()], 2)
                conjunto6B = random.sample([num(), num()], 2)

        #Atribuír para cada conjunto, o respectivo valor.
        valores1A = conjunto1A
        valores2A = conjunto2A
        valores3A = conjunto3A
        valores4A = conjunto4A
        valores5A = conjunto5A

        prémio1 = conjunto6A

        valores1B = conjunto1B
        valores2B = conjunto2B
        valores3B = conjunto3B
        valores4B = conjunto4B
        valores5B = conjunto5B

        prémio2 = conjunto6B

        #Se, número de apostas for igual à 1.
        if valor == 1:
            print([apostas], conjunto1A, conjunto1B)

        #Se, número de apostas for igual à 2.    
        elif valor == 2:
            print([apostas], conjunto1A, conjunto1B)
            print([apostas + 1], conjunto2A, conjunto2B)

        #Se, número de apostas for igual à 3.
        elif valor == 3:
            print([apostas], conjunto1A, conjunto1B)
            print([apostas + 1], conjunto2A, conjunto2B)
            print([apostas + 2], conjunto3A, conjunto3B)

        #Se, número de apostas for igual à 4.
        elif valor == 4:
            print([apostas], conjunto1A, conjunto1B)
            print([apostas + 1], conjunto2A, conjunto2B)
            print([apostas + 2], conjunto3A, conjunto3B)
            print([apostas + 3], conjunto4A, conjunto4B)

        #Se, número de apostas for igual à 5.
        elif valor == 5 :
            print([apostas], conjunto1A, conjunto1B)
            print([apostas + 1], conjunto2A, conjunto2B)
            print([apostas + 2], conjunto3A, conjunto3B)
            print([apostas + 3], conjunto4A, conjunto4B)
            print([apostas + 4], conjunto5A, conjunto5B)

        #Lista de todas as apostas, incluêm, números e estrelas.
        listaA = [valores1A, valores2A, valores3A, valores4A, valores5A]
        listaB = [valores1B, valores2B, valores3B, valores4B, valores5B]

        #Representação dos valores do prémio
        print("------------------Valores do prémio(",valor,")------------------")
        print("Prémio:","Números:", prémio1,"- Estrelas:", prémio2)

        for i in range(valor):
            listaA[i:i+1]
            listaB[i:i+1]

            #Se, os valores de uma determinada linha de números e estrelas são iguais aos valores do prémio, ganha.
            if prémio1 in listaA[i:i+1] and prémio2 in listaB[i:i+1]:
                print("------------------Ganhou a lotaria(",valor,")-------------------")
                print("Muitos parabêns, ganhou o prémio!")
                        
                break;

        #Se, os valores de uma determinada linha de números e estrelas são diferentes aos valores do prémio, perde.
        else:
            print("------------------Perdeu a lotaria(",valor,")-------------------")
            print("Infelizmente, não ganhou o prémio!")

    #Limite máximo de apostas.
    elif valor > 5:

        print("---------------------Limite de apostas(",valor,")---------------------")
        print("Ultrapassou, o limite máximo de apostas!")
        print("Tente, novamente para proxima.")

    #Limite mínimo de apostas.
    elif valor < 1:
        print("---------------------Limite de apostas(",valor,")---------------------")
        print("Ultrapassou, o limite mínimo de apostas!")
        print("Tente, novamente para proxima.")

    #Se, possuir ocorrência de falhas.
    else:
        print("----------------------Erro ocorrido(",valor,")------------------------")
        print("Falha na execução!")

def lotaria_multipla(valor):

        print("----------------Escolheu a aposta múltipla-----------------")
        print("Quantas vezes pretende apostar: ", valor)

        #Se, número de apostas for maior e igual à 5 e menor, igual à 1.
        if valor <= 5 and valor >= 1:

            print("------------------Número de apostas(",valor,")-------------------")

            for apostas in range(0, valor, 5):
                apostas = apostas + 1

                for i in range(valor):

                    #1º grupo é a operação de chaves
                    num = lambda : random.randint(1, 50)

                    conjunto1A = random.sample([num(), num(), num(), num(), num(), num(), num(), num(), num(), num(), num()], random.randint(5, 11))
                    conjunto2A = random.sample([num(), num(), num(), num(), num(), num(), num(), num(), num(), num(), num()], random.randint(5, 11))
                    conjunto3A = random.sample([num(), num(), num(), num(), num(), num(), num(), num(), num(), num(), num()], random.randint(5, 11))
                    conjunto4A = random.sample([num(), num(), num(), num(), num(), num(), num(), num(), num(), num(), num()], random.randint(5, 11))
                    conjunto5A = random.sample([num(), num(), num(), num(), num(), num(), num(), num(), num(), num(), num()], random.randint(5, 11))
                    conjunto6A = random.sample([num(), num(), num(), num(), num(), num(), num(), num(), num(), num(), num()], random.randint(5, 11))

                    #2º grupo é a operação de estrelas
                    num = lambda : random.randint(1, 9)

                    conjunto1B = random.sample([num(), num(), num(), num(), num()], random.randint(2, 5))
                    conjunto2B = random.sample([num(), num(), num(), num(), num()], random.randint(2, 5))
                    conjunto3B = random.sample([num(), num(), num(), num(), num()], random.randint(2, 5))
                    conjunto4B = random.sample([num(), num(), num(), num(), num()], random.randint(2, 5))
                    conjunto5B = random.sample([num(), num(), num(), num(), num()], random.randint(2, 5))
                    conjunto6B = random.sample([num(), num(), num(), num(), num()], random.randint(2, 5))

            #Atribuír para cada conjunto, o respectivo valor.
            valores1A = conjunto1A
            valores2A = conjunto2A
            valores3A = conjunto3A
            valores4A = conjunto4A
            valores5A = conjunto5A

            prémio1 = conjunto6A

            valores1B = conjunto1B
            valores2B = conjunto2B
            valores3B = conjunto3B
            valores4B = conjunto4B
            valores5B = conjunto5B

            prémio2 = conjunto6B

            #Se, número de apostas for igual à 1.
            if valor == 1:
                print([apostas], conjunto1A, conjunto1B)

            #Se, número de apostas for igual à 2.
            elif valor == 2:
                print([apostas], conjunto1A, conjunto1B)
                print([apostas + 1], conjunto2A, conjunto2B)

            #Se, número de apostas for igual à 3.
            elif valor == 3:
                print([apostas], conjunto1A, conjunto1B)
                print([apostas + 1], conjunto2A, conjunto2B)
                print([apostas + 2], conjunto3A, conjunto3B)

            #Se, número de apostas for igual à 4.
            elif valor == 4:
                print([apostas], conjunto1A, conjunto1B)
                print([apostas + 1], conjunto2A, conjunto2B)
                print([apostas + 2], conjunto3A, conjunto3B)
                print([apostas + 3], conjunto4A, conjunto4B)

            #Se, número de apostas for igual à 5.
            elif valor == 5:
                print([apostas], conjunto1A, conjunto1B)
                print([apostas + 1], conjunto2A, conjunto2B)
                print([apostas + 2], conjunto3A, conjunto3B)
                print([apostas + 3], conjunto4A, conjunto4B)
                print([apostas + 4], conjunto5A, conjunto5B)

            #Lista de todas as postas, incluêm, números e estrelas.
            listaA = [valores1A, valores2A, valores3A, valores4A, valores5A]
            listaB = [valores1B, valores2B, valores3B, valores4B, valores5B]

            #Representação dos valores do prémio
            print("------------------Valores do prémio(",valor,")------------------")
            print("Prémio:","Números:", prémio1,"- Estrelas:", prémio2)

            for i in range(valor):
                listaA[i:i+1]
                listaB[i:i+1]

                #Se, os valores de uma determinada linha de números e estrelas são iguais aos valores do prémio, ganha.
                if prémio1 in listaA[i:i+1] and prémio2 in listaB[i:i+1]:
                    print("------------------Ganhou a lotaria(",valor,")-------------------")
                    print("Muitos parabêns, ganhou o prémio!")

                    break;

            #Se, os valores de uma determinada linha de números e estrelas são diferentes aos valores do prémio, perde.
            else:
                print("------------------Perdeu a lotaria(",valor,")-------------------")
                print("Infelizmente, não ganhou o prémio!")

        #Limite máximo de apostas.
        elif valor > 5:
            print("---------------------Limite de apostas(",valor,")---------------------")
            print("Ultrapassou, o limite máximo de apostas!")
            print("Tente, novamente para proxima.")

        #Limite mínimo de apostas.
        elif valor < 1:
            print("---------------------Limite de apostas(",valor,")---------------------")
            print("Ultrapassou, o limite mínimo de apostas!")
            print("Tente, novamente para proxima.")

        #Se, possuir ocorrência de falhas.   
        else:
            print("----------------------Erro ocorrido(",valor,")------------------------")
            print("Falha na execução!")

def lotaria():

    print("\n                   Bem-vindo ao Lotaria")
    print("        Escolha o tipo de aposta que deseja realizar\n")
    print("Aposta simples (Digite 'S')\nAposta múltipla (Digite 'M')")
    print("Número de aposta(s) (1 até 5)\n")

    aposta = input("Tipo de aposta: ")
    valor = input("Número de aposta(s): ")

    valor = int(valor)

    if aposta == 'S':
        return lotaria_simples(valor)

    elif aposta == 'M':
        return lotaria_multipla(valor)

    #Se, a opção não corresponder.
    elif aposta != ' ':
        print("---------------------Aposta não existe(",aposta,")---------------------")
        print("A aposta não existe!")

    #Se, possuir ocorrência de falhas.        
    else:
        print("----------------------Erro ocorrido------------------------")
        print("Falha na execução!")

def verificar():
    modo = input("\nQuer recomeçar? ('Sim' ou 'Não')\n")

    if modo == "Sim":
        return True
    elif modo == "Não":
        return False
    else:
        return verificar()

def main():
    lotaria()

while repetir:
    try:
        main()
    except ValueError:
        print("\nErro: Introduza o valor inteiro correctamente! Tente novamente.")
    except:
        print("\nUnexpected error: ", sys.exc_info()[1])
    finally:
        repetir = verificar()

