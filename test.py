import ast

entree = input(">>> ")
print(ast.dump(ast.parse(entree)))