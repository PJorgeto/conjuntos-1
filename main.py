from collections import OrderedDict

def realizar_operacoes(arquivo_entrada):
    # função para ordenar corretamento o arquivo
    def ordenar(lst):
        return OrderedDict.fromkeys(lst)

    # abre pra o arquivo leitura
    with open(arquivo_entrada, 'r') as arquivo:
        linhas = arquivo.readlines()

    num_operacoes = int(linhas[0].strip())
    index = 1  

    resultados = []  # lista que armazena resultados

    for i in range(num_operacoes):
        operacao = linhas[index].strip()
        conjunto1 = linhas[index + 1].strip().split(', ')
        conjunto2 = linhas[index + 2].strip().split(', ')

        conjunto1_od = ordenar(conjunto1)
        conjunto2_od = ordenar(conjunto2)

        if operacao == 'U':
            resultado = list(conjunto1_od.keys()) + [elem for elem in conjunto2 if elem not in conjunto1_od]
            op_descr = "União"
        elif operacao == 'I':
            resultado = [elem for elem in conjunto1 if elem in conjunto2_od]
            op_descr = "Interseção"
        elif operacao == 'D':
            resultado = [elem for elem in conjunto1 if elem not in conjunto2_od] + [elem for elem in conjunto2 if elem not in conjunto1_od]
            op_descr = "Diferença"
        elif operacao == 'C':
            resultado = [(x, y) for x in conjunto1 for y in conjunto2]
            op_descr = "Produto cartesiano"
        else:
            continue

        resultado_str = f"{op_descr}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        resultados.append(resultado_str)

        index += 3

    for resultado in resultados:
        print(resultado)

arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
realizar_operacoes(arquivo_entrada)


