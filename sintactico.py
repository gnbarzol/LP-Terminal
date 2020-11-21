# Get the token map from the lexer.  This is required.
from lexico import tokens

import ply.yacc as yacc

def p_STATEMENT(p):
  ''' STATEMENT : EXPRESSION
                | ASIGNATION
                | STRUCTURE_FOR
  '''

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
                | FUNTIONS_ARRAY
                | LOGIC_NOT EXPRESSION
                | EXPRESSION_MAT
                | EXPRESSION_CONCAT
                | PUTS EXPRESSION
                | PUTS ID
                | GETS
  '''
  p[0] = p[1]

# Permite comparaciones entre booleanos y strings
def p_EXPRESSION_COMP_BOOLEAN(p):
  ''' EXPRESSION : BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN
                | DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING
  '''
  p[0] = "EXPRESSION_COMP_BOOLEAN"

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

# Permite reconocer una concatenacion de strings o arrays
def p_EXPRESSION_CONCAT(p):
  ''' EXPRESSION_CONCAT : EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT
      EXPRESSION_CONCAT : DATASTRING
                        | ARRAY
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

def p_DATA(p):
  '''DATA : NUMBER
          | FLOAT
          | BOOLEAN
          | STRING
  '''
  p[0] = p[1]

def p_DATA_ANY(p):
  'DATA : DATA COMMA DATA'

def p_DATA_NUMBER_FLOAT(p):
  '''DATANF : NUMBER 
            | FLOAT
  '''
  p[0] = p[1]

def p_DATA_STRINGS(p):
  '''DATASTRING : STRING 
                | OTHERSTRINGDECLARATION
  '''
  p[0] = p[1]

def p_BOOLEAN(p):
  '''BOOLEAN : TRUE
            | FALSE
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

def p_OPERATOR_COMP_BOOLEAN(p):
  '''OPERATOR_COMP_BOOLEAN : EQUAL
                          | EQUAL_STRICT
                          | LOGIC_AND
                          | LOGIC_OR
                          | PIPE
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
 
while True:
  try:
    s = raw_input('calc > ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)