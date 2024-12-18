import random

def add_gold_and_glow(main_window):
    num_gold = random.randint(2, 6)
    main_window.gold = []
    for _ in range(num_gold):
        while True:
            row = random.randint(0, main_window.rows - 1)
            column = random.randint(0, main_window.columns - 1)
            if (row, column) not in main_window.pits and (row, column) not in main_window.gold and (row, column) != (0, 0):
                main_window.gold.append((row, column))
                main_window.cells[(row, column)].config(bg="gray")  # Representa el oro con color amarillo
                add_glow(main_window, row, column)
                break

def add_glow(main_window, row, column):
    main_window.cells[(row, column)].config(bg="gray")  # Representa el resplandor con color dorado

def recoger_oro(main_window):
    row, column = main_window.current_position
    if (row, column) in main_window.gold:
        main_window.gold.remove((row, column))
        main_window.cells[(row, column)].config(bg="gray")  # Regresa la celda a su estado original
        return True
    return False
