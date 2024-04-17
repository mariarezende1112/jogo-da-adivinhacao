import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#definindo o numero secreto
numeroSecreto = round(random.random()*1,101)
#print(numeroSecreto)

rodada = 1
#definindi numero de de tentativas
numerotentativas = 10

print("Qual o nível de dificuldade?")
print("(1)-Fácil, (2)-Médio, (3)-Difícil")

nível = int(input('Defina '))
while(rodada <= numerotentativas):
    print('tentativas',rodada,'de',numerotentativas)
    

#recebendo o chute do jogador
    chuteString= input('Digite um numero entre 1 a 100:')
    chute = int(chuteString)

    #print('Você digitou', chuteString)


#declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Você errou! O numero secreto é um numero menor')
    else:
        print('Você errou! O numero secreto é um numero maior')    
    #numerotentativas = numerotentativas - 1
    rodada = rodada + 1    