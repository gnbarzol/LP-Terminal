# Get the token map from the lexer.  This is required.
from lexico import tokens
import ply.yacc as yacc


def p_statement(p):
  ''' STATEMENT : EXPRESSION
                | ASIGNATION
                | STRUCTURE_FOR
                | STRUCTURE_IF
                | STRUCTURE_WHILE
  '''
  p[0] = p[1]


def p_asignation(p):
  'ASIGNATION : ID ASIGN EXPRESSION'
  p[0] = ('ASIGNATION', p[1], p[2], p[3])


def p_expression(p):
  ''' EXPRESSION : NUMBER
                | MINUS NUMBER
                | FLOAT
                | MINUS FLOAT
                | BOOLEAN
                | STRING
                | GETS
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
                | FUNCTIONS_STRING
                | ID PLUS ASIGN DATANF
  '''
  p[0] = ('EXPRESION', p[1])

# Permite comparaciones entre booleanos y strings
def p_expression_comp_boolean(p):
  ''' EXPRESSION : BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN
                | DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING
  '''
  p[0] = ('EXPRESSION__BOOLEAN', p[1], p[2], p[3])

def p_operator_comp_boolean(p):
  '''OPERATOR_COMP_BOOLEAN : EQUAL
                          | EQUAL_STRICT
                          | LOGIC_AND
                          | LOGIC_OR
                          | PIPE

  '''
  p[0] = ('OPERATOR_BOOLEAN', p[1])

# Permite comparaciones entre numeros y floats
def p_expression_comp_mat(p):
  'EXPRESSION : DATANF OPERATOR_COMP_MAT DATANF'
  p[0] =  ('EXPRESSION', p[1], p[2], p[3])

# Permite operaciones mat entre numeros y floats
def p_expression_mat(p):
  ''' EXPRESSION_MAT : EXPRESSION_MAT OPERATOR_MAT EXPRESSION_MAT
                    | LPAREN EXPRESSION_MAT RPAREN
      EXPRESSION_MAT : DATANF
  '''
  p[0] = 'EXPRESSION_MAT'

def p_data_number_float(p):
  '''DATANF : NUMBER
            | FLOAT
            | ID
            | MINUS NUMBER
            | MINUS FLOAT
  '''
  p[0] = ('DATA', p[0])

# Permite reconocer una concatenacion de strings o arrays
def p_expression_concat(p):
  ''' EXPRESSION_CONCAT : EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT
      EXPRESSION_CONCAT : DATASTRING
                        | ARRAY

  '''
  p[0] = "EXPRESSION_CONCAT"


# Funciones que un String puede llamar
def p_functions_string(p):
  '''
  FUNCTIONS_STRING : DATASTRING POINT FUNCTIONS_ALLOWED_STRING

  FUNCTIONS_ALLOWED_STRING : INCLUDE QUESTION DATASTRING
                            | EMPTY QUESTION
                            | UPCASE
  '''
  p[0] = "FUNCTIONS_STRING"


def p_data_strings(p):
  '''DATASTRING : STRING
                | OTHERSTRINGDECLARATION
  '''
  p[0] = ('STRING', p[1])
  
# Permite reconocer arreglos
def p_array(p):
  '''ARRAY : ALFT ARGT
            | ALFT DATA ARGT
  '''
  if len(p) == 3:
    p[0] = ('ARRAY', p[1], p[2], p[3])
  elif len(p) == 2:
    p[0] = ('ARRAY', p[1], p[2])
  else:
    p[0] = ('ARRAY')


# Funciones que un array puede llamar
def p_funtions_array(p):
  '''FUNTIONS_ARRAY : ARRAY POINT FUNTIONS_ALLOWED_ARRAY

    FUNTIONS_ALLOWED_ARRAY : MIN
                          | FIRST
                          | MAP_ARRAY
  '''
  if len(p) == 3:
    p[0] = ('FUNTIONS_ARRAY', p[1], p[2], p[3])
  else:
    p[0] = ('FUNTIONS_ARRAY')


# Estructura para reconcer un map y el contenido permitido dentro de el.
def p_map_array(p):
  '''MAP_ARRAY : MAP OPENINGCB PIPE ID PIPE DATA_REPEAT_MAP CLOSURECB
                | MAP OPENINGCB CLOSURECB
                | MAP OPENINGCB DATA_REPEAT_MAP CLOSURECB

    DATA_REPEAT_MAP : DATA_ALLOWED_IN_MAP
                    | DATA_ALLOWED_IN_MAP DATA_REPEAT_MAP

    DATA_ALLOWED_IN_MAP : ASIGNATION
                        | EXPRESSION
  '''
  p[0] = "MAP"


# Permite reconocer Hash.
def p_hash(p):
  'HASH : OPENINGCB REGISTRY CLOSURECB'
  if len(p) == 3:
    p[0] = ('HASH', p[1], p[2], p[3])
  else:
    p[0] = ('HASH')


def p_registry(p):
  'REGISTRY : STRING HASHROCKET KEY'
  p[0] = ('REGISTRY', p[1], p[2], p[3])

def p_key(p):
  '''KEY : NUMBER
          | STRING
  '''
  p[0] = ('KEY', p[1])


# Funciones que un hash puede llamar
def p_funtions_hash(p):
  '''FUNTIONS_HASH : HASH POINT FUNTIONS_ALLOWED_HASH

    FUNTIONS_ALLOWED_HASH : HAS_VALUE QUESTION KEY
                          | MERGE LPAREN HASH RPAREN
                          | SIZE
  '''
  p[0] = "FUNTIONS_HASH"

def p_registry_any(p):
  'REGISTRY : REGISTRY COMMA REGISTRY'
  if len(p) == 3:
    p[0] = ('REGISTRY', p[1], p[2], p[3])
  else:
    p[0] = ('REGISTRY')


# Permite reconocer la estructura de control for
def p_structure_for(p):
  ' STRUCTURE_FOR : STRUCTURE_IN_FOR DATA_REPEAT END'

  if len(p) == 4:
    p[0] = ('FOR', p[1], p[2], p[3])
  else:
    p[0] = ('FOR')

def p_structure_initial_for(p):
  ''' STRUCTURE_IN_FOR : FOR ID IN ARRAY DO
                    | FOR ID IN ID DO
  '''
  p[0] = ('INITIAL', p[1], p[2], p[3], p[4], p[5])

def p_data_repeat_for(p):
  '''DATA_REPEAT : DATA_ALLOWED_IN_FOR
                  | DATA_ALLOWED_IN_FOR DATA_REPEAT
  '''
  if len(p) == 1:
    p[0] = ('DATA_IN_FOR', p[1])
  else:
    p[0] = ('DATA_IN_FOR')


def p_data_allowed_in_for(p):
  '''DATA_ALLOWED_IN_FOR : ASIGNATION
                          | EXPRESSION
  '''
  p[0] = ('DATA', p[1])

# Permite reconocer la estructura de control if
def p_structure_if(p):
  ''' STRUCTURE_IF : STRUCTURE_IN_IF DATA_REPEAT_IF END

      STRUCTURE_IN_IF : IF LPAREN DATANF OPERATOR_COMP_MAT DATANF RPAREN

      DATA_REPEAT_IF : DATA_ALLOWED_IN_IF
                  | DATA_ALLOWED_IN_IF DATA_REPEAT_IF
                  | DATA_ALLOWED_IN_IF ELSE DATA_ALLOWED_IN_IF

      DATA_ALLOWED_IN_IF : ASIGNATION
                        | EXPRESSION
  '''
  if len(p) == 4:
    p[0] = ('IF', p[1], p[2], p[3])
  else:
    p[0] = ('IF')


# Permite reconocer la estructura de control While
def p_structure_while(p):
  ''' STRUCTURE_WHILE : STRUCTURE_IN_WHILE DATA_REPEAT_W END

      STRUCTURE_IN_WHILE : WHILE LPAREN DATANF OPERATOR_COMP_MAT DATANF RPAREN

      DATA_REPEAT_W : DATA_ALLOWED_IN_WHILE
                  | DATA_ALLOWED_IN_WHILE DATA_REPEAT_W

      DATA_ALLOWED_IN_WHILE : ASIGNATION
                            | EXPRESSION
  '''
  if len(p) == 4:
    p[0] = ('WHILE', p[1], p[2], p[3])
  else:
    p[0] = ('WHILE')

def p_data(p):
  '''DATA : NUMBER
          | FLOAT
          | BOOLEAN
          | STRING
          | MINUS NUMBER
          | MINUS FLOAT
  '''
  p[0] = ('DATA', p[1])

def p_data_any(p):
  'DATA : DATA COMMA DATA'
  if len(p) == 3:
    p[0] = ('VALUE', p[1], p[2], p[3])
  else:
    p[0] = ('VALUE')

def p_boolean(p):
  '''BOOLEAN : TRUE
            | FALSE
            | LOGIC_NOT TRUE
            | LOGIC_NOT FALSE
  '''
  p[0] = ('BOOLEAN', p[1])

def p_operator_mat(p):
  '''OPERATOR_MAT : PLUS
                  | MINUS
                  | TIMES
                  | DIVIDE
                  | EXPONENTIATION
  '''
  p[0] = ('OPERATOR_MAT', p[1])



def p_operator_comp_mat(p):
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
  p[0] = ('OPERATOR_COMP_MAT', p[1])

def p_error(p):
  if p:
    return "Syntax error at token"
  else:
    return "Syntax error at EOF"

# Build the parser
parser = yacc.yacc()
