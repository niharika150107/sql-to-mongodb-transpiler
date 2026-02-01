import ply.lex as lex
from .tokens import tokens,reserved
t_COMMA = r','
t_EQ = r'='
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_SEMICOLON = r';'
t_ignore=' \t'
#grammer for identifier and converting to lower case letters.
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')
    return t
#numbers and converting to integers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_STRING(t):
    r'\'[^\']*\'|"[^"]*"'
    t.value = t.value[1:-1]   # remove quotes
    return t
# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()
#def tokenize1(sql_query):
#   lexer.input(sql_query)
#    result=[]
#    while True:
#        tok=lexer.token()
#        if not tok:
#            break
#        result.append((tok.type,tok.value))
#    return result
def tokenize(sql_query):
    lexer.input(sql_query)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append({
            "type": tok.type,
            "value": tok.value,
            "line": tok.lineno,
            "position": tok.lexpos
        })
    return tokens_list
