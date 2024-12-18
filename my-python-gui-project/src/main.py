import os
from tkinter import Tk, Frame, simpledialog, Label, PhotoImage, messagebox
from movimiento import handle_keypress, move_image
from pozos import add_pits_and_breeze, show_breeze
from oro import add_gold_and_glow, recoger_oro
from wumpus import add_wumpus_and_stench, show_stench
from agente import Agente

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Mi Aplicación GUI")
        self.ask_grid_size()
        self.setup_ui()
        self.add_image_to_cell(0, 0)  # Cambiado a la celda (0, 0)
        self.current_position = (0, 0)
        self.game_over = False
        self.pits = []  # Inicializa los pozos
        self.gold = []  # Inicializa el oro
        self.wumpus = []  # Inicializa los Wumpus

        # Preguntar al usuario si quiere jugar él mismo o si quiere que el agente resuelva el juego
        self.ask_player_or_agent()

    def ask_player_or_agent(self):
        choice = messagebox.askyesno("Modo de Juego", "¿Quieres jugar tú mismo? (Sí) o ¿Quieres que el agente resuelva el juego? (No)")
        if choice:
            self.master.bind("<Key>", lambda event: handle_keypress(event, self))
            self.master.bind("<space>", lambda event: self.handle_space())
        else:
            self.agente = Agente(self)
            self.agente.resolver_juego()

        add_pits_and_breeze(self)
        add_gold_and_glow(self)
        add_wumpus_and_stench(self)

    def ask_grid_size(self):
        self.rows = simpledialog.askinteger("Input", "Número de filas:", minvalue=1, maxvalue=100)
        self.columns = simpledialog.askinteger("Input", "Número de columnas:", minvalue=1, maxvalue=100)

    def setup_ui(self):
        self.grid_frame = Frame(self.master)
        self.grid_frame.pack(fill="both", expand=True)
        self.create_grid(self.rows, self.columns)

    def create_grid(self, rows, columns):
        self.cells = {}
        for row in range(rows):
            for column in range(columns):
                cell = Frame(self.grid_frame, borderwidth=1, relief="solid", bg="gray")  # Establece el color de fondo a gris
                cell.grid(row=row, column=column, sticky="nsew")
                self.cells[(row, column)] = cell

        for row in range(rows):
            self.grid_frame.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            self.grid_frame.grid_columnconfigure(column, weight=1)

    def add_image_to_cell(self, row, column):
        if (row, column) in self.cells:
            image_path = "C:/users/uriel/Documents/Wumpus/my-python-gui-project/images/player_facing_to_down.png"
            if not os.path.exists(image_path):
                messagebox.showerror("Error", f"No se encontró la imagen en: {image_path}")
                return
            
            # Carga la imagen
            image = PhotoImage(file=image_path)
            label = Label(self.cells[(row, column)], image=image)
            label.image = image  # Evita que la imagen sea recolectada por el garbage collector
            label.pack(expand=True)
            self.current_image_label = label

    def move_image(self, new_row, new_column):
        if self.game_over:
            return

        if (new_row, new_column) in self.pits:
            messagebox.showinfo("Fin del juego", "¡Has caído en un pozo! Fin del juego.")
            self.game_over = True
            return

        if (new_row, new_column) in self.wumpus:
            messagebox.showinfo("Fin del juego", "¡Has sido devorado por el Wumpus! Fin del juego.")
            self.game_over = True
            return

        # Regresa la celda anterior a su color original si tenía oro
        old_row, old_column = self.current_position
        if (old_row, old_column) in self.gold:
            self.cells[(old_row, old_column)].config(bg="yellow")
        else:
            self.cells[(old_row, old_column)].config(bg="green")

        move_image(self, new_row, new_column)
        show_breeze(self, new_row, new_column)  # Muestra la brisa en las celdas adyacentes
        show_stench(self, new_row, new_column)  # Muestra el hedor en las celdas adyacentes

    def handle_space(self):
        if recoger_oro(self):
            messagebox.showinfo("Oro recogido", "¡Has recogido el oro!")
            if not self.gold:  # Si no quedan más oros
                messagebox.showinfo("Victoria", "¡Has recolectado todos los oros! ¡Has ganado el juego!")
                self.game_over = True

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()