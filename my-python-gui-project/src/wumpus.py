import random
from tkinter import Label

def add_wumpus_and_stench(main_window):
    num_wumpus = random.randint(1, 2)
    main_window.wumpus = []
    for _ in range(num_wumpus):
        while True:
            row = random.randint(0, main_window.rows - 1)
            column = random.randint(0, main_window.columns - 1)
            if (row, column) not in main_window.pits and (row, column) not in main_window.gold and (row, column) not in main_window.wumpus and (row, column) != (0, 0):
                main_window.wumpus.append((row, column))
                main_window.cells[(row, column)].config(bg="red")  # Representa el Wumpus con color rojo
                add_stench(main_window, row, column)
                break

def add_stench(main_window, row, column):
    adjacent_cells = [
        (row-1, column), (row+1, column),
        (row, column-1), (row, column+1)
    ]
    for r, c in adjacent_cells:
        if 0 <= r < main_window.rows and 0 <= c < main_window.columns:
            if (r, c) not in main_window.wumpus:
                main_window.cells[(r, c)].stench = True  # Marca la celda como adyacente a un Wumpus

def show_stench(main_window, row, column):
    adjacent_cells = [
        (row-1, column), (row+1, column),
        (row, column-1), (row, column+1)
    ]
    for r, c in adjacent_cells:
        if 0 <= r < main_window.rows and 0 <= c < main_window.columns:
            if hasattr(main_window.cells[(r, c)], 'stench') and main_window.cells[(r, c)].stench:
                if not hasattr(main_window.cells[(r, c)], 'stench_label'):
                    label = Label(main_window.cells[(r, c)], text="H", bg="gray")
                    label.pack(expand=True)
                    main_window.cells[(r, c)].stench_label = label  # Guarda la referencia para evitar el garbage collector