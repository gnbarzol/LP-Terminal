import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for':'FOR',
    'end':'END',
    'and':'AND',
    'or':'OR',
    'in': 'IN'


 }
# List of token names. This is always required
tokens = [
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'ASIGN',
    'GREATER',
    'MINOR',
    'ALFT',
    'ARGT',
    'EXPONENTIATION',
    'LOGIC_AND',
    'COMMA'
]+list(reserved.values())



def analyze(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

# Regular expression rules for simple tokens
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASIGN = r'='
t_GREATER = r'>'
t_MINOR = r'<'
t_ALFT = r'\['
t_ARGT = r'\]'
t_EXPONENTIATION = r'\*\*'
t_LOGIC_AND = r'&&'
t_COMMA = r'\,'


# A regular expression rule with some action code

def t_ID(t):
    r'[a-zA-Z_\$@][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_STRING(t):
    r'["][a-zA-Z0-9\s]["]+'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

 # A string containing ignored characters (spaces and tabs)


t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Tokenize
while True:
    data = input(">>>")
    analyze(data)
    if len(data)==0:
        break
