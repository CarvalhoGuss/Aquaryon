from datetime import date

print('Utilizar "." (ponto) ao invés de "," (vírgula) em números reais.')
print('<======= Tabela de testes =======>')
print('Data: {}'.format(date.today().strftime("%d/%m/%Y")))
cli = str(input('Cliente: '))
sal = int(input('Salinidade: '))
kh = float(input('Alcalinidade (Kh): '))
fosf = float(input('Fosfato (PO4): '))
nitr = float(input('Nitrato (NO3): '))
ca = int(input('Cálcio (Ca): '))
mg = int(input('Magnésio (Mg): '))
print()

print('<======== Resultados aceitáveis ========>')
print('Salinidade: 1024 - 1026')
print('Alcalinidade (Kh): 6.5 - 7.0')
print('Fosfato (PO4): 0.03 - 0.08 (ppm)')
print('Nitrato (NO3): 8.0 - 15.0 (ppm)')
print('Cálcio (Ca): 350 - 450 (mg/litro)')
print('Magnésio (Mg): 1250 - 1380 (mg/litro)')
print()

# Laudo
print('<===== Resultados dos Testes =====>')
print('Data: {}'.format(date.today().strftime("%d/%m/%Y")))
print('Cliente: {}'.format(cli))
print()
print('Salinidade: {}'.format(sal))
print('Alcalinidade (Kh): {}'.format(kh))
print('Fosfato (PO4): {}ppm'.format(fosf))
print('Nitrato (NO3): {}ppm'.format(nitr))
print('Cálcio (Ca): {}mg/l'.format(ca))
print('Magnésio (Mg): {}mg/l'.format(mg))
print()

# Salinidade
if sal != '':
    if sal <= 1021:  # salinidade muito baixa
        print('Salinidade muito baixa. Aprensenta risco aos animais. Para corrigir recomendamos fazer a reposição da '
              'água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de salinidade está '
              'devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu sistema por algum '
              'vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de recalque (se há água '
              'escorrendo pelo lado de fora do aquário em algum ponto.)')
    if sal == 1022:  # salinidade baixa
        print('Salinidade muito baixa. Apresenta risco aos animais. Para corrigir recomendamos fazer a reposição'
              ' da água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de salinidade '
              'está devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu sistema por '
              'algum vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de recalque '
              '(se há água escorrendo pelo lado de fora do aquário em algum ponto.)')
    if sal == 1023:  # salinidade levemente baixa
        print('Salinidade levemente baixa. Não apresenta risco aos animais. Para corrigir recomendamos fazer a '
              'reposição da água do aquário com água salgada. Obs.: verifique regularmente se o seu medidor de '
              'salinidade está devidamente calibrado. Recomendamos também verificar se existe água saíndo do seu '
              'sistema por algum vazamento ou goticulas pulando para fora do aquario próximo a saída da bomba de '
              'recalque (se há água escorrendo pelo lado de fora do aquário em algum ponto.)')
    if sal == 1024 or sal == 1025:  # salinidade ideal
        print('Nível de salinidade aceitável.')
    if sal == 1026:  # bom mas eu abaixaria
        print('Salinidade adequada. Não apresenta risco aos animais. Porém recomendamos abaixar para 1025 ou 1024. '
              'Para corrigir recomendamos fazer uma TPA. Obs.: verifique regularmente se o seu medidor de salinidade '
              'está devidamente calibrado.')
    if sal == 1027:  # salinidade levemente alta
        print('Salinidade levemente alta. Não apresenta riscos aos animais. Para corrigir recomendamos fazer uma TPA.'
              ' Obs.: verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
    if sal == 1028:  # salinidade alta
        print('Salinidade alta. Apresenta riscos aos animais. Para corrigir recomendamos fazer uma TPA. Obs.: '
              'verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
    if sal >= 1029:  # salinidade muito alta
        print('Salinidade muito alta. Apresenta risco aos animais. Para corrigir recomendamos fazer uma TPA. Obs.:'
              ' verifique regularmente se o seu medidor de salinidade está devidamente calibrado.')
print()

# Kh
if kh != '':  # condicional de ocorrencia.
    if kh <= 5.5:  # muito baixo
        print('Nível de Kh muito baixo. Para corrigir recomendamos suplementar Kh através'
              ' de algum balling. Fazer uma tpa pode ajudar nesse processo. Há risco de perda de corais caso se '
              'mantenha nesse nível ou abaixo.')
    if kh <= 5.9:  # baixo
        print('Nível de Kh baixo. Nesse caso, recomendamos suplementar Kh '
              'através de algum balling. Fazer uma tpa pode ajudar nesse processo.Há risco de perda de corais caso se '
              'mantenha nesse nível ou abaixo.')
    if kh <= 6.9:  # levemente baixo
        print('Nível de Kh levemente baixo. Não apresenta riscos aos animais. Nesse caso, recomendamos suplementar Kh '
              'através de algum balling. Fazer uma tpa pode ajudar nesse processo.')
    if 6.9 < kh <= 8.0:  # ideal
        print('Nível de Kh dentro do aceitável.')
    if 8.0 < kh <= 9.0:  # levemente alto
        print('Nível de Kh levemente alto. Não apresenta risco aos animais. Recomendamos suspender a dosagem do'
              ' balling de Kh ou reduzir a dosagem. Fazer uma TPA (troca parcial de água) pode ajudar a normalizar '
              'os parâmetros.')
    if 9.0 < kh <= 11.0:  # alto
        print('Nível de Kh alto. Não apresenta risco aos animais. Recomendamos suspender a dosagem do balling de Kh ou '
              'reduzir a dosagem. Fazer uma TPA (troca parcial de água) pode ajudar a normalizar os parâmetros.')
    if kh > 11.0:  # muito alto
        print('Nível de Kh muito alto. Apresenta risco aos animais. Para corrigir, recomendamos suspender a dosagem do '
              'balling de Kh até os parâmetros se adequarem. Fazer uma TPA (troca parcial de água) pode ajudar a '
              'reduzir os níveis.')
print()

# fosfato
if fosf != '':
    if fosf == 0.00:  # fosfato zerado
        print('Nível de fosfáto muito baixo (zerado). Não apresenta riscos aos animais desde que feito por aquaristas '
              'mais experientes. De maneira geral, fosfato zerado não é o recomendável. Para subir recomendamos '
              'aumentar um pouco a quantidade de ração dada aos peixes ou aos corais. Isso ja deve ser o suficiente '
              'para a correção.')
    if fosf == 0.01:  # fosfato baixo
        print('Nível de fosfáto baixo. Não apresenta riscos aos animais. Para aumentar os níveis recomendamos aumentar '
              'um pouco a quantidade de ração dada aos peixes ou aos corais. Isso ja deve ser o suficiente para a '
              'correção.')
    if fosf == 0.02:  # fosfato levemente baixo
        print('Nível de fosfáto levemente baixo. Não apresenta risco aos animais. Para aumentar os níveis '
              'recomendamos aumentar um pouco a quantidade de ração dada aos peixes. Isso ja deve ser o suficiente '
              'para a correção.')
    if 0.03 <= fosf < 0.08:  # ideal
        print('Nível de fosfáto aceitável.')
    if 0.09 <= fosf < 0.20:  # fosfato levemente alto
        print('Nível de fosfáto levemente alto. Não apresenta risco aos animais. Recomendamos a utilização de uma mídia'
              'redutora de fosfáto ou uma TPA (troca parcial de água). Tome cuidado para não alimentar excessivamente '
              'os animais. Restos de ração no aquario fazem aumentar o nível de fosfáto.')
    if 0.20 <= fosf < 1.00:  # fosfato alto
        print('Nível de fosfáto alto. Não apresenta risco aos animais, porém pode causar deformação no crescimento dos '
              'animais. Para reduzir recomendamos a utilização de alguma mídia para reduzir fosfáto ou uma TPA (troca '
              'parcial de água). Além disso, alimentar os animais em grandes quantidades pode acabar aumentando seu '
              'fosfáto.')
    if fosf >= 1.00:  # fosfato muito alto
        print('Nível de fosfáto muito alto. Apresenta risco aos animais. Para corrigir recomendamos o uso de alguma '
              'mídia para redução de fosfáto ou uma TPA para acelerar o processo de redução. Tome cuidado para não '
              'alimentar excessivamente os animais. Restos de ração no aquario fazem aumentar o nível de fosfáto.')
print()

# Nitrato
if nitr != '':
    if nitr == 0.00:  # zerado (muito baixo)
        print('Nível de nitrato muito baixo (zerado). Não apresenta risco aos animais (desde que feito por aquaristas'
              ' experiêntes), porém impede que eles se desenvolvam da maneira adequada. Nesse caso você '
              'pode: dosar nitrato líquido; ou remover o copo do Skimmer por alguns dias (fazer monitoramento com '
              'testes).')
    if 0.00 < nitr < 5.00:  # baixo
        print('Nível de nitrato baixo. Não apresenta risco aos animais. Para corrigir pode-se dosar nitrato líquido,'
              ' ou remover o copo do Skimmer por alguns dias (fazer monitoramento com testes).')
    if 5.00 <= nitr < 8.00:  # levemente baixo
        print('Nível de nitrato levemente baixo. Não apresenta risco aos animais. Para corrigir pode se dosar nitrato '
              'líquido ou remover o copo do Skimmer por alguns dias (fazer monitoramento com testes)')
    if 8.00 <= nitr < 15.00:  # Ideal
        print('Nivel de nitrato aceitável.')
    if 15.00 <= nitr < 20.00:  # levemente alto
        print('Nível de nitrato levemente elevado. Não apresenta risco, porém pode causar perda de coloração dos '
              'corais. Pode ser reduzido com TPA (troca parcial de água) ou fontes de carbono.')
    if 20.00 <= nitr < 30.00:  # alto
        print('Nível de nitrato elevado. Não apresenta risco imediato aos animais, porém pode causar perda de coloração'
              ' dos corais porém recomendamos que abaixe ele. Para abaixar recomendamos uma TPA (troca parcial de água)'
              ' ou utilização de fonte de carbono.')
    if nitr >= 30.00:  # muito alto
        print('Nivel de nitrato muito alto. Apresenta risco de perda de animais. Para corrigir recomendamos verificar '
              'se o Skimmer está devidamente regulado, e utilizar uma fonte de carbono. Uma TPA (troca parcial de água)'
              ' pode ajudar nesse processo.')
print()

# Cálcio
if ca != '':
    if ca <= 310:  # muito baixo
        print('Nível de cálcio muito baixo. Apresenta risco aos corais. Deve ser corrigido através de reposição por '
              'balling ou por TPA (troca parcial de água).')
    if ca <= 330:  # baixo
        print('Nível de cálcio baixo. Apresenta risco aos corais. Recomendamos correção através do uso de algum '
              'balling.')
    if ca < 350:  # levemente baixo
        print('Nível de cálcio levemente baixo. Ainda não apresenta risco, porém seria interessante corrigir dosando '
              'algum balling.')
    if ca <= 450:  # ideal
        print('Nível de cálcio adequado.')
    if 450 <= ca <= 480:  # levemente alto
        print('Nível de cálcio levemente elevado. Não apresenta riscos, pode ser abaixado reduzindo a dosagem do '
              'balling ou com uma TPA (troca parcial de água)')
    if 480 < ca <= 500:  # alto
        print('Nível de cálcio elevado. Não apresenta riscos aos animais, porém seria interessante reduzir um pouco.'
              ' Pode ser corrigido com TPA (troca parcial de água) ou suspensão da dosagem de balling.')
    if ca > 500:
        print('Nível de cálcio estourou o teste. Para corrigir, recomendamos suspender momentâneamente a dosagem de '
              'balling até a normalização.')
print()

# Magnésio
if mg != '':
    if mg <= 1200:  # muito baixo
        print('Nível de magnésio muito baixo. Para corrigir, recomendamos a reposição com balling.')
    if mg <= 1220:  # baixo
        print('Nível de magnésio baixo. Para corrigir recomendamos a reposição com balling.')
    if mg < 1250:  # levemente baixo
        print('Nível de magnésio levemente baixo. Para corrigir, recomendamos a reposição com balling.')
    if 1250 <= mg < 1390:  # ideal
        print('Nível de magnésio adequado.')
    if 1380 < mg <= 1410:  # levemene elevado
        print('Nível de magnésio levemente elevado. Para corrigir, recomendamos fazer uma TPA (troca parcial de água) '
              'ou dar uma pausa na dosagem de balling.')
    if 1410 < mg < 1490:  # alto
        print('Nível de magnésio alto. Para corrigir, recomendamos fazer uma TPA (troca parcial de água) e reduzir a '
              'dosagem do balling.')
    if mg >= 1500:
        print('Nível de magnésio muito alto. Para corrigir, recomendamos fazer uma TPA (troca parcial de água) ou '
              'suspender momentaneamente o uso do balling até normalizarem os parâmetros.')
