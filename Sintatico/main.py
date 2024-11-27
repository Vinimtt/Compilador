from ply import yacc
from listaTokens import tokens

def p_programa(p):
    """
    programa : declaracao
    """

def p_declaracao(p):
    """
    declaracao : declaracao_variavel
                | declaracao_funcao
                | declaracao_estrutura
                | comentario
    """

def p_declaracao_variavel(p):
    """
    declaracao_variavel : tipo ID SEMICOLON
                        | tipo ID EQUAL expressao SEMICOLON
    """
    
def p_tipo(p):
    """
    tipo : NUM_INT
         | NUM_DEC
         | TEXTO
    """

def p_declaracao_funcao(p):
    """
    declaracao_funcao : tipo ID LPAREN parametros RPAREN bloco
    """

def p_parametros(p):
    """
    parametros : parametros
               | parametros COMMA parametros
               | tipo ID
               | tipo ID LBRACKET RBRACKET
    """

def p_bloco(p):
    """
    bloco : LBRACE declaracao RBRACE

    """
    
def p_comentario(p):
    """
    comentario : COMMENT
               | MULTICOMMENT
    """

def p_expressoes(p):
    """
    expressoes : atribuicao
    """

def p_atribuicao(p):
    """
    atribuicao : ID EQUAL expressao
               | ID PLUSEQUAL expressao
               | ID MINUSEQUAL expressao
               | ID TIMESEQUAL expressao
               | ID DIVEQUAL expressao
               | ID ANDANDEQUAL expressao
               | ID OROREQUAL expressao
               | ID EQUAL ID
               | ID PLUSEQUAL ID
               | ID MINUSEQUAL ID
               | ID TIMESEQUAL ID
               | ID DIVEQUAL ID
               | ID ANDANDEQUAL ID
               | ID OROREQUAL ID
    """
    
def p_estrutura_controle(p):
    """
    estrutura_controle : IF LPAREN expressao RPAREN bloco
                       | IF LPAREN expressao RPAREN ELSE bloco
                       | WHILE LPAREN expressao RPAREN bloco
                       | FOR LPAREN expressao SEMICOLON expressao SEMICOLON expressao RPAREN bloco
                       | RETURN expressao
    """

def p_declaracao_estrutura(p):
    """
    declaracao_estrutura : STRUCT ID LBRACE declaracao_variavel RBRACE
    """
    
def p_array(p):
    """
    array : ID LBRACKET expressao RBRACKET
          | ID LBRACKET RBRACKET
          | ID LBRACE expressoes RBRACE
    """

def p_expressao(p):
    """
    expressao : expressao_logica
    """
    
def p_expressao_logica(p):
    """
    expressao_logica : expressao_relacional
                     | expressao_logica ANDAND expressao_relacional
                     | expressao_logica OROR expressao_relacional
    """

def p_expressao_relacional(p):
    """
    expressao_relacional : expressao_aritmetica
                         | expressao_aritmetica GREATER expressao_aritmetica
                         | expressao_aritmetica GREATEREQUAL expressao_aritmetica
                         | expressao_aritmetica LESS expressao_aritmetica
                         | expressao_aritmetica LESSEQUAL expressao_aritmetica
                         | expressao_aritmetica NOTEQUAL expressao_aritmetica
                         | expressao_aritmetica EQUALS expressao_aritmetica
    """

def p_expressao_aritmetica(p):
    """
    expressao_aritmetica : expressao_multiplicativa
                         | expressao_aritmetica PLUS expressao_multiplicativa
                         | expressao_aritmetica MINUS expressao_multiplicativa
    """

def p_expressao_multiplicativa(p):
    """
    expressao_multiplicativa : expressao_unaria
                             | expressao_multiplicativa TIMES expressao_unaria
                             | expressao_multiplicativa DIVIDE expressao_unaria
                             | expressao_multiplicativa MODULO expressao_unaria
    """

def p_expressao_unaria(p):
    """
    expressao_unaria : expressao_postfix
                     | MINUS expressao_unaria
                     | PLUSPLUS expressao_postfix
                     | MINUSMINUS expressao_postfix
    """

def p_expressao_postfix(p):
    """
    expressao_postfix : primaria
                      | primaria LBRACKET expressao RBRACKET
                      | primaria LPAREN argumentos RPAREN
                      | primaria DOT ID
    """

def p_argumentos(p):
    """
    argumentos : expressoes
               | 
    """

def p_primaria(p):
    """
    primaria : ID
             | NUM_INT
             | NUM_DEC
             | TEXTO
             | LPAREN expressao RPAREN
    """
    
def p_error(p):
    if p:
        print(f"Erro de sintaxe token {p.type}")
        print(f"Linha: {p.lineno}")
        print(f"Posicao: {p.lexpos}")
        print(f"Valor: {p.value}")
    else:
        print("Erro de sintaxe")
        
sintatico = yacc.yacc()