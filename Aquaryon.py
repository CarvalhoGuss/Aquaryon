from datetime import date


def formatar(valor, unidade=''):
    """Mostra '-' se o valor estiver vazio, ou 'valor unidade' se houver número."""
    if valor == '':
        return '-'
    return f'{valor} {unidade}'.strip()


# Verificação se é número
def pedir_numero(mensagem, tipo=float):
    """Pede um número ao usuário. Aceita campo em branco (retorna '')."""
    while True:
        valor = input(mensagem).strip()
        if valor == '':
            return ''  # campo em branco -> "não medido"
        try:
            return tipo(valor.replace(',', '.'))
        except ValueError:
            print('Valor inválido. Digite um número (ou deixe em branco para pular).')


# Menu principal
def menu():
    """Aqui é onde o usuário insere os resultados dos testes"""
    print('<======= Tabela de testes =======>')
    print('Data: {}'.format(date.today().strftime("%d/%m/%Y")))
    nome_cliente = input('Cliente: ').strip()
    salinidade = pedir_numero('Salinidade: ', int)
    kh = pedir_numero('Alcalinidade (Kh): ', float)
    fosfato = pedir_numero('Fosfato (PO4): ', float)
    nitrato = pedir_numero('Nitrato (NO3): ', float)
    calcio = pedir_numero('Cálcio (Ca): ', int)
    magnesio = pedir_numero('Magnésio (Mg): ', int)

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
        if salinidade <= 1021:  # Salinidade muito baixa
            print(
                'Salinidade muito baixa. Aprensenta risco aos animais. Para corrigir recomendamos fazer a reposição da '
                'água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de salinidade está '
                'devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu sistema por algum '
                'vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de recalque (se há água '
                'escorrendo pelo lado de fora do aquário em algum ponto.)')
        elif salinidade == 1022:  # Salinidade baixa
            print('Salinidade muito baixa. Apresenta risco aos animais. Para corrigir recomendamos fazer a reposição'
                  ' da água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de salinidade '
                  'está devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu sistema por '
                  'algum vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de recalque '
                  '(se há água escorrendo pelo lado de fora do aquário em algum ponto.)')
        elif salinidade == 1023:  # Salinidade levemente baixa
            print('Salinidade levemente baixa. Não apresenta risco aos animais. Para corrigir recomendamos fazer a '
                  'reposição da água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de '
                  'salinidade está devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu '
                  'sistema por algum vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de '
                  'recalque (se há água escorrendo pelo lado de fora do aquário em algum ponto.)')
        elif salinidade == 1024 or salinidade == 1025:  # Salinidade ideal
            print('Nível de salinidade aceitável.')
        elif salinidade == 1026:  # Bom, mas eu abaixaria
            print('Salinidade adequada. Não apresenta risco aos animais. Porém recomendamos abaixar para 1025 ou 1024. '
                  'Para corrigir recomendamos fazer uma TPA. Obs.: verifique regularmente se o seu medidor de '
                  'salinidade está devidamente calibrado.')
        elif salinidade == 1027:  # Salinidade levemente alta
            print(
                'Salinidade levemente alta. Não apresenta riscos aos animais. Para corrigir recomendamos fazer uma TPA.'
                ' Obs.: verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
        elif salinidade == 1028:  # Salinidade alta
            print('Salinidade alta. Apresenta riscos aos animais. Para corrigir recomendamos fazer uma TPA. Obs.: '
                  'verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
        else:  # Salinidade muito alta
            print('Salinidade muito alta. Apresenta risco aos animais. Para corrigir recomendamos fazer uma TPA. Obs.:'
                  ' verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
        print()
    else:
        salinidade = "Não medido"

    return salinidade


def avaliar_kh(kh):
    if kh != '':  # Condicional de ocorrencia.
        if kh <= 5.5:  # muito baixo
            print('Nível de Kh muito baixo. Para corrigir recomendamos suplementar Kh através'
                  ' de algum balling. Fazer uma tpa pode ajudar nesse processo. Há risco de perda de corais caso se '
                  'mantenha nesse nível ou abaixo.')
        elif kh <= 5.9:  # Baixo
            print('Nível de Kh baixo. Nesse caso, recomendamos suplementar Kh através de algum balling. Fazer uma tpa '
                  'pode ajudar nesse processo.Há risco de perda de corais caso se mantenha nesse nível ou abaixo.')
        elif kh <= 6.9:  # Levemente baixo
            print(
                'Nível de Kh levemente baixo. Não apresenta riscos aos animais. Nesse caso, recomendamos suplementar '
                'Kh através de algum balling. Fazer uma tpa pode ajudar nesse processo.')
        elif kh <= 8.0:  # Ideal
            print('Nível de Kh dentro do aceitável.')
        elif kh <= 9.0:  # Levemente alto
            print('Nível de Kh levemente alto. Não apresenta risco aos animais. Recomendamos suspender a dosagem do'
                  ' balling de Kh ou reduzir a dosagem. Fazer uma TPA (troca parcial de água) pode ajudar a normalizar '
                  'os parâmetros.')
        elif kh <= 11.0:  # Alto
            print(
                'Nível de Kh alto. Não apresenta risco aos animais. Recomendamos suspender a dosagem do balling de '
                'Kh ou reduzir a dosagem. Fazer uma TPA (troca parcial de água) pode ajudar a normalizar os '
                'parâmetros.')
        else:  # Muito alto
            print(
                'Nível de Kh muito alto. Apresenta risco aos animais. Para corrigir, recomendamos suspender a dosagem '
                'do balling de Kh até os parâmetros se adequarem. Fazer uma TPA (troca parcial de água) pode ajudar a '
                'reduzir os níveis.')
        print()
    else:
        kh = 'Não medido'

    return kh


def avaliar_fosfato(fosfato):
    if fosfato != '':
        if fosfato == 0.00:  # Fosfato zerado
            print(
                'Nível de fosfáto muito baixo (zerado). Não apresenta riscos aos animais desde que feito por aquaristas '
                'mais experientes. De maneira geral, fosfato zerado não é o recomendável. Para subir recomendamos '
                'aumentar um pouco a quantidade de ração dada aos peixes ou aos corais. Isso ja deve ser o suficiente '
                'para a correção.')
        elif fosfato == 0.01:  # Fosfato baixo
            print(
                'Nível de fosfáto baixo. Não apresenta riscos aos animais. Para aumentar os níveis recomendamos aumentar '
                'um pouco a quantidade de ração dada aos peixes ou aos corais. Isso ja deve ser o suficiente para a '
                'correção.')
        elif fosfato == 0.02:  # Fosfato levemente baixo
            print('Nível de fosfáto levemente baixo. Não apresenta risco aos animais. Para aumentar os níveis '
                  'recomendamos aumentar um pouco a quantidade de ração dada aos peixes. Isso ja deve ser o suficiente '
                  'para a correção.')
        elif fosfato < 0.08:  # Ideal
            print('Nível de fosfáto aceitável.')
        elif fosfato < 0.20:  # Fosfato levemente alto
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
        if nitrato == 0.00:  # Zerado (muito baixo)
            print(
                'Nível de nitrato muito baixo (zerado). Não apresenta risco aos animais (desde que feito por aquaristas'
                ' experiêntes), porém impede que eles se desenvolvam da maneira adequada. Nesse caso você '
                'pode: dosar nitrato líquido; ou remover o copo do Skimmer por alguns dias (fazer monitoramento com '
                'testes).')
        elif nitrato < 5.00:  # Baixo
            print(
                'Nível de nitrato baixo. Não apresenta risco aos animais. Para corrigir pode-se dosar nitrato líquido,'
                ' ou remover o copo do Skimmer por alguns dias (fazer monitoramento com testes).')
        elif nitrato < 8.00:  # Levemente baixo
            print(
                'Nível de nitrato levemente baixo. Não apresenta risco aos animais. Para corrigir pode se dosar nitrato '
                'líquido ou remover o copo do Skimmer por alguns dias (fazer monitoramento com testes)')
        elif nitrato < 15.00:  # Ideal
            print('Nivel de nitrato aceitável.')
        elif nitrato < 20.00:  # Levemente alto
            print('Nível de nitrato levemente elevado. Não apresenta risco, porém pode causar perda de coloração dos '
                  'corais. Pode ser reduzido com TPA (troca parcial de água) ou fontes de carbono.')
        elif nitrato < 30.00:  # Alto
            print(
                'Nível de nitrato elevado. Não apresenta risco imediato aos animais, porém pode causar perda de coloração'
                ' dos corais porém recomendamos que abaixe ele. Para abaixar recomendamos uma TPA (troca parcial de água)'
                ' ou utilização de fonte de carbono.')
        else:  # Muito alto
            print(
                'Nivel de nitrato muito alto. Apresenta risco de perda de animais. Para corrigir recomendamos verificar '
                'se o Skimmer está devidamente regulado, e utilizar uma fonte de carbono. Uma TPA (troca parcial de água)'
                ' pode ajudar nesse processo.')
    print()

    return nitrato


def avaliar_calcio(calcio):
    if calcio != '':
        if calcio <= 310:  # Muito baixo
            print(
                'Nível de cálcio muito baixo. Apresenta risco aos corais. Deve ser corrigido através de reposição por '
                'balling ou por TPA (troca parcial de água).')
        elif calcio <= 330:  # Baixo
            print('Nível de cálcio baixo. Apresenta risco aos corais. Recomendamos correção através do uso de algum '
                  'balling.')
        elif calcio < 350:  # Levemente baixo
            print(
                'Nível de cálcio levemente baixo. Ainda não apresenta risco, porém seria interessante corrigir dosando '
                'algum balling.')
        elif calcio <= 450:  # Ideal
            print('Nível de cálcio adequado.')
        elif calcio <= 480:  # Levemente alto
            print('Nível de cálcio levemente elevado. Não apresenta riscos, pode ser abaixado reduzindo a dosagem do '
                  'balling ou com uma TPA (troca parcial de água)')
        elif calcio <= 500:  # Alto
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
          '\nCliente: {}'.format(nome_cliente, 'dKH')),
          '\nSalinidade: {}'.format(formatar(salinidade, 'g/cm³')),
          '\nAlcalinidade (Kh): {}'.format(formatar(kh, 'dKH')),
          '\nFosfato (PO4): {}'.format(formatar(fosfato, 'ppm')),
          '\nNitrato (NO3): {}'.format(formatar(nitrato, 'ppm')),
          '\nCálcio (Ca): {}'.format(formatar(calcio, 'mg/l')),
          '\nMagnésio (Mg): {}'.format(formatar(magnesio, 'mg/l')),
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
input('\nPressione ENTER para sair...')
