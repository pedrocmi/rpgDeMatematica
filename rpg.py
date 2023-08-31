import random
import os
import time

#FUNÇÃO PARA LIMPAR O TERMINAL DO SISTEMA
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#DADOS
def dado(lados):
    return random.randint(1,lados)

#ATAQUE
def ataque():
    global dano
    if classe == 'Guerreiro':
        dano = dado(8) + dado(20) + atributoFor - atributoCon / 2
        return
    if classe == 'Mago':
        dano = dado(8) + dado(20) + atributoCon - atributoDes / 2
        return
    if classe == 'Ladrão':
        dano = dado(8) + dado(20) + atributoDes - atributoFor / 2
        return

#QUESTAO_ATAQUE
def questaoAtaque():
    print(f"O seu dano foi {dano} e a vida atual do inimigo é {vidaDoInimigo}. Digite a vida do inimigo após receber dano para atacar com sucesso.")
    resposta = float(input("Nova vida do inimigo: "))
    if resposta == vidaDoInimigo - dano:
        return True
    else:
        return False

#CURAR
def curar():
    global cura
    cura = dado(8) + dado(20) + atributoCon
    return

#QUESTAO_CURA
def questaoCura():
    print(f"A sua vida atual é {vida} e a cura foi de {cura}. Digite a sua vida após se curar para realizar a ação com sucesso.")
    resposta = float(input("Sua nova vida: "))
    if resposta == vida + cura:
        return True
    else:
        return False

#BATALHA
def batalha(vidaInimigo, armaduraInimigo, vida):
    global vidaDoInimigo
    vidaDoInimigo = vidaInimigo
    time.sleep(2)
    print('\nBATALHA!\n')
    while True:
        print('O que você irá fazer?\n1 - Atacar\n2 - Desviar')
        acao = input('Insira o número da ação: ')
        try:
            cls()
            acao = int(acao)
            if acao == 1:
                print('Você sacou a sua arma, ', item, ', e lançou um poderoso ataque contra o inimigo!', sep='')
                chanceErro = dado(10) + atributoDes
                if chanceErro > 7:
                    ataque()
                    if dano >= armaduraInimigo:
                        if questaoAtaque():
                            chanceDesvioInimigo = dado(20)
                            if chanceDesvioInimigo != 1:
                                vidaInimigo = vidaInimigo - dano
                                if vidaInimigo > 0:
                                    print('Seu ataque causou ', dano, ' de dano. O inimigo está com ', vidaInimigo, ' de vida.', sep='')
                                else:
                                    print('Seu ataque causou ', dano, ' de dano. Você derrotou o inimigo!', sep='')
                                    break
                            else:
                                print('O inimigo desviou do seu ataque!')
                        else:
                            print("Resposta incorreta! Seu ataque não funcionou!")
                    else:
                        print('Seu ataque não foi forte o suficiente.')
                else:
                    print('Você errou seu ataque!')
                chanceErroInimigo = dado(10) + 5
                if chanceErroInimigo > 7:
                    ataqueInimigo = dado(8) + dado(20) + 5
                    if ataqueInimigo >= armadura:
                        vida = vida - ataqueInimigo
                        if vida > 0:
                            print('O ataque inimigo causou ', ataqueInimigo, ' de dano. Você está com ', vida, ' de vida.', sep='')
                        elif vida <=0:
                            print('O ataque inimigo causou ', ataqueInimigo, ' de dano. Você foi derrotado.', sep='')
                            break
                    else:
                        print('O ataque inimigo não foi forte o suficiente.')
                else:
                    print('O inimigo errou o ataque!')
            elif acao == 2:
                chanceDesvio = dado(10) + atributoDes
                if chanceDesvio > 7:
                    print('Você desviou do ataque inimigo!')
                    if input('Você deseja se curar?\n1 - Sim\n2 - Não\nInsira o número da sua escolha: ') == '1':
                        if atributoCon > 0:
                            if vida < vidaInicial:
                                curar()
                                if questaoCura():
                                    vida = vida + cura
                                    if vida > vidaInicial:
                                        vida = vidaInicial
                                    print('Você curou ', cura, ' de vida com sucesso.', sep='')
                                else:
                                    print("Resposta incorreta! Sua cura não funcionou!")
                            else:
                                print('Você não pode se curar porque sua vida já está no máximo.')
                        else:
                            print('Você não pode se curar porque seu atributo de Constituição é pequeno demais.')
                else:
                    print('Você não conseguiu desviar.')
                    chanceErroInimigo = dado(10) + 5
                    if chanceErroInimigo > 7:
                        ataqueInimigo = dado(8) + dado(20) + 5
                        if ataqueInimigo >= armadura/2:
                            vida = vida - ataqueInimigo
                            if vida > 0:
                                print('O ataque inimigo causou ', ataqueInimigo, ' de dano. Você está com ', vida, ' de vida.', sep='')
                            elif vida <= 0:
                                print('O ataque inimigo causou ', ataqueInimigo, ' de dano. Você foi derrotado.', sep='')
                                break
                        else:
                            print('O ataque inimigo não foi forte o suficiente.')
                    else:
                        print('O inimigo errou o ataque!')
            else:
                print('Essa opção não é válida, tente novamente.')
        except:
            print('Essa opção não é válida, tente novamente.')

#BOAS VINDAS
cls()
print('Seja bem vindo ao RPG!')

#NOME
nome = input('Qual o nome do seu personagem? ')

#CLASSES
print('Qual a sua classe?\n1 - Guerreiro\n2 - Mago\n3 - Ladrão')

while True:
    classe = input('Insira o número da classe: ')
    try:
        classe = int(classe)
        if classe == 1:
            classe = 'Guerreiro'
            item = 'Espada grande'
            nomeArmadura = 'Armadura pesada'
            cls()
            break
        elif classe == 2:
            classe = 'Mago'
            item = 'Cajado mágico'
            nomeArmadura = 'Armadura leve'
            cls()
            break
        elif classe == 3:
            classe = 'Ladrão'
            item = 'Adagas duplas'
            nomeArmadura = 'Nenhuma'
            cls()
            break
        else:
            print('Essa opção não é válida, tente novamente.')
    except:
        print('Essa opção não é válida, tente novamente.')

#ATRIBUTOS
print('Você escolheu a classe ', classe, '. Agora, você escolherá o valor de seus atributos!', sep='')
print('Você tem 15 pontos e terá que dividi-los entre FORÇA, CONSTITUIÇÃO e DESTREZA!')
print('Seus atributos mudam dependendo da classe que você escolhe.') 
print('O Guerreiro tem mais força, o Mago, Constituição, e o Ladrão, Destreza.')
print('Caso sobrem pontos, eles serão automaticamente colocados no atributo aleatório.')
while True:
    pontos = 15
    atributoFor = input('Valor da sua força: ')
    try:
        atributoFor = int(atributoFor)
        if pontos - atributoFor >= 0:
            pontos = pontos - atributoFor
            break
        else:
            print('Pontos insuficientes!')
    except:
        print('Essa opção não é válida, tente novamente.')
while True:
    print('Você tem ', pontos, ' ponto(s) sobrando.', sep='')
    try:
        atributoCon = input('Valor da sua constituição: ')
        atributoCon = int(atributoCon)
        if pontos >= 0:
            if pontos - atributoCon >= 0:
                pontos = pontos - atributoCon
                break
            else:
                print('Pontos insuficientes!')
        else:
            print('Você não tem mais pontos!')
    except:
        print('Essa opção não é válida, tente novamente.')
while True:
    print('Você tem ', pontos, ' ponto(s) sobrando.', sep='')
    try:
        atributoDes = input('Valor da sua destreza: ')
        atributoDes = int(atributoDes)
        if pontos >= 0:
            if pontos - atributoDes >= 0:
                pontos = pontos - atributoDes
                break
            else:
                print('Pontos insuficientes!')
        else:
            print('Você não tem mais pontos!')
    except:
        print('Essa opção não é válida, tente novamente.')
if pontos > 0:
    pontosSobra = random.randint(1,3)
    if pontosSobra == 1:
        atributoFor = atributoFor + pontos
        print('Sobraram ', pontos, ' pontos. Eles serão adicionados no atributo Força.', sep='')
    elif pontosSobra == 2:
        atributoCon = atributoCon + pontos
        print('Sobraram ', pontos, ' pontos. Eles serão adicionados no atributo Constituição.', sep='')
    else:
        atributoDes = atributoDes + pontos
        print('Sobraram ', pontos, ' pontos. Eles serão adicionados no atributo Destreza.', sep='')

#VIDA + ARMADURA
vidaInicial = 100 + atributoCon * 5
vida = vidaInicial
match classe:
    case 'Guerreiro':
        atributoFor = atributoFor + 5
        armadura = 16
    case 'Mago':
        atributoCon = atributoCon + 5
        armadura = 11 + atributoDes
    case 'Ladrão':
        atributoDes = atributoDes + 5
        armadura = 0

#FICHA
cls()
print('Ficha do personagem:')
print('- Nome: ', nome, sep='')
print('- Classe: ', classe, sep='')
print('- Vida: ', vida, sep='')
print('- Armadura: ', nomeArmadura, ' (', armadura, ')', sep='')
print('- Item: ', item, sep='')
print('- Força: ', atributoFor, sep='')
print('- Constituição: ', atributoCon, sep='')
print('- Destreza: ', atributoDes, '\n', sep='')

#O JOGO
jogar = input('Pressione ENTER para jogar.')
cls()
dano = 0

for i in range(10):
    time.sleep(0.0625)
    print('-', end='')
print()

print('  ', end='')
for i in 'O JOGO':
    time.sleep(0.125)
    print(i, end='')
print()

for i in range(10):
    time.sleep(0.0625)
    print('-', end='')
print()

#Os inimigos têm os atributos divididos igualmente, ou seja, 5 pontos em cada atributo.
#Cada inimigo tem uma classe e a forma como elas funcionam é igual às classes do personagem.
#Isso explica o valor da vida e da armadura inimiga.
time.sleep(1)
if classe == 'Guerreiro':
    print('\nVocê, ', nome, ', é um guerreiro e está no meio de uma patrulha quando, de repente, um ladrão aparece e quer roubar você e seu grupo!', sep ='')
    batalha(125, 0, vida)
elif classe == 'Mago':
    print('\nVocê, ', nome, ', é um mago e, enquanto estudava necromancia, acidentalmente invocou um guerreiro zumbi e agora tem que derrotá-lo!', sep='')
    batalha(125, 16, vida)
else:
    print('\nVocê, ', nome, ', é um ladrão que, enquanto descansava, um mago que você roubou apareceu com sede de vingança e agora você terá que enfrentá-lo!')
    batalha(125, 16, vida)

#FIM DE JOGO
print()
print(10*'-')
print('FIM DE JOGO')
print(10*'-')
sair = input('\nPressione ENTER para sair')