# inicialização e leitura do arquivo de dados do projeto
def carregarDados():
    ArquivoDados = open('ArquivoDadosProjetos.csv', 'r')
    dadosMatriz = []
    data = ArquivoDados.read()
    linhas = data.split('\n')

    for linha in linhas:
        dadosMatriz.append(linha.split(';'))

    ArquivoDados.close()
    return dadosMatriz


# enunciado parte a) #
# print(dadosMatriz)


# lógica entrada de dados de Mês e Ano pelo usuário + validação dos dados #


def entradaMes():
    mes = int(input('Digite um mês: '))
    while 1 < mes > 12:
        mes = int(input('Erro! O mês deve estar entre 01 e 12, digite novamente: '))
    return str(mes)


def entradaAno():
    ano = int(input('Digite um ano entre 1961 e 2016: '))
    while ano < 1961 or ano > 2016:
        ano = int(
            input('Erro! O ano deve estar entre 1961 e 2016, digite novamente: '))
    return str(ano)

# lógica pegar resultado enunciado b) - precipitação #


def procurarResultado1(dados, mes, ano):
    data = f'{mes}/{ano}'
    resultado = []
    for linha in dados:
        if data in linha[0] and float(linha[1]) >= 0:
            resultado.append(linha[1])

    return resultado


# lógica pegar resultado enunciado c) - temperatura máxima #

def getLineByDate(dados, data):
    for linha in dados:
        if data in linha[0]:
            return linha
    return None


def PegaPrimeiraSemanaDoMesesDo(ano):
    resultado = []
    for mes in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        for dia in range(1, 8):
            data = f'{dia}/{mes}/{ano}'
            resultado.append(data)


def procurarResultado2(dados, ano):
    resultado = []
    for mes in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        temperaturas_dos_dias = [0]
        for dia in range(1, 8):
            data = f'{dia}/{mes}/{ano}'
            linha = getLineByDate(dados, data)
            if linha:
                temperatura_do_dia = float(linha[2])
                temperaturas_dos_dias.append(temperatura_do_dia)
        resultado.append(max(temperaturas_dos_dias))
    return resultado


# função principal com as outras funções dentro para printar o resultado dos enunciados b) e c) #


def main():
    dados = carregarDados()
    mes = entradaMes()
    ano = entradaAno()
    resultado1 = procurarResultado1(dados, mes, ano)
    resultado2 = procurarResultado2(dados, ano)
    print(resultado1)
    print(resultado2)


main()
