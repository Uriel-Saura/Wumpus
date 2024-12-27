import random

def get_posiciones_prohibidas(main_window):
    """Obtiene todas las posiciones donde no puede aparecer oro"""
    prohibidas = set()
    # Posición inicial
    prohibidas.add((0,0))
    
    # Añadir pozos y sus adyacentes (brisas)
    for x, y in main_window.pits:
        prohibidas.add((x,y))
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < main_window.rows and 0 <= ny < main_window.columns:
                prohibidas.add((nx,ny))
                
    # Añadir wumpus y sus adyacentes (hedores)
    for x, y in main_window.wumpus:
        prohibidas.add((x,y))
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < main_window.rows and 0 <= ny < main_window.columns:
                prohibidas.add((nx,ny))
                
    return prohibidas

def add_gold_and_glow(main_window):
    num_gold = random.randint(1,1)
    main_window.gold = []
    posiciones_prohibidas = get_posiciones_prohibidas(main_window)
    
    for _ in range(num_gold):
        posiciones_disponibles = []
        for row in range(main_window.rows):
            for col in range(main_window.columns):
                if (row,col) not in posiciones_prohibidas:
                    posiciones_disponibles.append((row,col))
        
        if posiciones_disponibles:
            row, column = random.choice(posiciones_disponibles)
            main_window.gold.append((row, column))
            main_window.cells[(row, column)].config(bg="yellow")
            add_glow(main_window, row, column)

def add_glow(main_window, row, column):
    main_window.cells[(row, column)].config(bg="yellow")

def recoger_oro(main_window):
    row, column = main_window.current_position
    if (row, column) in main_window.gold:
        main_window.gold.remove((row, column))
        main_window.cells[(row, column)].config(bg="yellow")
        return True
    return False
