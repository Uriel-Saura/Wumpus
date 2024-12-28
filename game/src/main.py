from tkinter import Tk, Frame, simpledialog, Label, PhotoImage, messagebox, Button, TOP
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
        self.buttons_frame = None  # Agregar esta línea

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

    def mostrar_botones_final(self):
        # Crear frame para botones si no existe
        if not self.buttons_frame:
            self.buttons_frame = Frame(self.master)
            self.buttons_frame.pack(side=TOP)
            
        # Crear botones
        Button(self.buttons_frame, 
               text="Reiniciar", 
               command=self.reiniciar_juego).pack(side="left", padx=5)
        
        Button(self.buttons_frame, 
               text="Salir", 
               command=self.master.quit).pack(side="left", padx=5)
    
    def reiniciar_juego(self):
        # Limpiar el frame de botones
        if self.buttons_frame:
            self.buttons_frame.destroy()
            self.buttons_frame = None
            
        # Limpiar el tablero actual
        self.grid_frame.destroy()
        
        # Reiniciar variables
        self.game_over = False
        self.gold = []
        
        # Recrear tablero
        self.grid_frame = Frame(self.master)
        self.grid_frame.pack(fill="both", expand=True)
        create_grid(self, self.rows, self.columns)
        
        # Agregar elementos del juego
        add_pits_and_breeze(self)
        add_wumpus_and_stench(self)
        add_gold_and_glow(self)
        
        # Reiniciar posición del agente
        self.add_image_to_cell(0, 0)
        self.current_position = (0, 0)
        
        # Crear y lanzar nuevo agente
        self.agente = Agente(self)
        self.agente.resolver_juego()

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()