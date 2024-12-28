import os
from tkinter import Label, PhotoImage, messagebox

def add_image_to_cell(main_window, row, column):
    if (row, column) in main_window.cells:
        # Obtener directorio del archivo actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Subir un nivel para llegar a la raíz del proyecto
        project_root = os.path.dirname(current_dir)
        # Construir ruta relativa a la imagen
        image_path = os.path.join(project_root, "images", "player_facing_to_down.png")
        
        if not os.path.exists(image_path):
            messagebox.showerror("Error", f"No se encontró la imagen en: {image_path}")
            return

        image = PhotoImage(file=image_path)
        label = Label(main_window.cells[(row, column)], image=image)
        label.image = image
        label.pack(expand=True)
        main_window.current_image_label = label