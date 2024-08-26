# Ângelo Piovezan Jorgeto

# o coódigo resolverá as operações de união, interseção, diferença e produto cartesiano, por exemplo o primeiro arquivo conjuntos.txt proposto pelo professor terá que resolver a união de conjunto 1: [3, 5, 67, 7] com conjunto 2: [1, 2, 3, 4] e a resposta deve ser [1, 2, 3, 4, 5, 67, 7]. A interseção de conjunto 1: [1, 2, 3, 4] com conjunto 2: [4, 5] deve ser [4, 5]. A diferença de conjunto 1: [1, A, C, 34] com conjunto 2: [A, C, D, 23] deve ser [1, 34, D, 23]. E o produto cartesiano de conjunto 1: [3, 4, 5, 5, A, B, R] com conjunto 2: [1, B, C, D, 1] a resposta deve ser: [('3', '1'), ('3', 'B'), ('3', 'C'), ('3', 'D'), ('3', '1'), ('4', '1'), ('4', 'B'), ('4', 'C'), ('4', 'D'), ('4', '1'), ('5', '1'), ('5', 'B'), ('5', 'C'), ('5', 'D'), ('5', '1'), ('5', '1'), ('5', 'B'), ('5', 'C'), ('5', 'D'), ('5', '1'), ('A', '1'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', '1'), ('B', '1'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', '1'), ('R', '1'), ('R', 'B'), ('R', 'C'), ('R', 'D'), ('R', '1')]
from collections import OrderedDict

def realizar_operacoes(arquivo_entrada):
    # função para ordenar corretamento o arquivo
    def ordenar(lst):
        return OrderedDict.fromkeys(lst)

    # abre para fazer a leitura do arquivo
    with open(arquivo_entrada, 'r') as arquivo:
        linhas = arquivo.readlines()

    num_operacoes = int(linhas[0].strip())
    index = 1  
    # lista que armazena resultados
    resultados = []  

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


