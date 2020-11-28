# Get the token map from the lexer.  This is required.
from lexico import tokens

import ply.yacc as yacc


def p_STATEMENT(p):
  ''' STATEMENT : EXPRESSION
                | ASIGNATION
                | STRUCTURE_FOR
                | STRUCTURE_IF
                | STRUCTURE_WHILE
  '''
#GARY BARZOLA
def p_ASIGNATION(p):
  'ASIGNATION : ID ASIGN EXPRESSION'
  p[0] = 'ASIGNATION'


def p_EXPRESSION(p):
  ''' EXPRESSION : NUMBER
                | FLOAT
                | BOOLEAN
                | STRING
                | OTHERSTRINGDECLARATION
                | ARRAY
                | HASH
                | FUNTIONS_ARRAY
                | FUNTIONS_HASH
                | LOGIC_NOT EXPRESSION
                | EXPRESSION_MAT
                | EXPRESSION_CONCAT
                | PUTS EXPRESSION
                | PUTS ID
                | GETS EXPRESSION
                | FUNCTIONS_STRING
  '''
  p[0] = p[1]

# Permite comparaciones entre booleanos y strings
def p_EXPRESSION_COMP_BOOLEAN(p):
  ''' EXPRESSION : BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN
                | DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING
  '''
  p[0] = "EXPRESSION_COMP_BOOLEAN"

def p_OPERATOR_COMP_BOOLEAN(p):
  '''OPERATOR_COMP_BOOLEAN : EQUAL
                          | EQUAL_STRICT
                          | LOGIC_AND
                          | LOGIC_OR
                          | PIPE

  '''
  p[0] = p[1]

# Permite comparaciones entre numeros y floats
def p_EXPRESSION_COMP_MAT(p):
  'EXPRESSION : DATANF OPERATOR_COMP_MAT DATANF'
  p[0] = "EXPRESSION_COMP_MAT"

# Permite operaciones mat entre numeros y floats
def p_EXPRESSION_MAT(p):
  ''' EXPRESSION_MAT : EXPRESSION_MAT OPERATOR_MAT EXPRESSION_MAT
                    | LPAREN EXPRESSION_MAT RPAREN
      EXPRESSION_MAT : DATANF
  '''
  p[0] = "EXPRESSION_MAT"

def p_DATA_NUMBER_FLOAT(p):
  '''DATANF : NUMBER
            | FLOAT
            | ID
  '''
  p[0] = p[1]

# Permite reconocer una concatenacion de strings o arrays
def p_EXPRESSION_CONCAT(p):
  ''' EXPRESSION_CONCAT : EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT
      EXPRESSION_CONCAT : DATASTRING
                        | ARRAY

  '''

def p_DATA_STRINGS(p):
  '''DATASTRING : STRING
                | OTHERSTRINGDECLARATION
  '''
  p[0] = p[1]

# Funciones que un String puede llamar
def p_FUNCTIONS_STRING(p):
  '''
  FUNCTIONS_STRING : DATASTRING POINT FUNCTIONS_ALLOWED_STRING

  FUNCTIONS_ALLOWED_STRING : INCLUDE QUESTION DATASTRING
                            | EMPTY QUESTION
                            | UPCASE
  '''

# Permite reconocer arreglos
def p_ARRAY(p):
  'ARRAY : ALFT DATA ARGT'
  p[0] = 'ARRAY'

# Funciones que un array puede llamar
def p_FUNTIONS_ARRAY(p):
  '''FUNTIONS_ARRAY : ARRAY POINT FUNTIONS_ALLOWED_ARRAY

    FUNTIONS_ALLOWED_ARRAY : MIN
                          | FIRST
                          | MAP_ARRAY
  '''

# Estructura para reconcer un map y el contenido permitido dentro de el.
def p_MAP_ARRAY(p):
  '''MAP_ARRAY : MAP OPENINGCB PIPE ID PIPE DATA_REPEAT_MAP CLOSURECB

    DATA_REPEAT_MAP : STATEMENT
                    | STATEMENT DATA_REPEAT_MAP

    DATA_ALLOWED_IN_MAP : ASIGNATION
                        | EXPRESSION
  '''

# Permite reconocer Hash.
def p_HASH(p):
  'HASH : OPENINGCB REGISTRY CLOSURECB'
  p[0] = 'HASH'


def p_REGISTRY(p):
  'REGISTRY : STRING HASHROCKET KEY'
  p[0] = 'p_REGISTRY'

def p_KEY(p):
  '''KEY : NUMBER
          | STRING
  '''
  p[0] = p[1]


# Funciones que un hash puede llamar
def p_FUNTIONS_HASH(p):
  '''FUNTIONS_HASH : HASH POINT FUNTIONS_ALLOWED_HASH

    FUNTIONS_ALLOWED_HASH : HAS_VALUE QUESTION KEY
                          | MERGE LPAREN HASH RPAREN
                          | SIZE
  '''

def p_REGISTRY_ANY(p):
  'REGISTRY : REGISTRY COMMA REGISTRY'

# Permite reconocer la estructura de control for
def p_STRUCTURE_FOR(p):
  ''' STRUCTURE_FOR : STRUCTURE_IN_FOR DATA_REPEAT END

      STRUCTURE_IN_FOR : FOR ID IN ARRAY DO
                    | FOR ID IN ID DO

      DATA_REPEAT : DATA_ALLOWED_IN_FOR
                  | DATA_ALLOWED_IN_FOR DATA_REPEAT

      DATA_ALLOWED_IN_FOR : ASIGNATION
                          | EXPRESSION
  '''

# Permite reconocer la estructura de control if
def p_STRUCTURE_IF(p):
  ''' STRUCTURE_IF : STRUCTURE_IN_IF DATA_REPEAT END

      STRUCTURE_IN_IF : IF LPAREN BOOLEAN RPAREN

      DATA_REPEAT : DATA_ALLOWED_IN_IF
                  | DATA_ALLOWED_IN_IF DATA_REPEAT
                  | DATA_ALLOWED_IN_IF ELSE DATA_ALLOWED_IN_IF

      DATA_ALLOWED_IN_IF : ASIGNATION
                        | EXPRESSION
  '''

# Permite reconocer la estructura de control While
def p_STRUCTURE_WHILE(p):
  ''' STRUCTURE_WHILE : STRUCTURE_IN_WHILE DATA_REPEAT END

      STRUCTURE_IN_WHILE : WHILE LPAREN TRUE RPAREN

      DATA_REPEAT : DATA_ALLOWED_IN_WHILE
                  | DATA_ALLOWED_IN_WHILE DATA_REPEAT

      DATA_ALLOWED_IN_WHILE : ASIGNATION
                            | EXPRESSION
  '''


def p_DATA(p):
  '''DATA : NUMBER
          | FLOAT
          | BOOLEAN
          | STRING
  '''
  p[0] = p[1]

def p_DATA_ANY(p):
  'DATA : DATA COMMA DATA'


def p_BOOLEAN(p):
  '''BOOLEAN : TRUE
            | FALSE
            | LOGIC_NOT TRUE
            | LOGIC_NOT FALSE
  '''
  p[0] = p[1]

def p_OPERATOR_MAT(p):
  '''OPERATOR_MAT : PLUS
                  | MINUS
                  | TIMES
                  | DIVIDE
                  | EXPONENTIATION
  '''
  p[0] = p[1]



def p_OPERATOR_COMP_MAT(p):
  '''OPERATOR_COMP_MAT : EQUAL
                      | EQUAL_STRICT
                      | GREATER_THAN_OR_EQUAL
                      | MINOR_THAN_OR_EQUAL
                      | MINOR
                      | GREATER
                      | LOGIC_AND
                      | LOGIC_OR
                      | PIPE
  '''
  p[0] = p[1]

def p_ERROR(p):
  print("Syntax error in input", p)

 # Build the parser

parser = yacc.yacc()
'''''
while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)'''