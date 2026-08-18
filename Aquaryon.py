from datetime import date


# Menu principal
def menu():
    print('Utilizar "." (ponto) ao invés de "," (vírgula) em números reais.')
    print('<======= Tabela de testes =======>')
    print('Data: {}'.format(date.today().strftime("%d/%m/%Y")))
    nome_cliente = input('Cliente: ')
    salinidade = int(input('Salinidade: '))
    kh = float(input('Alcalinidade (Kh): '))
    fosfato = float(input('Fosfato (PO4): '))
    nitrato = float(input('Nitrato (NO3): '))
    calcio = int(input('Cálcio (Ca): '))
    magnesio = int(input('Magnésio (Mg): '))

    return nome_cliente, salinidade, kh, fosfato, nitrato, calcio, magnesio


# Tabela de referência
def tabela_de_referencia():
    print('\n<======== TABELA DE REFERÊNCIA ========>\n',
          'Salinidade: 1024 - 1026 g/cm³.\n',
          'Alcalinidade (Kh): 6.5 - 7.0\n',
          'Fosfato (PO4): 0.03 - 0.08 (ppm)\n',
          'Nitrato (NO3): 8.0 - 15.0 (ppm)\n',
          'Cálcio (Ca): 350 - 450 (mg/litro)\n',
          'Magnésio (Mg): 1250 - 1380 (mg/litro)\n'
          )


# Parâmetros e procedimentos
def avaliar_salinidade(salinidade):
    if salinidade != '':
        if salinidade <= 1021:  # salinidade muito baixa
            print(
                'Salinidade muito baixa. Aprensenta risco aos animais. Para corrigir recomendamos fazer a reposição da '
                'água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de salinidade está '
                'devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu sistema por algum '
                'vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de recalque (se há água '
                'escorrendo pelo lado de fora do aquário em algum ponto.)')
        elif salinidade == 1022:  # salinidade baixa
            print('Salinidade muito baixa. Apresenta risco aos animais. Para corrigir recomendamos fazer a reposição'
                  ' da água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de salinidade '
                  'está devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu sistema por '
                  'algum vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de recalque '
                  '(se há água escorrendo pelo lado de fora do aquário em algum ponto.)')
        elif salinidade == 1023:  # salinidade levemente baixa
            print('Salinidade levemente baixa. Não apresenta risco aos animais. Para corrigir recomendamos fazer a '
                  'reposição da água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de '
                  'salinidade está devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu '
                  'sistema por algum vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de '
                  'recalque (se há água escorrendo pelo lado de fora do aquário em algum ponto.)')
        elif salinidade == 1024 or salinidade == 1025:  # salinidade ideal
            print('Nível de salinidade aceitável.')
        elif salinidade == 1026:  # bom, mas eu abaixaria
            print('Salinidade adequada. Não apresenta risco aos animais. Porém recomendamos abaixar para 1025 ou 1024. '
                  'Para corrigir recomendamos fazer uma TPA. Obs.: verifique regularmente se o seu medidor de '
                  'salinidade está devidamente calibrado.')
        elif salinidade == 1027:  # salinidade levemente alta
            print(
                'Salinidade levemente alta. Não apresenta riscos aos animais. Para corrigir recomendamos fazer uma TPA.'
                ' Obs.: verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
        elif salinidade == 1028:  # salinidade alta
            print('Salinidade alta. Apresenta riscos aos animais. Para corrigir recomendamos fazer uma TPA. Obs.: '
                  'verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
        else:  # salinidade muito alta
            print('Salinidade muito alta. Apresenta risco aos animais. Para corrigir recomendamos fazer uma TPA. Obs.:'
                  ' verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
        print()
    else:
        salinidade = "Não medido"

    return salinidade


def avaliar_kh(kh):
    if kh != '':  # condicional de ocorrencia.
        if kh <= 5.5:  # muito baixo
            print('Nível de Kh muito baixo. Para corrigir recomendamos suplementar Kh através'
                  ' de algum balling. Fazer uma tpa pode ajudar nesse processo. Há risco de perda de corais caso se '
                  'mantenha nesse nível ou abaixo.')
        elif kh <= 5.9:  # baixo
            print('Nível de Kh baixo. Nesse caso, recomendamos suplementar Kh '
                  'através de algum balling. Fazer uma tpa pode ajudar nesse processo.Há risco de perda de corais caso se '
                  'mantenha nesse nível ou abaixo.')
        elif kh <= 6.9:  # levemente baixo
            print(
                'Nível de Kh levemente baixo. Não apresenta riscos aos animais. Nesse caso, recomendamos suplementar Kh '
                'através de algum balling. Fazer uma tpa pode ajudar nesse processo.')
        elif kh <= 8.0:  # ideal
            print('Nível de Kh dentro do aceitável.')
        elif kh <= 9.0:  # levemente alto
            print('Nível de Kh levemente alto. Não apresenta risco aos animais. Recomendamos suspender a dosagem do'
                  ' balling de Kh ou reduzir a dosagem. Fazer uma TPA (troca parcial de água) pode ajudar a normalizar '
                  'os parâmetros.')
        elif kh <= 11.0:  # alto
            print(
                'Nível de Kh alto. Não apresenta risco aos animais. Recomendamos suspender a dosagem do balling de Kh ou '
                'reduzir a dosagem. Fazer uma TPA (troca parcial de água) pode ajudar a normalizar os parâmetros.')
        else:  # muito alto
            print(
                'Nível de Kh muito alto. Apresenta risco aos animais. Para corrigir, recomendamos suspender a dosagem do '
                'balling de Kh até os parâmetros se adequarem. Fazer uma TPA (troca parcial de água) pode ajudar a '
                'reduzir os níveis.')
        print()
    else:
        kh = 'Não medido'

    return kh


def avaliar_fosfato(fosfato):
    if fosfato != '':
        if fosfato == 0.00:  # fosfato zerado
            print(
                'Nível de fosfáto muito baixo (zerado). Não apresenta riscos aos animais desde que feito por aquaristas '
                'mais experientes. De maneira geral, fosfato zerado não é o recomendável. Para subir recomendamos '
                'aumentar um pouco a quantidade de ração dada aos peixes ou aos corais. Isso ja deve ser o suficiente '
                'para a correção.')
        elif fosfato == 0.01:  # fosfato baixo
            print(
                'Nível de fosfáto baixo. Não apresenta riscos aos animais. Para aumentar os níveis recomendamos aumentar '
                'um pouco a quantidade de ração dada aos peixes ou aos corais. Isso ja deve ser o suficiente para a '
                'correção.')
        elif fosfato == 0.02:  # fosfato levemente baixo
            print('Nível de fosfáto levemente baixo. Não apresenta risco aos animais. Para aumentar os níveis '
                  'recomendamos aumentar um pouco a quantidade de ração dada aos peixes. Isso ja deve ser o suficiente '
                  'para a correção.')
        elif fosfato < 0.08:  # ideal
            print('Nível de fosfáto aceitável.')
        elif fosfato < 0.20:  # fosfato levemente alto
            print(
                'Nível de fosfáto levemente alto. Não apresenta risco aos animais. Recomendamos a utilização de uma mídia'
                'redutora de fosfáto ou uma TPA (troca parcial de água). Tome cuidado para não alimentar excessivamente '
                'os animais. Restos de ração no aquario fazem aumentar o nível de fosfáto.')
        elif fosfato < 1.00:  # Fosfato alto
            print(
                'Nível de fosfáto alto. Não apresenta risco aos animais, porém pode causar deformação no crescimento dos '
                'animais. Para reduzir recomendamos a utilização de alguma mídia para reduzir fosfáto ou uma TPA (troca '
                'parcial de água). Além disso, alimentar os animais em grandes quantidades pode acabar aumentando seu '
                'fosfáto.')
        else:  # Fosfato muito alto
            print(
                'Nível de fosfáto muito alto. Apresenta risco aos animais. Para corrigir recomendamos o uso de alguma '
                'mídia para redução de fosfáto ou uma TPA para acelerar o processo de redução. Tome cuidado para não '
                'alimentar excessivamente os animais. Restos de ração no aquario fazem aumentar o nível de fosfáto.')
    print()

    return fosfato


def avaliar_nitrato(nitrato):
    if nitrato != '':
        if nitrato == 0.00:  # zerado (muito baixo)
            print(
                'Nível de nitrato muito baixo (zerado). Não apresenta risco aos animais (desde que feito por aquaristas'
                ' experiêntes), porém impede que eles se desenvolvam da maneira adequada. Nesse caso você '
                'pode: dosar nitrato líquido; ou remover o copo do Skimmer por alguns dias (fazer monitoramento com '
                'testes).')
        elif nitrato < 5.00:  # baixo
            print(
                'Nível de nitrato baixo. Não apresenta risco aos animais. Para corrigir pode-se dosar nitrato líquido,'
                ' ou remover o copo do Skimmer por alguns dias (fazer monitoramento com testes).')
        elif nitrato < 8.00:  # levemente baixo
            print(
                'Nível de nitrato levemente baixo. Não apresenta risco aos animais. Para corrigir pode se dosar nitrato '
                'líquido ou remover o copo do Skimmer por alguns dias (fazer monitoramento com testes)')
        elif nitrato < 15.00:  # Ideal
            print('Nivel de nitrato aceitável.')
        elif nitrato < 20.00:  # levemente alto
            print('Nível de nitrato levemente elevado. Não apresenta risco, porém pode causar perda de coloração dos '
                  'corais. Pode ser reduzido com TPA (troca parcial de água) ou fontes de carbono.')
        elif nitrato < 30.00:  # alto
            print(
                'Nível de nitrato elevado. Não apresenta risco imediato aos animais, porém pode causar perda de coloração'
                ' dos corais porém recomendamos que abaixe ele. Para abaixar recomendamos uma TPA (troca parcial de água)'
                ' ou utilização de fonte de carbono.')
        else:  # muito alto
            print(
                'Nivel de nitrato muito alto. Apresenta risco de perda de animais. Para corrigir recomendamos verificar '
                'se o Skimmer está devidamente regulado, e utilizar uma fonte de carbono. Uma TPA (troca parcial de água)'
                ' pode ajudar nesse processo.')
    print()

    return nitrato


def avaliar_calcio(calcio):
    if calcio != '':
        if calcio <= 310:  # muito baixo
            print(
                'Nível de cálcio muito baixo. Apresenta risco aos corais. Deve ser corrigido através de reposição por '
                'balling ou por TPA (troca parcial de água).')
        elif calcio <= 330:  # baixo
            print('Nível de cálcio baixo. Apresenta risco aos corais. Recomendamos correção através do uso de algum '
                  'balling.')
        elif calcio < 350:  # levemente baixo
            print(
                'Nível de cálcio levemente baixo. Ainda não apresenta risco, porém seria interessante corrigir dosando '
                'algum balling.')
        elif calcio <= 450:  # ideal
            print('Nível de cálcio adequado.')
        elif calcio <= 480:  # levemente alto
            print('Nível de cálcio levemente elevado. Não apresenta riscos, pode ser abaixado reduzindo a dosagem do '
                  'balling ou com uma TPA (troca parcial de água)')
        elif calcio <= 500:  # alto
            print(
                'Nível de cálcio elevado. Não apresenta riscos aos animais, porém seria interessante reduzir um pouco.'
                ' Pode ser corrigido com TPA (troca parcial de água) ou suspensão da dosagem de balling.')
        else:
            print(
                'Nível de cálcio estourou o teste. Para corrigir, recomendamos suspender momentâneamente a dosagem de '
                'balling até a normalização.')
    print()

    return calcio


def avaliar_magnesio(magnesio):
    if magnesio != '':
        if magnesio <= 1200:  # muito baixo
            print('Nível de magnésio muito baixo. Para corrigir, recomendamos a reposição com balling.')
        elif magnesio <= 1220:  # baixo
            print('Nível de magnésio baixo. Para corrigir recomendamos a reposição com balling.')
        elif magnesio < 1250:  # levemente baixo
            print('Nível de magnésio levemente baixo. Para corrigir, recomendamos a reposição com balling.')
        elif magnesio <= 1380:  # ideal
            print('Nível de magnésio adequado.')
        elif magnesio <= 1410:  # levemente elevado
            print(
                'Nível de magnésio levemente elevado. Para corrigir, recomendamos fazer uma TPA (troca parcial de água) '
                'ou dar uma pausa na dosagem de balling.')
        elif magnesio < 1500:  # alto
            print(
                'Nível de magnésio alto. Para corrigir, recomendamos fazer uma TPA (troca parcial de água) e reduzir a '
                'dosagem do balling.')
        else:  # muito alto
            print('Nível de magnésio muito alto. Para corrigir, recomendamos fazer uma TPA (troca parcial de água) ou '
                  'suspender momentaneamente o uso do balling até normalizarem os parâmetros.')
    print()

    return magnesio


# Tabela de laudo
def resultados_dos_testes(nome_cliente, salinidade, kh, fosfato, nitrato, calcio, magnesio):
    print('\n<===== Resultados dos Testes =====>',
          '\nData: {}'.format(date.today().strftime("%d/%m/%Y")),
          '\nCliente: {}'.format(nome_cliente),
          '\nSalinidade: {} g/cm³'.format(salinidade),
          '\nAlcalinidade (Kh): {} dKH'.format(kh),
          '\nFosfato (PO4): {} ppm'.format(fosfato),
          '\nNitrato (NO3): {} ppm'.format(nitrato),
          '\nCálcio (Ca): {} mg/l'.format(calcio),
          '\nMagnésio (Mg): {} mg/l'.format(magnesio),
          '\n'
          )
    avaliar_salinidade(salinidade)
    avaliar_kh(kh)
    avaliar_fosfato(fosfato)
    avaliar_nitrato(nitrato)
    avaliar_calcio(calcio)
    avaliar_magnesio(magnesio)


# Programa principal
nome_cliente, salinidade, kh, fosfato, nitrato, calcio, magnesio = menu()
tabela_de_referencia()
resultados_dos_testes(nome_cliente, salinidade, kh, fosfato, nitrato, calcio, magnesio)
