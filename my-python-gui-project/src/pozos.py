import random
from tkinter import Label

def add_pits_and_breeze(main_window):
    num_pits = random.randint(1, 2)
    main_window.pits = []
    for _ in range(num_pits):
        while True:
            row = random.randint(0, main_window.rows - 1)
            column = random.randint(0, main_window.columns - 1)
            if (row, column) not in main_window.pits and (row, column) != (0, 0):
                if not any((r, c) in main_window.pits for r, c in get_adjacent_cells(row, column, main_window.rows, main_window.columns)):
                    main_window.pits.append((row, column))
                    main_window.cells[(row, column)].config(bg="black")  # Representa el pozo con color negro
                    add_breeze(main_window, row, column)
                    break

def get_adjacent_cells(row, column, max_rows, max_columns):
    adjacent_cells = [
        (row-1, column), (row+1, column),
        (row, column-1), (row, column+1)
    ]
    return [(r, c) for r, c in adjacent_cells if 0 <= r < max_rows and 0 <= c < max_columns]

def add_breeze(main_window, row, column):
    adjacent_cells = get_adjacent_cells(row, column, main_window.rows, main_window.columns)
    for r, c in adjacent_cells:
        if (r, c) not in main_window.pits:
            main_window.cells[(r, c)].breeze = True  # Marca la celda como adyacente a un pozo

def show_breeze(main_window, row, column):
    adjacent_cells = get_adjacent_cells(row, column, main_window.rows, main_window.columns)
    for r, c in adjacent_cells:
        if hasattr(main_window.cells[(r, c)], 'breeze') and main_window.cells[(r, c)].breeze:
            if not hasattr(main_window.cells[(r, c)], 'breeze_label'):
                label = Label(main_window.cells[(r, c)], text="B", bg="white")
                label.pack(expand=True)
                main_window.cells[(r, c)].breeze_label = label  # Guarda la referencia para evitar el garbage collector