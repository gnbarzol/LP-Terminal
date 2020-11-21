
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALFT AND ARGT ASIGN CLOSURECB COMMA DIVIDE DO ELSE EMPTY END EQUAL EQUAL_STRICT EXPONENTIATION FALSE FIRST FLOAT FOR GETS GREATER GREATER_THAN_OR_EQUAL HASHROCKET HAS_VALUE ID IF IN INCLUDE LOGIC_AND LOGIC_NOT LOGIC_OR LPAREN MAP MERGE MIN MINOR MINOR_THAN_OR_EQUAL MINUS NUMBER OPENINGCB OR OTHERSTRINGDECLARATION PIPE PLUS POINT PUTS QUESTION RPAREN SIZE STRING TIMES TRUE UPCASE WHILE STATEMENT : EXPRESSION\n                | ASIGNATION\n                | STRUCTURE_FOR\n  ASIGNATION : ID ASIGN EXPRESSION EXPRESSION : NUMBER \n                | FLOAT\n                | BOOLEAN\n                | STRING\n                | OTHERSTRINGDECLARATION\n                | ARRAY\n                | FUNTIONS_ARRAY\n                | LOGIC_NOT EXPRESSION\n                | EXPRESSION_MAT\n                | EXPRESSION_CONCAT\n                | PUTS EXPRESSION\n                | PUTS ID\n                | GETS\n   EXPRESSION : BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN\n                | DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING\n  EXPRESSION : DATANF OPERATOR_COMP_MAT DATANF EXPRESSION_MAT : EXPRESSION_MAT OPERATOR_MAT EXPRESSION_MAT\n                    | LPAREN EXPRESSION_MAT RPAREN\n      EXPRESSION_MAT : DATANF\n   EXPRESSION_CONCAT : EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT\n      EXPRESSION_CONCAT : DATASTRING\n                        | ARRAY\n  ARRAY : ALFT DATA ARGTFUNTIONS_ARRAY : ARRAY POINT FUNTIONS_ALLOWED_ARRAY\n\n    FUNTIONS_ALLOWED_ARRAY : MIN\n                          | FIRST\n                          | MAP_ARRAY\n  MAP_ARRAY : MAP OPENINGCB PIPE ID PIPE DATA_REPEAT_MAP CLOSURECB\n    \n    DATA_REPEAT_MAP : STATEMENT\n                    | STATEMENT DATA_REPEAT_MAP\n\n    DATA_ALLOWED_IN_MAP : ASIGNATION\n                        | EXPRESSION\n   STRUCTURE_FOR : STRUCTURE_IN_FOR DATA_REPEAT END\n\n      STRUCTURE_IN_FOR : FOR ID IN ARRAY DO\n                    | FOR ID IN ID DO\n\n      DATA_REPEAT : DATA_ALLOWED_IN_FOR\n                  | DATA_ALLOWED_IN_FOR DATA_REPEAT\n\n      DATA_ALLOWED_IN_FOR : ASIGNATION\n                          | EXPRESSION\n  DATA : NUMBER\n          | FLOAT\n          | BOOLEAN\n          | STRING\n  DATA : DATA COMMA DATADATANF : NUMBER \n            | FLOAT\n  DATASTRING : STRING \n                | OTHERSTRINGDECLARATION\n  BOOLEAN : TRUE\n            | FALSE\n  OPERATOR_MAT : PLUS\n                  | MINUS\n                  | TIMES\n                  | DIVIDE \n                  | EXPONENTIATION\n  OPERATOR_COMP_BOOLEAN : EQUAL\n                          | EQUAL_STRICT\n                          | LOGIC_AND\n                          | LOGIC_OR\n                          | PIPE\n  OPERATOR_COMP_MAT : EQUAL\n                      | EQUAL_STRICT\n                      | GREATER_THAN_OR_EQUAL\n                      | MINOR_THAN_OR_EQUAL\n                      | MINOR\n                      | GREATER \n                      | LOGIC_AND\n                      | LOGIC_OR\n                      | PIPE\n  '
    
_lr_action_items = {'DO':([78,90,91,],[-27,94,95,]),'EXPONENTIATION':([1,2,13,21,53,54,55,56,69,81,],[-49,27,-23,-50,-50,-49,-23,27,27,-22,]),'ASIGN':([16,],[57,]),'ARGT':([18,19,38,39,40,41,42,92,],[-53,-54,-47,-45,-44,-46,78,-48,]),'EQUAL':([1,10,13,18,19,21,23,24,25,],[-49,-51,47,-53,-54,-50,64,64,-52,]),'LOGIC_AND':([1,10,13,18,19,21,23,24,25,],[-49,-51,48,-53,-54,-50,65,65,-52,]),'EQUAL_STRICT':([1,10,13,18,19,21,23,24,25,],[-49,-51,49,-53,-54,-50,66,66,-52,]),'MINOR_THAN_OR_EQUAL':([1,13,21,],[-49,51,-50,]),'TRUE':([0,1,2,3,4,5,6,7,8,9,10,12,13,17,18,19,20,21,22,23,24,25,34,35,36,53,54,55,57,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,78,79,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[18,-5,-13,-11,-14,-2,-3,-17,-1,18,-8,18,-23,-10,-53,-54,18,-6,18,-25,-7,-9,-42,18,-43,-50,-49,-23,18,-15,-16,-12,-64,-63,-60,-62,-61,18,-21,-51,-25,-52,-26,-24,-37,-27,18,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,18,18,-32,]),'MINUS':([1,2,13,21,53,54,55,56,69,81,],[-49,31,-23,-50,-50,-49,-23,31,31,-22,]),'DIVIDE':([1,2,13,21,53,54,55,56,69,81,],[-49,26,-23,-50,-50,-49,-23,26,26,-22,]),'RPAREN':([53,54,55,56,69,81,],[-50,-49,-23,81,-21,-22,]),'LOGIC_OR':([1,10,13,18,19,21,23,24,25,],[-49,-51,45,-53,-54,-50,63,63,-52,]),'POINT':([17,78,],[58,-27,]),'MIN':([58,],[85,]),'PIPE':([1,10,13,18,19,21,23,24,25,93,97,],[-49,-51,43,-53,-54,-50,62,62,-52,96,98,]),'PLUS':([1,2,4,10,13,17,21,23,25,53,54,55,56,69,70,71,72,73,74,78,81,],[-49,29,32,-51,-23,-26,-50,-25,-52,-50,-49,-23,29,29,-51,-25,-52,-26,32,-27,-22,]),'COMMA':([18,19,38,39,40,41,42,92,],[-53,-54,-47,-45,-44,-46,79,79,]),'GETS':([0,1,2,3,4,5,6,7,8,9,10,13,17,18,19,20,21,22,23,24,25,34,35,36,53,54,55,57,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[7,-5,-13,-11,-14,-2,-3,-17,-1,7,-8,-23,-10,-53,-54,7,-6,7,-25,-7,-9,-42,7,-43,-50,-49,-23,7,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,7,7,-32,]),'$end':([1,2,3,4,5,6,7,8,10,13,14,17,18,19,21,23,24,25,53,54,55,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,102,],[-5,-13,-11,-14,-2,-3,-17,-1,-8,-23,0,-10,-53,-54,-6,-25,-7,-9,-50,-49,-23,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-32,]),'END':([1,2,3,4,7,10,13,17,18,19,21,23,24,25,33,34,35,36,53,54,55,59,60,61,69,70,71,72,73,74,76,78,80,81,82,84,85,86,87,88,89,102,],[-5,-13,-11,-14,-17,-8,-23,-10,-53,-54,-6,-25,-7,-9,75,-42,-40,-43,-50,-49,-23,-15,-16,-12,-21,-51,-25,-52,-26,-24,-41,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-32,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,12,13,17,18,19,20,21,22,23,24,25,32,34,35,36,53,54,55,57,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,78,79,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[10,-5,-13,-11,-14,-2,-3,-17,-1,10,-8,38,-23,-10,-53,-54,10,-6,10,-25,-7,-9,70,-42,10,-43,-50,-49,-23,10,-15,-16,-12,-64,-63,-60,-62,-61,70,-21,-51,-25,-52,-26,-24,-37,-27,38,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,10,10,-32,]),'FOR':([0,1,2,3,4,5,6,7,8,10,13,17,18,19,21,23,24,25,53,54,55,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,98,99,102,],[11,-5,-13,-11,-14,-2,-3,-17,-1,-8,-23,-10,-53,-54,-6,-25,-7,-9,-50,-49,-23,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,11,11,-32,]),'CLOSURECB':([1,2,3,4,5,6,7,8,10,13,17,18,19,21,23,24,25,53,54,55,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,99,100,101,102,],[-5,-13,-11,-14,-2,-3,-17,-1,-8,-23,-10,-53,-54,-6,-25,-7,-9,-50,-49,-23,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-33,102,-34,-32,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,12,13,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,60,61,69,70,71,72,73,74,75,78,79,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[1,-5,-13,-11,-14,-2,-3,-17,-1,1,-8,40,-23,54,-10,-53,-54,1,-6,1,-25,-7,-9,-58,-59,-57,-55,54,-56,-42,1,-43,-73,-70,-72,54,-65,-71,-66,-67,-68,-69,-50,-49,-23,1,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,40,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,1,1,-32,]),'ALFT':([0,1,2,3,4,5,6,7,8,9,10,13,17,18,19,20,21,22,23,24,25,32,34,35,36,53,54,55,57,59,60,61,69,70,71,72,73,74,75,77,78,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[12,-5,-13,-11,-14,-2,-3,-17,-1,12,-8,-23,-10,-53,-54,12,-6,12,-25,-7,-9,12,-42,12,-43,-50,-49,-23,12,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,12,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,12,12,-32,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,13,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,53,54,55,57,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[15,-5,-13,-11,-14,-2,-3,-17,-1,15,-8,-23,15,-10,-53,-54,15,-6,15,-25,-7,-9,-58,-59,-57,-55,15,-56,-42,15,-43,-50,-49,-23,15,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,15,15,-32,]),'IN':([37,],[77,]),'TIMES':([1,2,13,21,53,54,55,56,69,81,],[-49,28,-23,-50,-50,-49,-23,28,28,-22,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,13,17,18,19,20,21,23,24,25,34,35,36,53,54,55,59,60,61,69,70,71,72,73,74,75,77,78,80,81,82,84,85,86,87,88,89,94,95,96,98,99,102,],[16,-5,-13,-11,-14,-2,-3,-17,-1,16,-8,37,-23,-10,-53,-54,60,-6,-25,-7,-9,-42,16,-43,-50,-49,-23,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,91,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,97,16,16,-32,]),'MINOR':([1,13,21,],[-49,52,-50,]),'FIRST':([58,],[87,]),'MAP':([58,],[83,]),'OPENINGCB':([83,],[93,]),'FALSE':([0,1,2,3,4,5,6,7,8,9,10,12,13,17,18,19,20,21,22,23,24,25,34,35,36,53,54,55,57,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,78,79,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[19,-5,-13,-11,-14,-2,-3,-17,-1,19,-8,19,-23,-10,-53,-54,19,-6,19,-25,-7,-9,-42,19,-43,-50,-49,-23,19,-15,-16,-12,-64,-63,-60,-62,-61,19,-21,-51,-25,-52,-26,-24,-37,-27,19,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,19,19,-32,]),'GREATER':([1,13,21,],[-49,44,-50,]),'PUTS':([0,1,2,3,4,5,6,7,8,9,10,13,17,18,19,20,21,22,23,24,25,34,35,36,53,54,55,57,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[20,-5,-13,-11,-14,-2,-3,-17,-1,20,-8,-23,-10,-53,-54,20,-6,20,-25,-7,-9,-42,20,-43,-50,-49,-23,20,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,20,20,-32,]),'GREATER_THAN_OR_EQUAL':([1,13,21,],[-49,50,-50,]),'FLOAT':([0,1,2,3,4,5,6,7,8,9,10,12,13,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,34,35,36,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,60,61,69,70,71,72,73,74,75,78,79,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[21,-5,-13,-11,-14,-2,-3,-17,-1,21,-8,39,-23,53,-10,-53,-54,21,-6,21,-25,-7,-9,-58,-59,-57,-55,53,-56,-42,21,-43,-73,-70,-72,53,-65,-71,-66,-67,-68,-69,-50,-49,-23,21,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,39,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,21,21,-32,]),'LOGIC_NOT':([0,1,2,3,4,5,6,7,8,9,10,13,17,18,19,20,21,22,23,24,25,34,35,36,53,54,55,57,59,60,61,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[22,-5,-13,-11,-14,-2,-3,-17,-1,22,-8,-23,-10,-53,-54,22,-6,22,-25,-7,-9,-42,22,-43,-50,-49,-23,22,-15,-16,-12,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,22,22,-32,]),'OTHERSTRINGDECLARATION':([0,1,2,3,4,5,6,7,8,9,10,13,17,18,19,20,21,22,23,24,25,32,34,35,36,53,54,55,57,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,78,80,81,82,84,85,86,87,88,89,94,95,98,99,102,],[25,-5,-13,-11,-14,-2,-3,-17,-1,25,-8,-23,-10,-53,-54,25,-6,25,-25,-7,-9,72,-42,25,-43,-50,-49,-23,25,-15,-16,-12,-64,-63,-60,-62,-61,72,-21,-51,-25,-52,-26,-24,-37,-27,-20,-22,-4,-28,-29,-31,-30,-19,-18,-38,-39,25,25,-32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'OPERATOR_COMP_BOOLEAN':([23,24,],[67,68,]),'STRUCTURE_IN_FOR':([0,98,99,],[9,9,9,]),'DATA_REPEAT':([9,35,],[33,76,]),'FUNTIONS_ARRAY':([0,9,20,22,35,57,98,99,],[3,3,3,3,3,3,3,3,]),'FUNTIONS_ALLOWED_ARRAY':([58,],[84,]),'OPERATOR_COMP_MAT':([13,],[46,]),'EXPRESSION':([0,9,20,22,35,57,98,99,],[8,36,59,61,36,82,8,8,]),'DATA_ALLOWED_IN_FOR':([9,35,],[35,35,]),'ASIGNATION':([0,9,35,98,99,],[5,34,34,5,5,]),'DATASTRING':([0,9,20,22,32,35,57,67,98,99,],[23,23,23,23,71,23,23,88,23,23,]),'DATANF':([0,9,15,20,22,30,35,46,57,98,99,],[13,13,55,13,13,55,13,80,13,13,13,]),'BOOLEAN':([0,9,12,20,22,35,57,68,79,98,99,],[24,24,41,24,24,24,24,89,41,24,24,]),'STATEMENT':([0,98,99,],[14,99,99,]),'EXPRESSION_MAT':([0,9,15,20,22,30,35,57,98,99,],[2,2,56,2,2,69,2,2,2,2,]),'MAP_ARRAY':([58,],[86,]),'STRUCTURE_FOR':([0,98,99,],[6,6,6,]),'OPERATOR_MAT':([2,56,69,],[30,30,30,]),'EXPRESSION_CONCAT':([0,9,20,22,32,35,57,98,99,],[4,4,4,4,74,4,4,4,4,]),'ARRAY':([0,9,20,22,32,35,57,77,98,99,],[17,17,17,17,73,17,17,90,17,17,]),'DATA_REPEAT_MAP':([98,99,],[100,101,]),'DATA':([12,79,],[42,92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> STATEMENT","S'",1,None,None,None),
  ('STATEMENT -> EXPRESSION','STATEMENT',1,'p_STATEMENT','sintactico.py',7),
  ('STATEMENT -> ASIGNATION','STATEMENT',1,'p_STATEMENT','sintactico.py',8),
  ('STATEMENT -> STRUCTURE_FOR','STATEMENT',1,'p_STATEMENT','sintactico.py',9),
  ('ASIGNATION -> ID ASIGN EXPRESSION','ASIGNATION',3,'p_ASIGNATION','sintactico.py',13),
  ('EXPRESSION -> NUMBER','EXPRESSION',1,'p_EXPRESSION','sintactico.py',17),
  ('EXPRESSION -> FLOAT','EXPRESSION',1,'p_EXPRESSION','sintactico.py',18),
  ('EXPRESSION -> BOOLEAN','EXPRESSION',1,'p_EXPRESSION','sintactico.py',19),
  ('EXPRESSION -> STRING','EXPRESSION',1,'p_EXPRESSION','sintactico.py',20),
  ('EXPRESSION -> OTHERSTRINGDECLARATION','EXPRESSION',1,'p_EXPRESSION','sintactico.py',21),
  ('EXPRESSION -> ARRAY','EXPRESSION',1,'p_EXPRESSION','sintactico.py',22),
  ('EXPRESSION -> FUNTIONS_ARRAY','EXPRESSION',1,'p_EXPRESSION','sintactico.py',23),
  ('EXPRESSION -> LOGIC_NOT EXPRESSION','EXPRESSION',2,'p_EXPRESSION','sintactico.py',24),
  ('EXPRESSION -> EXPRESSION_MAT','EXPRESSION',1,'p_EXPRESSION','sintactico.py',25),
  ('EXPRESSION -> EXPRESSION_CONCAT','EXPRESSION',1,'p_EXPRESSION','sintactico.py',26),
  ('EXPRESSION -> PUTS EXPRESSION','EXPRESSION',2,'p_EXPRESSION','sintactico.py',27),
  ('EXPRESSION -> PUTS ID','EXPRESSION',2,'p_EXPRESSION','sintactico.py',28),
  ('EXPRESSION -> GETS','EXPRESSION',1,'p_EXPRESSION','sintactico.py',29),
  ('EXPRESSION -> BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN','EXPRESSION',3,'p_EXPRESSION_COMP_BOOLEAN','sintactico.py',35),
  ('EXPRESSION -> DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING','EXPRESSION',3,'p_EXPRESSION_COMP_BOOLEAN','sintactico.py',36),
  ('EXPRESSION -> DATANF OPERATOR_COMP_MAT DATANF','EXPRESSION',3,'p_EXPRESSION_COMP_MAT','sintactico.py',42),
  ('EXPRESSION_MAT -> EXPRESSION_MAT OPERATOR_MAT EXPRESSION_MAT','EXPRESSION_MAT',3,'p_EXPRESSION_MAT','sintactico.py',47),
  ('EXPRESSION_MAT -> LPAREN EXPRESSION_MAT RPAREN','EXPRESSION_MAT',3,'p_EXPRESSION_MAT','sintactico.py',48),
  ('EXPRESSION_MAT -> DATANF','EXPRESSION_MAT',1,'p_EXPRESSION_MAT','sintactico.py',49),
  ('EXPRESSION_CONCAT -> EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT','EXPRESSION_CONCAT',3,'p_EXPRESSION_CONCAT','sintactico.py',55),
  ('EXPRESSION_CONCAT -> DATASTRING','EXPRESSION_CONCAT',1,'p_EXPRESSION_CONCAT','sintactico.py',56),
  ('EXPRESSION_CONCAT -> ARRAY','EXPRESSION_CONCAT',1,'p_EXPRESSION_CONCAT','sintactico.py',57),
  ('ARRAY -> ALFT DATA ARGT','ARRAY',3,'p_ARRAY','sintactico.py',62),
  ('FUNTIONS_ARRAY -> ARRAY POINT FUNTIONS_ALLOWED_ARRAY','FUNTIONS_ARRAY',3,'p_FUNTIONS_ARRAY','sintactico.py',67),
  ('FUNTIONS_ALLOWED_ARRAY -> MIN','FUNTIONS_ALLOWED_ARRAY',1,'p_FUNTIONS_ARRAY','sintactico.py',69),
  ('FUNTIONS_ALLOWED_ARRAY -> FIRST','FUNTIONS_ALLOWED_ARRAY',1,'p_FUNTIONS_ARRAY','sintactico.py',70),
  ('FUNTIONS_ALLOWED_ARRAY -> MAP_ARRAY','FUNTIONS_ALLOWED_ARRAY',1,'p_FUNTIONS_ARRAY','sintactico.py',71),
  ('MAP_ARRAY -> MAP OPENINGCB PIPE ID PIPE DATA_REPEAT_MAP CLOSURECB','MAP_ARRAY',7,'p_MAP_ARRAY','sintactico.py',76),
  ('DATA_REPEAT_MAP -> STATEMENT','DATA_REPEAT_MAP',1,'p_MAP_ARRAY','sintactico.py',78),
  ('DATA_REPEAT_MAP -> STATEMENT DATA_REPEAT_MAP','DATA_REPEAT_MAP',2,'p_MAP_ARRAY','sintactico.py',79),
  ('DATA_ALLOWED_IN_MAP -> ASIGNATION','DATA_ALLOWED_IN_MAP',1,'p_MAP_ARRAY','sintactico.py',81),
  ('DATA_ALLOWED_IN_MAP -> EXPRESSION','DATA_ALLOWED_IN_MAP',1,'p_MAP_ARRAY','sintactico.py',82),
  ('STRUCTURE_FOR -> STRUCTURE_IN_FOR DATA_REPEAT END','STRUCTURE_FOR',3,'p_STRUCTURE_FOR','sintactico.py',87),
  ('STRUCTURE_IN_FOR -> FOR ID IN ARRAY DO','STRUCTURE_IN_FOR',5,'p_STRUCTURE_FOR','sintactico.py',89),
  ('STRUCTURE_IN_FOR -> FOR ID IN ID DO','STRUCTURE_IN_FOR',5,'p_STRUCTURE_FOR','sintactico.py',90),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_FOR','DATA_REPEAT',1,'p_STRUCTURE_FOR','sintactico.py',92),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_FOR DATA_REPEAT','DATA_REPEAT',2,'p_STRUCTURE_FOR','sintactico.py',93),
  ('DATA_ALLOWED_IN_FOR -> ASIGNATION','DATA_ALLOWED_IN_FOR',1,'p_STRUCTURE_FOR','sintactico.py',95),
  ('DATA_ALLOWED_IN_FOR -> EXPRESSION','DATA_ALLOWED_IN_FOR',1,'p_STRUCTURE_FOR','sintactico.py',96),
  ('DATA -> NUMBER','DATA',1,'p_DATA','sintactico.py',100),
  ('DATA -> FLOAT','DATA',1,'p_DATA','sintactico.py',101),
  ('DATA -> BOOLEAN','DATA',1,'p_DATA','sintactico.py',102),
  ('DATA -> STRING','DATA',1,'p_DATA','sintactico.py',103),
  ('DATA -> DATA COMMA DATA','DATA',3,'p_DATA_ANY','sintactico.py',108),
  ('DATANF -> NUMBER','DATANF',1,'p_DATA_NUMBER_FLOAT','sintactico.py',111),
  ('DATANF -> FLOAT','DATANF',1,'p_DATA_NUMBER_FLOAT','sintactico.py',112),
  ('DATASTRING -> STRING','DATASTRING',1,'p_DATA_STRINGS','sintactico.py',117),
  ('DATASTRING -> OTHERSTRINGDECLARATION','DATASTRING',1,'p_DATA_STRINGS','sintactico.py',118),
  ('BOOLEAN -> TRUE','BOOLEAN',1,'p_BOOLEAN','sintactico.py',123),
  ('BOOLEAN -> FALSE','BOOLEAN',1,'p_BOOLEAN','sintactico.py',124),
  ('OPERATOR_MAT -> PLUS','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',129),
  ('OPERATOR_MAT -> MINUS','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',130),
  ('OPERATOR_MAT -> TIMES','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',131),
  ('OPERATOR_MAT -> DIVIDE','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',132),
  ('OPERATOR_MAT -> EXPONENTIATION','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',133),
  ('OPERATOR_COMP_BOOLEAN -> EQUAL','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',138),
  ('OPERATOR_COMP_BOOLEAN -> EQUAL_STRICT','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',139),
  ('OPERATOR_COMP_BOOLEAN -> LOGIC_AND','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',140),
  ('OPERATOR_COMP_BOOLEAN -> LOGIC_OR','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',141),
  ('OPERATOR_COMP_BOOLEAN -> PIPE','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',142),
  ('OPERATOR_COMP_MAT -> EQUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',147),
  ('OPERATOR_COMP_MAT -> EQUAL_STRICT','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',148),
  ('OPERATOR_COMP_MAT -> GREATER_THAN_OR_EQUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',149),
  ('OPERATOR_COMP_MAT -> MINOR_THAN_OR_EQUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',150),
  ('OPERATOR_COMP_MAT -> MINOR','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',151),
  ('OPERATOR_COMP_MAT -> GREATER','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',152),
  ('OPERATOR_COMP_MAT -> LOGIC_AND','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',153),
  ('OPERATOR_COMP_MAT -> LOGIC_OR','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',154),
  ('OPERATOR_COMP_MAT -> PIPE','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',155),
]