
output = ""

# exemple d'entrée : lambda x : x + 1
function = input(">>> ")

# traitements de l'entrée des arguments
arguments = [x for x in function.split("lambda")[1].split(":")[0].split(" ") if x != ""]
ARGS = {argument: input(f"{argument} >>> ") for argument in arguments}
fonction_courante = function.split(":")[1].strip()
ast_stack = [{"type": "value", "value": element} for i, element in zip(range(len(fonction_courante.split(" "))), fonction_courante.split(" ")) if element not in ["+",]]

ast_stack = ast_stack[::-1]
for i, element in zip(range(len(fonction_courante.split(" "))), fonction_courante.split(" ")):
    if element == "+":
        element_1 = ast_stack.pop()
        element_2 = ast_stack.pop()
        ast_stack.append({"type": "operation", "operation": element, "element_1": element_1, "element_2": element_2})

def remplacer_arguments(element):
    if element["type"] == "value" and element["value"] in ARGS:
        element["value"] = ARGS[element["value"]]
    if element["type"] == "operation":
        element["element_1"] = remplacer_arguments(element["element_1"])
        element["element_2"] = remplacer_arguments(element["element_2"])
    return element
print(ast_stack)
remplacer_arguments(ast_stack[0])

def executer_operation(operation, element_1, element_2):
    match operation:
        case "+":
            if str(element_1).isnumeric() and str(element_2).isnumeric():
                return int(element_1) + int(element_2)

def executer_fonction(element):
    if element["type"] == "value":
        return element["value"]
    if element["type"] == "operation":
        return executer_operation(element["operation"], executer_fonction(element["element_1"]), executer_fonction(element["element_2"]))
output = executer_fonction(ast_stack[0])
print(f"résultat : {output}")