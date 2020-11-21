import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for':'FOR',
    'end':'END',
    'and':'AND',
    'or':'OR',
    'in': 'IN',
    'do': 'DO',
    'false': 'FALSE',
    'true': 'TRUE',
    'puts': 'PUTS',
    'gets': 'GETS',
    'include': 'INCLUDE',
    'empty': 'EMPTY',
    'upcase': 'UPCASE',
    'min': 'MIN',
    'first': 'FIRST',
    'map': 'MAP',
    'has_value': 'HAS_VALUE',
    'merge': 'MERGE',
    'size': 'SIZE'

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
    'EQUAL',
    'EQUAL_STRICT',
    'GREATER',
    'GREATER_THAN_OR_EQUAL',
    'MINOR',
    'MINOR_THAN_OR_EQUAL',
    'ALFT',
    'ARGT',
    'EXPONENTIATION',
    'LOGIC_AND',
    'LOGIC_OR',
    'LOGIC_NOT',
    'COMMA',
    'FLOAT',
    'POINT',
    'QUESTION',
    'PIPE',
    'OTHERSTRINGDECLARATION',
    'OPENINGCB',
    'CLOSURECB',
    'HASHROCKET'
]+list(reserved.values())

 # A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_\$@][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_OTHERSTRINGDECLARATION(t):
    r'\%q\(.*?\)'
    t.value = t.value[3:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER = r'>'
t_GREATER_THAN_OR_EQUAL = r'>='
t_MINOR = r'<'
t_MINOR_THAN_OR_EQUAL = r'<='
t_ALFT = r'\['
t_ARGT = r'\]'
t_EXPONENTIATION = r'\*\*'
t_LOGIC_AND = r'&&'
t_LOGIC_OR = r'\|\|'
t_LOGIC_NOT = r'!'
t_COMMA = r'\,'
t_ASIGN = r'='
t_EQUAL = r'=='
t_EQUAL_STRICT = r'==='
t_POINT = r'\.'
t_QUESTION = r'\?'
t_PIPE = r'\|'
t_ignore_COMMENT = r'\#.*'
t_OPENINGCB = r'\{'
t_CLOSURECB = r'\}'
t_HASHROCKET = r'=>'

# Build the lexer
lexer = lex.lex()

def analyze(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


archivo = open("codigo.txt","r")


for line in archivo:
    print(">>>"+ line)
    analyze(line)
    if len(line)==0:
        break