
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALFT AND ARGT ASIGN CLOSURECB COMMA DIVIDE DO ELSE EMPTY END EQUAL EQUAL_STRICT EXPONENTIATION FALSE FIRST FLOAT FOR GETS GREATER GREATER_THAN_OR_EQUAL HASHROCKET HAS_VALUE ID IF IN INCLUDE LOGIC_AND LOGIC_NOT LOGIC_OR LPAREN MAP MERGE MIN MINOR MINOR_THAN_OR_EQUAL MINUS NUMBER OPENINGCB OR OTHERSTRINGDECLARATION PIPE PLUS POINT PUTS QUESTION RPAREN SIZE STRING TIMES TRUE UPCASE WHILE STATEMENT : EXPRESSION\n                | ASIGNATION\n                | STRUCTURE_FOR\n                | STRUCTURE_IF\n                | STRUCTURE_WHILE\n  ASIGNATION : ID ASIGN EXPRESSION EXPRESSION : NUMBER\n                | FLOAT\n                | BOOLEAN\n                | STRING\n                | OTHERSTRINGDECLARATION\n                | ARRAY\n                | HASH\n                | FUNTIONS_ARRAY\n                | FUNTIONS_HASH\n                | LOGIC_NOT EXPRESSION\n                | EXPRESSION_MAT\n                | EXPRESSION_CONCAT\n                | PUTS EXPRESSION\n                | PUTS ID\n                | GETS EXPRESSION\n                | FUNCTIONS_STRING\n   EXPRESSION : BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN\n                | DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING\n  OPERATOR_COMP_BOOLEAN : EQUAL\n                          | EQUAL_STRICT\n                          | LOGIC_AND\n                          | LOGIC_OR\n                          | PIPE\n\n  EXPRESSION : DATANF OPERATOR_COMP_MAT DATANF EXPRESSION_MAT : EXPRESSION_MAT OPERATOR_MAT EXPRESSION_MAT\n                    | LPAREN EXPRESSION_MAT RPAREN\n      EXPRESSION_MAT : DATANF\n  DATANF : NUMBER\n            | FLOAT\n            | ID\n   EXPRESSION_CONCAT : EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT\n      EXPRESSION_CONCAT : DATASTRING\n                        | ARRAY\n\n  DATASTRING : STRING\n                | OTHERSTRINGDECLARATION\n  \n  FUNCTIONS_STRING : DATASTRING POINT FUNCTIONS_ALLOWED_STRING\n\n  FUNCTIONS_ALLOWED_STRING : INCLUDE QUESTION DATASTRING\n                            | EMPTY QUESTION\n                            | UPCASE\n  ARRAY : ALFT DATA ARGTFUNTIONS_ARRAY : ARRAY POINT FUNTIONS_ALLOWED_ARRAY\n\n    FUNTIONS_ALLOWED_ARRAY : MIN\n                          | FIRST\n                          | MAP_ARRAY\n  MAP_ARRAY : MAP OPENINGCB PIPE ID PIPE DATA_REPEAT_MAP CLOSURECB\n\n    DATA_REPEAT_MAP : STATEMENT\n                    | STATEMENT DATA_REPEAT_MAP\n\n    DATA_ALLOWED_IN_MAP : ASIGNATION\n                        | EXPRESSION\n  HASH : OPENINGCB REGISTRY CLOSURECBREGISTRY : STRING HASHROCKET KEYKEY : NUMBER\n          | STRING\n  FUNTIONS_HASH : HASH POINT FUNTIONS_ALLOWED_HASH\n\n    FUNTIONS_ALLOWED_HASH : HAS_VALUE QUESTION KEY\n                          | MERGE LPAREN HASH RPAREN\n                          | SIZE\n  REGISTRY : REGISTRY COMMA REGISTRY STRUCTURE_FOR : STRUCTURE_IN_FOR DATA_REPEAT END\n\n      STRUCTURE_IN_FOR : FOR ID IN ARRAY DO\n                    | FOR ID IN ID DO\n\n      DATA_REPEAT : DATA_ALLOWED_IN_FOR\n                  | DATA_ALLOWED_IN_FOR DATA_REPEAT\n\n      DATA_ALLOWED_IN_FOR : ASIGNATION\n                          | EXPRESSION\n   STRUCTURE_IF : STRUCTURE_IN_IF DATA_REPEAT END\n\n      STRUCTURE_IN_IF : IF LPAREN BOOLEAN RPAREN\n\n      DATA_REPEAT : DATA_ALLOWED_IN_IF\n                  | DATA_ALLOWED_IN_IF DATA_REPEAT\n                  | DATA_ALLOWED_IN_IF ELSE DATA_ALLOWED_IN_IF\n\n      DATA_ALLOWED_IN_IF : ASIGNATION\n                        | EXPRESSION\n   STRUCTURE_WHILE : STRUCTURE_IN_WHILE DATA_REPEAT END\n\n      STRUCTURE_IN_WHILE : WHILE LPAREN TRUE RPAREN\n\n      DATA_REPEAT : DATA_ALLOWED_IN_WHILE\n                  | DATA_ALLOWED_IN_WHILE DATA_REPEAT\n\n      DATA_ALLOWED_IN_WHILE : ASIGNATION\n                            | EXPRESSION\n  DATA : NUMBER\n          | FLOAT\n          | BOOLEAN\n          | STRING\n  DATA : DATA COMMA DATABOOLEAN : TRUE\n            | FALSE\n            | LOGIC_NOT TRUE\n            | LOGIC_NOT FALSE\n  OPERATOR_MAT : PLUS\n                  | MINUS\n                  | TIMES\n                  | DIVIDE\n                  | EXPONENTIATION\n  OPERATOR_COMP_MAT : EQUAL\n                      | EQUAL_STRICT\n                      | GREATER_THAN_OR_EQUAL\n                      | MINOR_THAN_OR_EQUAL\n                      | MINOR\n                      | GREATER\n                      | LOGIC_AND\n                      | LOGIC_OR\n                      | PIPE\n  '
    
_lr_action_items = {'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,44,45,46,47,48,49,50,51,52,53,55,56,57,58,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,125,126,127,128,130,131,136,139,145,147,150,151,153,155,156,157,159,160,162,163,],[7,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,7,-17,-18,7,-36,7,-22,-38,-33,7,7,7,-90,-91,80,89,-16,-90,-91,-36,89,-94,-95,-96,-97,-98,-19,-20,7,-21,89,-99,-100,-101,-102,-103,-104,-105,-106,-107,7,7,7,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,7,-72,-79,-46,80,-92,-93,-56,147,-32,147,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,7,7,-51,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,44,45,46,47,48,49,50,51,52,53,55,56,57,58,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,125,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[8,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,8,-17,-18,8,-36,8,-22,-38,-33,8,8,8,-90,-91,81,90,-16,-90,-91,-36,90,-94,-95,-96,-97,-98,-19,-20,8,-21,90,-99,-100,-101,-102,-103,-104,-105,-106,-107,8,8,8,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,8,-72,-79,-46,81,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,8,8,-51,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,37,38,39,40,41,44,45,46,47,54,55,56,57,58,59,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,125,126,127,128,129,130,131,136,138,139,145,147,150,151,153,155,156,157,159,160,162,163,],[10,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,10,-17,-18,10,-36,10,-22,-38,-33,10,10,10,-90,-91,83,86,-25,-26,-27,-28,-29,-16,-90,-91,-36,108,-19,-20,10,-21,108,10,10,10,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,10,-72,-79,-46,83,-92,-93,-56,86,145,-32,145,108,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,10,10,-51,]),'OTHERSTRINGDECLARATION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,37,38,39,40,41,44,45,46,47,54,55,56,57,58,59,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,138,139,145,147,150,151,153,155,156,157,159,160,162,163,],[11,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,11,-17,-18,11,-36,11,-22,-38,-33,11,11,11,-90,-91,-25,-26,-27,-28,-29,-16,-90,-91,-36,109,-19,-20,11,-21,109,11,11,11,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,11,-72,-79,-46,-92,-93,-56,-32,109,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,11,11,-51,]),'LOGIC_NOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,36,37,38,39,40,41,44,45,46,47,55,56,57,58,72,73,74,75,76,88,89,90,92,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,125,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[16,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,16,-17,-18,16,-36,16,-22,-38,-33,16,16,16,-90,-91,84,84,-25,-26,-27,-28,-29,-16,-90,-91,-36,-19,-20,16,-21,16,16,16,-70,-71,-33,-34,-35,84,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,16,-72,-79,-46,84,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,16,16,-51,]),'PUTS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,44,45,46,47,55,56,57,58,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[19,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,19,-17,-18,19,-36,19,-22,-38,-33,19,19,19,-90,-91,-16,-90,-91,-36,-19,-20,19,-21,19,19,19,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,19,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,19,19,-51,]),'GETS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,44,45,46,47,55,56,57,58,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[21,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,21,-17,-18,21,-36,21,-22,-38,-33,21,21,21,-90,-91,-16,-90,-91,-36,-19,-20,21,-21,21,21,21,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,21,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,21,21,-51,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,33,44,45,46,47,48,49,50,51,52,53,55,56,57,58,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,132,139,145,147,150,151,152,153,155,156,157,159,160,162,163,],[20,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,47,-17,-18,56,-36,47,-22,-38,-33,20,20,20,-90,-91,47,91,-16,-90,-91,-36,47,-94,-95,-96,-97,-98,-19,-20,47,-21,47,-99,-100,-101,-102,-103,-104,-105,-106,-107,20,20,20,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,20,-72,-79,-46,-92,-93,-56,-32,148,-44,-59,-58,-73,-80,158,-61,-43,-67,-66,-62,20,20,-51,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,36,37,38,39,40,41,44,45,46,47,55,56,57,58,72,73,74,75,76,84,88,89,90,92,93,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,125,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[28,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,45,-17,-18,28,-36,28,-22,-38,-33,28,28,28,-90,-91,28,28,-25,-26,-27,-28,-29,-16,-90,-91,-36,-19,-20,28,-21,28,28,28,-70,-71,126,-33,-34,-35,28,134,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,28,-72,-79,-46,28,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,28,28,-51,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,36,37,38,39,40,41,44,45,46,47,55,56,57,58,72,73,74,75,76,84,88,89,90,92,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,125,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[29,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,46,-17,-18,29,-36,29,-22,-38,-33,29,29,29,-90,-91,29,29,-25,-26,-27,-28,-29,-16,-90,-91,-36,-19,-20,29,-21,29,29,29,-70,-71,127,-33,-34,-35,29,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,29,-72,-79,-46,29,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,29,29,-51,]),'ALFT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,44,45,46,47,54,55,56,57,58,72,73,74,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,132,139,145,147,150,151,153,155,156,157,159,160,162,163,],[30,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,30,-17,-18,30,-36,30,-22,-38,-33,30,30,30,-90,-91,-16,-90,-91,-36,30,-19,-20,30,-21,30,30,30,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,30,-72,-79,-46,-92,-93,-56,-32,30,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,30,30,-51,]),'OPENINGCB':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,44,45,46,47,55,56,57,58,72,73,74,75,76,88,89,90,94,95,96,97,98,99,100,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,137,139,145,147,150,151,153,155,156,157,159,160,162,163,],[31,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,31,-17,-18,31,-36,31,-22,-38,-33,31,31,31,-90,-91,-16,-90,-91,-36,-19,-20,31,-21,31,31,31,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,135,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,31,-72,-79,-46,-92,-93,-56,-32,31,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,31,31,-51,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,34,35,44,45,46,47,48,49,50,51,52,53,55,56,57,58,72,73,74,75,76,88,89,90,94,95,96,97,98,100,102,103,104,105,106,107,108,109,110,111,112,115,116,117,120,122,123,124,126,127,128,131,139,145,147,150,151,153,155,156,157,159,160,162,163,],[32,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,32,-17,-18,32,-36,32,-22,-38,-33,32,32,32,-90,-91,32,92,93,-16,-90,-91,-36,32,-94,-95,-96,-97,-98,-19,-20,32,-21,32,32,32,-70,-71,-33,-34,-35,-23,-47,-48,-49,-50,-60,137,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,32,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-73,-80,-61,-43,-67,-66,-62,32,32,-51,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,122,123,124,126,127,128,131,139,145,147,153,155,159,160,162,163,],[33,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-61,-43,-62,33,33,-51,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,122,123,124,126,127,128,131,139,145,147,153,155,159,160,162,163,],[34,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-61,-43,-62,34,34,-51,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,122,123,124,126,127,128,131,139,145,147,153,155,159,160,162,163,],[35,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-61,-43,-62,35,35,-51,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,122,123,124,126,127,128,131,139,145,147,153,155,159,163,],[0,-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,-72,-79,-46,-92,-93,-56,-32,-44,-59,-58,-61,-43,-62,-51,]),'CLOSURECB':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,85,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,117,122,123,124,126,127,128,131,139,144,145,146,147,153,155,159,161,162,163,164,],[-1,-2,-3,-4,-5,-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,128,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-65,-72,-79,-46,-92,-93,-56,-32,-44,-64,-59,-57,-58,-61,-43,-62,163,-52,-51,-53,]),'END':([7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,71,72,73,74,75,76,77,78,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,118,119,121,124,126,127,128,131,139,140,141,142,145,147,153,155,159,163,],[-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,117,-68,-74,-81,-70,-71,122,123,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-69,-75,-82,-46,-92,-93,-56,-32,-44,-76,-77,-78,-59,-58,-61,-43,-62,-51,]),'ELSE':([7,8,9,10,11,12,13,14,15,17,18,20,22,23,24,28,29,44,45,46,47,55,56,58,73,75,76,88,89,90,94,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,115,116,124,126,127,128,131,139,145,147,153,155,159,163,],[-7,-8,-9,-10,-11,-12,-13,-14,-15,-17,-18,-36,-22,-38,-33,-90,-91,-16,-90,-91,-36,-19,-20,-21,120,-77,-78,-33,-34,-35,-23,-47,-48,-49,-50,-60,-63,-31,-37,-38,-39,-40,-41,-6,-24,-42,-45,-30,-46,-92,-93,-56,-32,-44,-59,-58,-61,-43,-62,-51,]),'EQUAL':([7,8,9,10,11,20,23,24,28,29,45,46,47,56,],[-34,-35,37,-40,-41,-36,37,62,-90,-91,-90,-91,-36,-36,]),'EQUAL_STRICT':([7,8,9,10,11,20,23,24,28,29,45,46,47,56,],[-34,-35,38,-40,-41,-36,38,63,-90,-91,-90,-91,-36,-36,]),'GREATER_THAN_OR_EQUAL':([7,8,20,24,47,56,],[-34,-35,-36,64,-36,-36,]),'MINOR_THAN_OR_EQUAL':([7,8,20,24,47,56,],[-34,-35,-36,65,-36,-36,]),'MINOR':([7,8,20,24,47,56,],[-34,-35,-36,66,-36,-36,]),'GREATER':([7,8,20,24,47,56,],[-34,-35,-36,67,-36,-36,]),'LOGIC_AND':([7,8,9,10,11,20,23,24,28,29,45,46,47,56,],[-34,-35,39,-40,-41,-36,39,68,-90,-91,-90,-91,-36,-36,]),'LOGIC_OR':([7,8,9,10,11,20,23,24,28,29,45,46,47,56,],[-34,-35,40,-40,-41,-36,40,69,-90,-91,-90,-91,-36,-36,]),'PIPE':([7,8,9,10,11,20,23,24,28,29,45,46,47,56,135,158,],[-34,-35,41,-40,-41,-36,41,70,-90,-91,-90,-91,-36,-36,152,160,]),'PLUS':([7,8,10,11,12,17,18,20,23,24,47,56,87,88,89,90,104,105,106,107,108,109,124,131,],[-34,-35,-40,-41,-39,49,54,-36,-38,-33,-36,-36,49,-33,-34,-35,49,54,-38,-39,-40,-41,-46,-32,]),'MINUS':([7,8,17,20,24,47,56,87,88,89,90,104,131,],[-34,-35,50,-36,-33,-36,-36,50,-33,-34,-35,50,-32,]),'TIMES':([7,8,17,20,24,47,56,87,88,89,90,104,131,],[-34,-35,51,-36,-33,-36,-36,51,-33,-34,-35,51,-32,]),'DIVIDE':([7,8,17,20,24,47,56,87,88,89,90,104,131,],[-34,-35,52,-36,-33,-36,-36,52,-33,-34,-35,52,-32,]),'EXPONENTIATION':([7,8,17,20,24,47,56,87,88,89,90,104,131,],[-34,-35,53,-36,-33,-36,-36,53,-33,-34,-35,53,-32,]),'POINT':([10,11,12,13,23,124,128,],[-40,-41,42,43,60,-46,-56,]),'ASIGN':([20,],[57,]),'ARGT':([28,29,79,80,81,82,83,126,127,143,],[-90,-91,124,-85,-86,-87,-88,-92,-93,-89,]),'COMMA':([28,29,79,80,81,82,83,85,126,127,143,144,145,146,147,],[-90,-91,125,-85,-86,-87,-88,129,-92,-93,125,129,-59,-57,-58,]),'RPAREN':([28,29,47,87,88,89,90,104,126,127,128,131,133,134,154,],[-90,-91,-36,131,-33,-34,-35,-31,-92,-93,-56,-32,150,151,159,]),'MIN':([42,],[96,]),'FIRST':([42,],[97,]),'MAP':([42,],[99,]),'HAS_VALUE':([43,],[101,]),'MERGE':([43,],[102,]),'SIZE':([43,],[103,]),'INCLUDE':([60,],[113,]),'EMPTY':([60,],[114,]),'UPCASE':([60,],[115,]),'HASHROCKET':([86,],[130,]),'IN':([91,],[132,]),'QUESTION':([101,113,114,],[136,138,139,]),'DO':([124,148,149,],[-46,156,157,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'STATEMENT':([0,160,162,],[1,162,162,]),'EXPRESSION':([0,16,19,21,25,26,27,57,72,73,74,120,160,162,],[2,44,55,58,76,76,76,110,76,76,76,142,2,2,]),'ASIGNATION':([0,25,26,27,72,73,74,120,160,162,],[3,75,75,75,75,75,75,141,3,3,]),'STRUCTURE_FOR':([0,160,162,],[4,4,4,]),'STRUCTURE_IF':([0,160,162,],[5,5,5,]),'STRUCTURE_WHILE':([0,160,162,],[6,6,6,]),'BOOLEAN':([0,16,19,21,25,26,27,30,36,57,72,73,74,92,120,125,160,162,],[9,9,9,9,9,9,9,82,94,9,9,9,9,133,9,82,9,9,]),'ARRAY':([0,16,19,21,25,26,27,54,57,72,73,74,120,132,160,162,],[12,12,12,12,12,12,12,107,12,12,12,12,12,149,12,12,]),'HASH':([0,16,19,21,25,26,27,57,72,73,74,120,137,160,162,],[13,13,13,13,13,13,13,13,13,13,13,13,154,13,13,]),'FUNTIONS_ARRAY':([0,16,19,21,25,26,27,57,72,73,74,120,160,162,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'FUNTIONS_HASH':([0,16,19,21,25,26,27,57,72,73,74,120,160,162,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'EXPRESSION_MAT':([0,16,19,21,25,26,27,32,48,57,72,73,74,120,160,162,],[17,17,17,17,17,17,17,87,104,17,17,17,17,17,17,17,]),'EXPRESSION_CONCAT':([0,16,19,21,25,26,27,54,57,72,73,74,120,160,162,],[18,18,18,18,18,18,18,105,18,18,18,18,18,18,18,]),'FUNCTIONS_STRING':([0,16,19,21,25,26,27,57,72,73,74,120,160,162,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'DATASTRING':([0,16,19,21,25,26,27,54,57,59,72,73,74,120,138,160,162,],[23,23,23,23,23,23,23,106,23,111,23,23,23,23,155,23,23,]),'DATANF':([0,16,19,21,25,26,27,32,48,57,61,72,73,74,120,160,162,],[24,24,24,24,24,24,24,88,88,24,116,24,24,24,24,24,24,]),'STRUCTURE_IN_FOR':([0,160,162,],[25,25,25,]),'STRUCTURE_IN_IF':([0,160,162,],[26,26,26,]),'STRUCTURE_IN_WHILE':([0,160,162,],[27,27,27,]),'OPERATOR_COMP_BOOLEAN':([9,23,],[36,59,]),'OPERATOR_MAT':([17,87,104,],[48,48,48,]),'OPERATOR_COMP_MAT':([24,],[61,]),'DATA_REPEAT':([25,26,27,72,73,74,],[71,77,78,118,119,121,]),'DATA_ALLOWED_IN_FOR':([25,26,27,72,73,74,],[72,72,72,72,72,72,]),'DATA_ALLOWED_IN_IF':([25,26,27,72,73,74,120,],[73,73,73,73,73,73,140,]),'DATA_ALLOWED_IN_WHILE':([25,26,27,72,73,74,],[74,74,74,74,74,74,]),'DATA':([30,125,],[79,143,]),'REGISTRY':([31,129,],[85,144,]),'FUNTIONS_ALLOWED_ARRAY':([42,],[95,]),'MAP_ARRAY':([42,],[98,]),'FUNTIONS_ALLOWED_HASH':([43,],[100,]),'FUNCTIONS_ALLOWED_STRING':([60,],[112,]),'KEY':([130,136,],[146,153,]),'DATA_REPEAT_MAP':([160,162,],[161,164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> STATEMENT","S'",1,None,None,None),
  ('STATEMENT -> EXPRESSION','STATEMENT',1,'p_STATEMENT','sintactico.py',8),
  ('STATEMENT -> ASIGNATION','STATEMENT',1,'p_STATEMENT','sintactico.py',9),
  ('STATEMENT -> STRUCTURE_FOR','STATEMENT',1,'p_STATEMENT','sintactico.py',10),
  ('STATEMENT -> STRUCTURE_IF','STATEMENT',1,'p_STATEMENT','sintactico.py',11),
  ('STATEMENT -> STRUCTURE_WHILE','STATEMENT',1,'p_STATEMENT','sintactico.py',12),
  ('ASIGNATION -> ID ASIGN EXPRESSION','ASIGNATION',3,'p_ASIGNATION','sintactico.py',16),
  ('EXPRESSION -> NUMBER','EXPRESSION',1,'p_EXPRESSION','sintactico.py',21),
  ('EXPRESSION -> FLOAT','EXPRESSION',1,'p_EXPRESSION','sintactico.py',22),
  ('EXPRESSION -> BOOLEAN','EXPRESSION',1,'p_EXPRESSION','sintactico.py',23),
  ('EXPRESSION -> STRING','EXPRESSION',1,'p_EXPRESSION','sintactico.py',24),
  ('EXPRESSION -> OTHERSTRINGDECLARATION','EXPRESSION',1,'p_EXPRESSION','sintactico.py',25),
  ('EXPRESSION -> ARRAY','EXPRESSION',1,'p_EXPRESSION','sintactico.py',26),
  ('EXPRESSION -> HASH','EXPRESSION',1,'p_EXPRESSION','sintactico.py',27),
  ('EXPRESSION -> FUNTIONS_ARRAY','EXPRESSION',1,'p_EXPRESSION','sintactico.py',28),
  ('EXPRESSION -> FUNTIONS_HASH','EXPRESSION',1,'p_EXPRESSION','sintactico.py',29),
  ('EXPRESSION -> LOGIC_NOT EXPRESSION','EXPRESSION',2,'p_EXPRESSION','sintactico.py',30),
  ('EXPRESSION -> EXPRESSION_MAT','EXPRESSION',1,'p_EXPRESSION','sintactico.py',31),
  ('EXPRESSION -> EXPRESSION_CONCAT','EXPRESSION',1,'p_EXPRESSION','sintactico.py',32),
  ('EXPRESSION -> PUTS EXPRESSION','EXPRESSION',2,'p_EXPRESSION','sintactico.py',33),
  ('EXPRESSION -> PUTS ID','EXPRESSION',2,'p_EXPRESSION','sintactico.py',34),
  ('EXPRESSION -> GETS EXPRESSION','EXPRESSION',2,'p_EXPRESSION','sintactico.py',35),
  ('EXPRESSION -> FUNCTIONS_STRING','EXPRESSION',1,'p_EXPRESSION','sintactico.py',36),
  ('EXPRESSION -> BOOLEAN OPERATOR_COMP_BOOLEAN BOOLEAN','EXPRESSION',3,'p_EXPRESSION_COMP_BOOLEAN','sintactico.py',42),
  ('EXPRESSION -> DATASTRING OPERATOR_COMP_BOOLEAN DATASTRING','EXPRESSION',3,'p_EXPRESSION_COMP_BOOLEAN','sintactico.py',43),
  ('OPERATOR_COMP_BOOLEAN -> EQUAL','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',48),
  ('OPERATOR_COMP_BOOLEAN -> EQUAL_STRICT','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',49),
  ('OPERATOR_COMP_BOOLEAN -> LOGIC_AND','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',50),
  ('OPERATOR_COMP_BOOLEAN -> LOGIC_OR','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',51),
  ('OPERATOR_COMP_BOOLEAN -> PIPE','OPERATOR_COMP_BOOLEAN',1,'p_OPERATOR_COMP_BOOLEAN','sintactico.py',52),
  ('EXPRESSION -> DATANF OPERATOR_COMP_MAT DATANF','EXPRESSION',3,'p_EXPRESSION_COMP_MAT','sintactico.py',59),
  ('EXPRESSION_MAT -> EXPRESSION_MAT OPERATOR_MAT EXPRESSION_MAT','EXPRESSION_MAT',3,'p_EXPRESSION_MAT','sintactico.py',64),
  ('EXPRESSION_MAT -> LPAREN EXPRESSION_MAT RPAREN','EXPRESSION_MAT',3,'p_EXPRESSION_MAT','sintactico.py',65),
  ('EXPRESSION_MAT -> DATANF','EXPRESSION_MAT',1,'p_EXPRESSION_MAT','sintactico.py',66),
  ('DATANF -> NUMBER','DATANF',1,'p_DATA_NUMBER_FLOAT','sintactico.py',71),
  ('DATANF -> FLOAT','DATANF',1,'p_DATA_NUMBER_FLOAT','sintactico.py',72),
  ('DATANF -> ID','DATANF',1,'p_DATA_NUMBER_FLOAT','sintactico.py',73),
  ('EXPRESSION_CONCAT -> EXPRESSION_CONCAT PLUS EXPRESSION_CONCAT','EXPRESSION_CONCAT',3,'p_EXPRESSION_CONCAT','sintactico.py',79),
  ('EXPRESSION_CONCAT -> DATASTRING','EXPRESSION_CONCAT',1,'p_EXPRESSION_CONCAT','sintactico.py',80),
  ('EXPRESSION_CONCAT -> ARRAY','EXPRESSION_CONCAT',1,'p_EXPRESSION_CONCAT','sintactico.py',81),
  ('DATASTRING -> STRING','DATASTRING',1,'p_DATA_STRINGS','sintactico.py',86),
  ('DATASTRING -> OTHERSTRINGDECLARATION','DATASTRING',1,'p_DATA_STRINGS','sintactico.py',87),
  ('FUNCTIONS_STRING -> DATASTRING POINT FUNCTIONS_ALLOWED_STRING','FUNCTIONS_STRING',3,'p_FUNCTIONS_STRING','sintactico.py',94),
  ('FUNCTIONS_ALLOWED_STRING -> INCLUDE QUESTION DATASTRING','FUNCTIONS_ALLOWED_STRING',3,'p_FUNCTIONS_STRING','sintactico.py',96),
  ('FUNCTIONS_ALLOWED_STRING -> EMPTY QUESTION','FUNCTIONS_ALLOWED_STRING',2,'p_FUNCTIONS_STRING','sintactico.py',97),
  ('FUNCTIONS_ALLOWED_STRING -> UPCASE','FUNCTIONS_ALLOWED_STRING',1,'p_FUNCTIONS_STRING','sintactico.py',98),
  ('ARRAY -> ALFT DATA ARGT','ARRAY',3,'p_ARRAY','sintactico.py',103),
  ('FUNTIONS_ARRAY -> ARRAY POINT FUNTIONS_ALLOWED_ARRAY','FUNTIONS_ARRAY',3,'p_FUNTIONS_ARRAY','sintactico.py',108),
  ('FUNTIONS_ALLOWED_ARRAY -> MIN','FUNTIONS_ALLOWED_ARRAY',1,'p_FUNTIONS_ARRAY','sintactico.py',110),
  ('FUNTIONS_ALLOWED_ARRAY -> FIRST','FUNTIONS_ALLOWED_ARRAY',1,'p_FUNTIONS_ARRAY','sintactico.py',111),
  ('FUNTIONS_ALLOWED_ARRAY -> MAP_ARRAY','FUNTIONS_ALLOWED_ARRAY',1,'p_FUNTIONS_ARRAY','sintactico.py',112),
  ('MAP_ARRAY -> MAP OPENINGCB PIPE ID PIPE DATA_REPEAT_MAP CLOSURECB','MAP_ARRAY',7,'p_MAP_ARRAY','sintactico.py',117),
  ('DATA_REPEAT_MAP -> STATEMENT','DATA_REPEAT_MAP',1,'p_MAP_ARRAY','sintactico.py',119),
  ('DATA_REPEAT_MAP -> STATEMENT DATA_REPEAT_MAP','DATA_REPEAT_MAP',2,'p_MAP_ARRAY','sintactico.py',120),
  ('DATA_ALLOWED_IN_MAP -> ASIGNATION','DATA_ALLOWED_IN_MAP',1,'p_MAP_ARRAY','sintactico.py',122),
  ('DATA_ALLOWED_IN_MAP -> EXPRESSION','DATA_ALLOWED_IN_MAP',1,'p_MAP_ARRAY','sintactico.py',123),
  ('HASH -> OPENINGCB REGISTRY CLOSURECB','HASH',3,'p_HASH','sintactico.py',128),
  ('REGISTRY -> STRING HASHROCKET KEY','REGISTRY',3,'p_REGISTRY','sintactico.py',133),
  ('KEY -> NUMBER','KEY',1,'p_KEY','sintactico.py',137),
  ('KEY -> STRING','KEY',1,'p_KEY','sintactico.py',138),
  ('FUNTIONS_HASH -> HASH POINT FUNTIONS_ALLOWED_HASH','FUNTIONS_HASH',3,'p_FUNTIONS_HASH','sintactico.py',145),
  ('FUNTIONS_ALLOWED_HASH -> HAS_VALUE QUESTION KEY','FUNTIONS_ALLOWED_HASH',3,'p_FUNTIONS_HASH','sintactico.py',147),
  ('FUNTIONS_ALLOWED_HASH -> MERGE LPAREN HASH RPAREN','FUNTIONS_ALLOWED_HASH',4,'p_FUNTIONS_HASH','sintactico.py',148),
  ('FUNTIONS_ALLOWED_HASH -> SIZE','FUNTIONS_ALLOWED_HASH',1,'p_FUNTIONS_HASH','sintactico.py',149),
  ('REGISTRY -> REGISTRY COMMA REGISTRY','REGISTRY',3,'p_REGISTRY_ANY','sintactico.py',153),
  ('STRUCTURE_FOR -> STRUCTURE_IN_FOR DATA_REPEAT END','STRUCTURE_FOR',3,'p_STRUCTURE_FOR','sintactico.py',157),
  ('STRUCTURE_IN_FOR -> FOR ID IN ARRAY DO','STRUCTURE_IN_FOR',5,'p_STRUCTURE_FOR','sintactico.py',159),
  ('STRUCTURE_IN_FOR -> FOR ID IN ID DO','STRUCTURE_IN_FOR',5,'p_STRUCTURE_FOR','sintactico.py',160),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_FOR','DATA_REPEAT',1,'p_STRUCTURE_FOR','sintactico.py',162),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_FOR DATA_REPEAT','DATA_REPEAT',2,'p_STRUCTURE_FOR','sintactico.py',163),
  ('DATA_ALLOWED_IN_FOR -> ASIGNATION','DATA_ALLOWED_IN_FOR',1,'p_STRUCTURE_FOR','sintactico.py',165),
  ('DATA_ALLOWED_IN_FOR -> EXPRESSION','DATA_ALLOWED_IN_FOR',1,'p_STRUCTURE_FOR','sintactico.py',166),
  ('STRUCTURE_IF -> STRUCTURE_IN_IF DATA_REPEAT END','STRUCTURE_IF',3,'p_STRUCTURE_IF','sintactico.py',171),
  ('STRUCTURE_IN_IF -> IF LPAREN BOOLEAN RPAREN','STRUCTURE_IN_IF',4,'p_STRUCTURE_IF','sintactico.py',173),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_IF','DATA_REPEAT',1,'p_STRUCTURE_IF','sintactico.py',175),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_IF DATA_REPEAT','DATA_REPEAT',2,'p_STRUCTURE_IF','sintactico.py',176),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_IF ELSE DATA_ALLOWED_IN_IF','DATA_REPEAT',3,'p_STRUCTURE_IF','sintactico.py',177),
  ('DATA_ALLOWED_IN_IF -> ASIGNATION','DATA_ALLOWED_IN_IF',1,'p_STRUCTURE_IF','sintactico.py',179),
  ('DATA_ALLOWED_IN_IF -> EXPRESSION','DATA_ALLOWED_IN_IF',1,'p_STRUCTURE_IF','sintactico.py',180),
  ('STRUCTURE_WHILE -> STRUCTURE_IN_WHILE DATA_REPEAT END','STRUCTURE_WHILE',3,'p_STRUCTURE_WHILE','sintactico.py',185),
  ('STRUCTURE_IN_WHILE -> WHILE LPAREN TRUE RPAREN','STRUCTURE_IN_WHILE',4,'p_STRUCTURE_WHILE','sintactico.py',187),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_WHILE','DATA_REPEAT',1,'p_STRUCTURE_WHILE','sintactico.py',189),
  ('DATA_REPEAT -> DATA_ALLOWED_IN_WHILE DATA_REPEAT','DATA_REPEAT',2,'p_STRUCTURE_WHILE','sintactico.py',190),
  ('DATA_ALLOWED_IN_WHILE -> ASIGNATION','DATA_ALLOWED_IN_WHILE',1,'p_STRUCTURE_WHILE','sintactico.py',192),
  ('DATA_ALLOWED_IN_WHILE -> EXPRESSION','DATA_ALLOWED_IN_WHILE',1,'p_STRUCTURE_WHILE','sintactico.py',193),
  ('DATA -> NUMBER','DATA',1,'p_DATA','sintactico.py',198),
  ('DATA -> FLOAT','DATA',1,'p_DATA','sintactico.py',199),
  ('DATA -> BOOLEAN','DATA',1,'p_DATA','sintactico.py',200),
  ('DATA -> STRING','DATA',1,'p_DATA','sintactico.py',201),
  ('DATA -> DATA COMMA DATA','DATA',3,'p_DATA_ANY','sintactico.py',206),
  ('BOOLEAN -> TRUE','BOOLEAN',1,'p_BOOLEAN','sintactico.py',210),
  ('BOOLEAN -> FALSE','BOOLEAN',1,'p_BOOLEAN','sintactico.py',211),
  ('BOOLEAN -> LOGIC_NOT TRUE','BOOLEAN',2,'p_BOOLEAN','sintactico.py',212),
  ('BOOLEAN -> LOGIC_NOT FALSE','BOOLEAN',2,'p_BOOLEAN','sintactico.py',213),
  ('OPERATOR_MAT -> PLUS','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',218),
  ('OPERATOR_MAT -> MINUS','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',219),
  ('OPERATOR_MAT -> TIMES','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',220),
  ('OPERATOR_MAT -> DIVIDE','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',221),
  ('OPERATOR_MAT -> EXPONENTIATION','OPERATOR_MAT',1,'p_OPERATOR_MAT','sintactico.py',222),
  ('OPERATOR_COMP_MAT -> EQUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',229),
  ('OPERATOR_COMP_MAT -> EQUAL_STRICT','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',230),
  ('OPERATOR_COMP_MAT -> GREATER_THAN_OR_EQUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',231),
  ('OPERATOR_COMP_MAT -> MINOR_THAN_OR_EQUAL','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',232),
  ('OPERATOR_COMP_MAT -> MINOR','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',233),
  ('OPERATOR_COMP_MAT -> GREATER','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',234),
  ('OPERATOR_COMP_MAT -> LOGIC_AND','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',235),
  ('OPERATOR_COMP_MAT -> LOGIC_OR','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',236),
  ('OPERATOR_COMP_MAT -> PIPE','OPERATOR_COMP_MAT',1,'p_OPERATOR_COMP_MAT','sintactico.py',237),
]
