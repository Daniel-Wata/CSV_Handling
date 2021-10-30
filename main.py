def csv_em_linhas_list(caminho: str):
    
    """
    THIS FUNCTION READS A CSV AND RETURNS A HEADER AND THE FOLLOWING DATA, SEPARATED BY COLUMNS
    args: caminho - path to the csv file
    
    """
    
    dados = []
    with open(caminho, 'r') as arquivo:
        for linha in arquivo.readlines():
            dados.append(linha.replace('\n', '').replace('"', '').split(','))
    header = dados[0]
    rows = dados[1:]
    
    return header, rows

def colunas_em_dicionarios(cabecalho,dados):
    
    """
    THIS FUNCTION TAKES A HEADER AND THE FOLLOWING DATA, SEPARATED BY COLUMNS AND TURNS IT INTO A DICTIONARY
    args: HEADER (LIST), DADOS (LIST)
    
    """
    
    dicionario_final = {}
    for coluna in range(len(cabecalho)):
        linhas = []
        for linha in range(len(dados)):
            linhas.append(dados[linha][coluna])
        dicionario_final[cabecalho[coluna]] = linhas
    return dicionario_final


def csv_em_dicionario(caminho: str):
    """
    THIS FUNCTION TAKES A PATH TO A CSV FILE AND RETURNS A DICTIONARY WITH THE LIST OF VALUES
    args: caminho
    """
    data = csv_em_linhas_list(caminho)
    return colunas_em_dicionarios(data[0],data[1])
