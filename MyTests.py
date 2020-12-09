from itertools import permutations

from logic_utils import frozendict
from predicates.functions import _compile_term

from propositions.syntax import *
from propositions.semantics import *
from propositions.deduction import *
from propositions.proofs import *
from propositions.axiomatic_systems import *
from propositions.deduction_test import *
from propositions.tautology import *

from predicates.syntax import *
from predicates.functions import *

# Term._parse_prefix("plus(s(x),3)")
# print(Term._parse_prefix("plus(s(x),3)"))
# string = "plus(s(x),3)"
# split = string.index('(')
# root, args = string[:split], string[split:]
# print(root,args)
# args = args.strip("()").split(',')
# print(args)
#

# print(equality_to_relation(Formula.parse("z1=g(x,y,z)")))
# formula1 = Formula.parse("R(g(x),f(x))")
# formula2 = Formula.parse("R(plus(f(0),g(h(x))))")
# formula = formula2
# compiled_terms = list()
# for term in formula.arguments:
#     compiled_terms.extend(_compile_term(term))
# new_list = [*compiled_terms, create_relation_with_z(formula2, compiled_terms)]
# print(multiple_equality_to_relation(compiled_terms))
# print(new_list)
# print(concatenate_relation(new_list))
# print(replace_functions_with_relations_in_formula(formula2))

f=Formula.parse("Ax1[Ax2[Ay1[Ay2[(({eq}(x1,y1)&{eq}(x2,y2))->({r}(x1,x2)->{r}(y1,y2)))]]]]".format(eq="SAME", r='R'))
print(f)