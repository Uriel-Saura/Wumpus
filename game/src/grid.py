# src/grid.py
from tkinter import Frame

def create_grid(main_window, rows, columns):
    main_window.cells = {}
    for row in range(rows):
        for column in range(columns):
            cell = Frame(main_window.grid_frame, borderwidth=1, relief="solid", bg="gray")
            cell.grid(row=row, column=column, sticky="nsew")
            main_window.cells[(row, column)] = cell

    for row in range(rows):
        main_window.grid_frame.grid_rowconfigure(row, weight=1)
    for column in range(columns):
        main_window.grid_frame.grid_columnconfigure(column, weight=1)