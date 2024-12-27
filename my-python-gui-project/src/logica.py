def evaluar_expresion(expression, truth_assignment):
    """Evalúa una expresión lógica con una asignación de verdad."""
    if isinstance(expression, bool):
        return expression
    if isinstance(expression, str):
        resultado = truth_assignment.get(expression, False)
        return resultado
    op, *args = expression
    if op == 'NOT':
        resultado = not evaluar_expresion(args[0], truth_assignment)
        return resultado
    if op == 'AND':
        resultado = all(evaluar_expresion(arg, truth_assignment) for arg in args)
        return resultado
    if op == 'OR':
        resultado = any(evaluar_expresion(arg, truth_assignment) for arg in args)
        return resultado

def generar_tabla_verdad(variables):
    """Genera tabla de verdad para las variables dadas."""
    n = len(variables)
    tabla = []
    for i in range(2**n):
        row = {}
        for j, var in enumerate(variables):
            row[var] = bool((i >> j) & 1)
        tabla.append(row)
    return tabla