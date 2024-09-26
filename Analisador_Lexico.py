import re

# definicoes / ER
simbolos_especiais = ["(", ")", "[", "]", "{", "}", ",", ";"]
palavras_reservadas = ["int", "float", "char", "boolean", "void", "if", "else", "for", "while", "scanf", "println", "main", "return"]
operadores = ["=", "+", "-", "/", "*", "%", "&&", "||", "!"]
comparacao = [">", ">=", "<", "<=", "==", "!="]

# tokens
lista_tokens = []
identificadores = []
simbolos_especiais_encontrados = []
palavras_reservadas_encontradas = []
operadores_encontrados = []
comparacao_encontrada = []
Constante_de_texto = []
num_inteiros = []
num_decimais = []


index = 1
arquivo = 'teste.txt'
verificador = ""
string_lendo = False

# Regulares
regex_inteiro = r'^\d+'
regex_decimal = r'^\d+\.\d+'


try:
    with open(arquivo, 'r') as codigo:
        linhas = [linha.strip() for linha in codigo.readlines()]
except FileNotFoundError:
    print(f"Arquivo {arquivo} não encontrado!")
    linhas = []

# Processamento de cada linha do arquivo
for linha in linhas:
    if linha.startswith("//") or linha.startswith("/") or linha.startswith("*/"):
        continue
    s = linha
    while s:  # Enquanto houver caracteres na linha
        atual = s[0]  # Pega o primeiro caractere da linha
        s = s[1:]  # Remove o primeiro caractere da linha
        
        if atual == '"':  # Detecta início ou fim de string
            if string_lendo:
                Constante_de_texto.append(verificador)
                verificador = ""
                string_lendo = False
                print("Constante de texto:", Constante_de_texto[-1])
            else:
                string_lendo = True
            continue

        if string_lendo:
            verificador += atual
            continue

        # Se encontrarmos um espaço ou símbolo especial, verifica o que temos
        if atual.isspace() or atual in simbolos_especiais + operadores + comparacao:
            if verificador:  # Se o buffer não está vazio, verificamos a palavra
                if verificador in palavras_reservadas:
                    palavras_reservadas_encontradas.append(verificador)
                    print("Palavra reservada:", verificador)
                verificador = ""
        
        # Verifica se é uma palavra reservada
        if atual in palavras_reservadas:
            palavras_reservadas_encontradas.append(atual)
            lista_tokens.append(atual)
            print(f"Palavra reservada: {atual}")
        
        # Verifica se é um símbolo especial
        elif atual in simbolos_especiais:
            simbolos_especiais_encontrados.append(atual)
            lista_tokens.append(atual)
            print(f"Símbolo especial: {atual}")
        
        # Verifica se é um operador
        elif atual in operadores:
            operadores_encontrados.append(atual)
            lista_tokens.append(atual)
            print(f"Operador: {atual}")
        
        # Verifica se é um comparador
        elif atual in comparacao:
            comparacao_encontrada.append(atual)
            lista_tokens.append(atual)
            print(f"Comparador: {atual}")
        
        # Caso seja um identificador ou número
        elif atual != " ":  # Ignora espaços em branco
            while len(s) > 0 and s[0] not in operadores and s[0] not in comparacao and s[0] not in simbolos_especiais and s[0] != ' ':
                atual += s[0]
                s = s[1:]
                
             # Verifica se é um número decimal ou inteiro
            if re.match(regex_decimal, atual):  # Verifica se é decimal
                num_decimais.append(atual)
                lista_tokens.append(f"decimal, {atual}")
                print(f"Número decimal: {atual}")
                
            elif re.match(regex_inteiro, atual):  # Verifica se é inteiro
                num_inteiros.append(atual)
                lista_tokens.append(f"inteiro, {atual}")
                print(f"Número inteiro: {atual}")
                
            elif atual in palavras_reservadas:
                lista_tokens.append(atual)
                print(f"Palavra reservada: {atual}")
            else:
                if atual not in identificadores:
                    identificadores.append(atual)
                    lista_tokens.append(f"id, {index}")
                    print(f"Identificador id, {index} ({atual})")
                    index += 1
                else:
                    lista_tokens.append(f"id, {identificadores.index(atual) + 1}")
                    print(f"Identificador id, {identificadores.index(atual) + 1} {atual}")
                    
# Após o processamento de cada linha do arquivo, adicionamos a impressão das tabelas.

# Função para imprimir a tabela de símbolos
def imprimir_tabela_simbolos():
    print("\nTabela de Símbolos (Identificadores):")
    print("------------------------------------")
    for idx, identificador in enumerate(identificadores, start=1):
        print(f"{identificador} | (id,{idx})") 

# Função para imprimir a lista de tokens
def imprimir_lista_tokens():
    print("\nTabela de Tokens:")
    print("-----------------")
    for token in lista_tokens:
        print(f"( {token} ) ")

# Chama as funções ao final do processamento
imprimir_tabela_simbolos()
imprimir_lista_tokens()
