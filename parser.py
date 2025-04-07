from ply.lex import lex
from ply.yacc import yacc
from operators import And, Or, Operand
from atoms import Atom

def create_operation(cls, a, b):
    return cls(a, b)

tokens = (
   "AND_OP",
   "OR_OP",
   "TERM",
   'LPAREN',
   'RPAREN',
)

t_AND_OP = r'AND'
t_OR_OP   = r'OR'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_TERM = r'True|False'

def t_SEPARATOR(t):
    r'\s+'
    pass  # discard separators


# Build the lexer
lexer = lex()

def p_expression_or(p):
    'expression : expression OR_OP expression'
    p[0] = Or(p[1], p[3])


def p_expression_and(p):
    '''expression : expression AND_OP expression'''
    p[0] = And(p[1], p[3])


 
def p_expression_unary(p):
    '''expression : factor'''
    p[0] = p[1]    
    

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_term(p):
    '''factor : TERM'''
    res = True if p[1] == "True" else False
    p[0] = Atom(res)
    

data = "(True OR False) AND (True AND True)"

parser = yacc(debug=True)

result = parser.parse(data)

print(result.calculate())