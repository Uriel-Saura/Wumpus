from tkinter import Tk, Frame, simpledialog, Label, PhotoImage, messagebox
from movimiento import move_image
from agente import Agente
from grid import create_grid 
from add_image import add_image_to_cell

# Agregar los imports que muestran brisas, hedores y oro
from pozos import add_pits_and_breeze
from wumpus import add_wumpus_and_stench
from oro import add_gold_and_glow

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Mi Aplicación GUI")
        
        # Pedimos los tamaños del grid
        self.ask_grid_size()

        self.game_over = False
        self.gold = []

        # Configuración y creación del tablero
        self.grid_frame = Frame(self.master)
        self.grid_frame.pack(fill="both", expand=True)
        create_grid(self, self.rows, self.columns)

        # Agrega pozos, brisas, Wumpus, hedores y oro de forma inicial
        add_pits_and_breeze(self)
        add_wumpus_and_stench(self)
        add_gold_and_glow(self)

        # Posición inicial del agente
        self.add_image_to_cell(0, 0)
        self.current_position = (0, 0)
        self.game_over = False

        # Crear y lanzar agente
        self.agente = Agente(self)
        self.agente.resolver_juego()

    def ask_grid_size(self):
        self.rows = simpledialog.askinteger("Input", "Número de filas:", minvalue=1, maxvalue=100)
        self.columns = simpledialog.askinteger("Input", "Número de columnas:", minvalue=1, maxvalue=100)

    def add_image_to_cell(self, row, column):
        add_image_to_cell(self, row, column)

    def move_image(self, new_row, new_column):
        move_image(self, new_row, new_column)

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()