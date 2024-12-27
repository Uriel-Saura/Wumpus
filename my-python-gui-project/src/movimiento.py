from tkinter import messagebox
from pozos import show_breeze
from wumpus import show_stench

def move_image(main_window, new_row, new_column):
    if main_window.game_over:
        return

    if (new_row, new_column) in main_window.pits:
        messagebox.showinfo("Fin del juego", "¡Has caído en un pozo! Fin del juego.")
        main_window.game_over = True
        return

    if (new_row, new_column) in main_window.wumpus:
        messagebox.showinfo("Fin del juego", "¡Has sido devorado por el Wumpus! Fin del juego.")
        main_window.game_over = True
        return

    # Movimiento físico de la imagen
    main_window.current_image_label.pack_forget()
    main_window.add_image_to_cell(new_row, new_column)
    main_window.current_position = (new_row, new_column)

     # Cambiar color de la nueva celda
    main_window.cells[(new_row, new_column)].config(bg="lightblue")


    # Mostrar efectos visuales
    show_breeze(main_window, new_row, new_column)
    show_stench(main_window, new_row, new_column)