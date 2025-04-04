from ply.lex import lex
from ply.yacc import yacc

tokens = ("AND", "OR", "BOOL")

t_AND = r"AND"
t_OR = r"OR"
t_BOOL = r"True|False"
