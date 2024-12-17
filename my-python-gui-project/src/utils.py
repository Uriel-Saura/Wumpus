from tkinter import Frame

def paint_cells(grid_frame, rows, columns):
    for row in range(rows):
        for column in range(columns):
            if (row + column) % 2 == 0:  # Ejemplo de condición para pintar algunas celdas
                cell = Frame(grid_frame, bg="yellow", borderwidth=1, relief="solid")
                cell.grid(row=row, column=column, sticky="nsew")